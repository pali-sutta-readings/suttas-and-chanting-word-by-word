#!/usr/bin/env python3
"""Lint chant files against docs/style-spec.md, and apply safe fixes.

Usage: lint.py [--fix] [--book BOOK] PATH...

A PATH is a chant file or a texts/ folder (its NN_*.md files; never
CHANGELOG.md). The allowed tags, rubrics, English stopwords and the repeat
note are read from the fenced blocks in docs/style-spec.md. Book options
(style spec §12.2) come from books/<book>/metadata.txt: from --book, or else
from the book whose `texts` lists the file's folder.

Output: `path:line: SEVERITY message`, then a total. Severities:
ERROR (breaks a rule), STRAY (text outside the allowed structure), WARN (to
check by hand; some are expected and explained in docs/legacy-migration.md).
The exit code is 1 if there is any ERROR or STRAY.

--fix applies only the safe fixes (style spec §1 and §5): NFC, ṃ → ṁ,
`---` lines removed, and the unambiguous tag synonyms. It writes the file
in place and prints one "safe fixes applied" line per changed file.
"""

import argparse
import difflib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib import books
from chantlib.parse import TAG_GROUP_RE, parse_text, tag_tokens
from chantlib.spec import SpecError, load_spec
from chantlib.text import (
    SANSKRIT_LETTERS,
    TONE_MARKS,
    fold_niggahita,
    is_pali_letter,
    nfc,
    norm_line,
)

SEVERITIES = ("ERROR", "STRAY", "WARN")

# Unambiguous synonyms only (style spec §5, approved 2026-10-01).
TAG_SYNONYMS = {
    "cmpd": "comp", "compound": "comp", "inst": "instr", "ins": "instr",
    "ppp": "pp", "ppr": "prp", "indcl": "ind",
}

# Word classes for which DPD gives no root (style spec §6).
NO_ROOT_TAGS = {"ind", "adv", "interj", "pron", "dem", "rel", "interr", "card", "prefix"}
PERSONS = {"1st", "2nd", "3rd"}
VERB_TAGS = {"pres", "aor", "fut", "perf", "cond", "imperat", "opt", "indic", "act", "mid", "pass"}

# Canonical tag order (style spec §5): the rank of each token in a group.
# A group with a person and a verb tag is a finite verb; a person without
# one is a personal pronoun; anything else is nominal.
_NOMINAL = ["adj pp prp ptp card ord rel dem interr ind adv abs inf interj prefix sandhi",
            "pron", "caus denom pass", "masc fem nt",
            "nom acc instr dat abl gen loc voc", "sg pl", "comp"]
_VERB = ["1st 2nd 3rd", "sg pl", "pres aor fut perf", "caus denom", "pass",
         "act mid", "indic imperat opt cond", "comp"]
_PERSONAL = ["1st 2nd 3rd", "sg pl", "nom acc instr dat abl gen loc voc", "comp"]
TAG_ORDER = {
    name: {tok: rank for rank, toks in enumerate(order) for tok in toks.split()}
    for name, order in (("nominal", _NOMINAL), ("verb", _VERB), ("personal pronoun", _PERSONAL))
}

MAX_INSTRUCTION_WORDS = 45


def text_files(paths):
    out = []
    for p in map(Path, paths):
        if p.is_dir():
            out += sorted(
                f for f in p.glob("[0-9]*.md")
                if not f.name.startswith("00_original_")
            )
        else:
            out.append(p)
    return out


# ------------------------------------------------------------------ tags

def tag_problems(groups, allowed):
    probs = []
    for grp in groups:
        if grp == "masc/fem/nt":
            probs.append("generic tag 'masc/fem/nt'")
        for tok in grp.split():
            for t in tok.split("/"):
                if t and t not in allowed:
                    probs.append(f"tag '{t}' not in allowed list")
        order = tag_order_problem(grp)
        if order:
            probs.append(order)
    return probs


def tag_order_problem(group):
    toks = group.split()
    first = {tok.split("/")[0] for tok in toks}
    if first & PERSONS:
        scheme = "verb" if first & VERB_TAGS else "personal pronoun"
    else:
        scheme = "nominal"
    ranks = TAG_ORDER[scheme]
    known = [(ranks[t], t) for t in (tok.split("/")[0] for tok in toks) if t in ranks]
    if [r for r, _ in known] != sorted(r for r, _ in known):
        want = " ".join(tok for _, tok in sorted(
            ((ranks.get(tok.split("/")[0], 99), tok) for tok in toks), key=lambda x: x[0]))
        return f"tags not in canonical {scheme} order: ({group}); expected ({want})"
    return None


def rootless_ok(groups):
    """True for indeclinables and pronouns, where DPD gives no root."""
    toks = tag_tokens(groups)
    if toks & NO_ROOT_TAGS:
        return True
    return bool(toks & PERSONS) and not (toks & VERB_TAGS)


# ------------------------------------------------------------------ tables

def coverage_problem(pali, rows):
    """None if the row words, read in order, spell out the Pāli exactly."""
    words = [r.word for r in rows if r and not r.member]
    a, b = norm_line(pali), norm_line("".join(words))
    if a == b:
        return None
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    diffs = [f"{op}: line '{a[i1:i2]}' vs rows '{b[j1:j2]}'"
             for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    return "table words do not cover the Pāli line exactly (" + "; ".join(diffs[:3]) + ")"


def row_issues(rows, spec, issues):
    """Tag, etymology and compound-member checks for one table."""
    allowed = set(spec["tags"])
    good = [r for r in rows if r]
    for r in good:
        for prob in tag_problems(r.groups, allowed):
            issues.append(("ERROR", r.line, prob))
        ety = r.ety
        if ("√" not in ety and "+" not in ety and "(trad.)" not in ety
                and len(ety.split()) < 2 and not rootless_ok(r.groups)):
            issues.append(("WARN", r.line, f"etymology has no root or construction: [{ety}]"))
    for k, r in enumerate(good):
        if r.member:
            heads = [x for x in good[:k] if not x.member]
            if not heads or "comp" not in tag_tokens(heads[-1].groups):
                issues.append(("ERROR", r.line, "member row (↳) not under a compound row"))
        elif "comp" in tag_tokens(r.groups):
            members = 0
            for r2 in good[k + 1:]:
                if not r2.member:
                    break
                members += 1
            if members < 2:
                issues.append(("WARN", r.line,
                               f"compound `{r.word}` needs a member row (↳) for each part"))


def variant_words(v):
    """The words a variant table must cover: each pair's new words that are
    not among its old words, in order."""
    out = []
    for old, new in v.pairs:
        pool = [norm_line(w) for w in old.split()]
        for w in new.split():
            if norm_line(w) in pool:
                pool.remove(norm_line(w))
            else:
                out.append(w)
    return out


def variant_issues(v, seen_pali, spec, issues):
    """Style spec §12.1: a cue names *old* → *new* pairs; its table covers the new words."""
    n = v.line
    if not v.pairs:
        issues.append(("ERROR", n, "variant cue has no *old* → *new* pair (style spec §12.1)"))
        return
    for old, _ in v.pairs:
        key = norm_line(old)
        if not any(key in s for ln, s in seen_pali if ln < n):
            issues.append(("WARN", n, f"variant replaces '{old}', which is not in any "
                                      "earlier Pāli line or variant"))
    words = variant_words(v)
    if not words:
        if v.rows:
            issues.append(("ERROR", n, "variant only omits or reorders words but has a table"))
        return
    if not v.header:
        issues.append(("ERROR", n, "variant: missing word table header"))
    if not v.rows:
        issues.append(("ERROR", n, f"variant: no word rows for {' '.join(words)}"))
        return
    row_issues(v.rows, spec, issues)
    cov = coverage_problem(" ".join(words), v.rows)
    # Or every word on the right: agreement changes (style spec §12.1).
    whole = " ".join(new for _, new in v.pairs)
    if cov and coverage_problem(whole, v.rows):
        issues.append(("ERROR", n, "variant " + cov.replace("Pāli line", "new words")))


# ------------------------------------------------------------------ files

def earlier_tables(path, spec, options):
    """Normalised Pāli of every unit with a full table in the files before
    this one in its folder (the repeat-across-files option)."""
    out = set()
    for f in text_files([path.parent]):
        if f.name >= path.name:
            continue
        cf = parse_text(f.read_text(encoding="utf-8"), spec, options)
        out |= {norm_line(u.pali) for u in cf.units if not u.repeat and u.rows}
    return out


def char_issues(text, issues):
    if nfc(text) != text:
        issues.append(("ERROR", 0, "text is not Unicode NFC (decomposed diacritics)"))
    for n, line in enumerate(text.splitlines(), 1):
        if "ṃ" in line or "Ṃ" in line:
            issues.append(("ERROR", n, "ṃ found; use ṁ"))
        if TONE_MARKS.search(line):
            issues.append(("ERROR", n, "tone mark character found"))
        m = SANSKRIT_LETTERS.search(line)
        if m:
            issues.append(("ERROR", n, f"Sanskrit-only letter: {m.group(0)}"))
        if "\\sqrt" in line or "$" in line:
            issues.append(("ERROR", n, "LaTeX in text"))
        if re.search(r"\[cite:|TBD|```", line):
            issues.append(("ERROR", n, "leftover prompt artefact ([cite], TBD or code fence)"))
        if "\t" in line:
            issues.append(("WARN", n, "tab character"))
        if " " in line or " " in line:
            issues.append(("ERROR", n, "non-breaking space"))


def non_pali_letters(s):
    """Letters outside the Pāli alphabet; ṃ is reported by char_issues instead."""
    s = fold_niggahita(s)
    return sorted({ch for ch in s if ch.isalpha() and not is_pali_letter(ch)})


def line_issues(cf, spec, options, issues):
    stop = {w.lower() for w in spec["english-stopwords"]}
    if cf.title is None:
        issues.append(("ERROR", 1, "no '# ' title line"))
    lines = cf.lines
    for idx, ln in enumerate(lines):
        n, k, s = ln.no, ln.kind, ln.text.rstrip("\n")
        if k == "other":
            if s.strip() == "---":
                issues.append(("STRAY", n, "'---' separator line (lint --fix removes it)"))
            else:
                issues.append(("STRAY", n, f"text outside the allowed structure: {s[:90]}"))
        elif k == "badrow":
            issues.append(("ERROR", n, f"table row does not match the row format: {s[:90]}"))
        elif k == "bm-citation":
            issues.append(("WARN", n, f"BM-style citation; use the SuttaCentral ID: {s.strip()}"))
        elif k == "badvariant":
            issues.append(("ERROR", n, "variant line with no formula before it (style spec §12.1)"))
        elif k in ("literal", "faithful", "variant"):
            if not s.endswith("  "):
                issues.append(("WARN", n, f"{k} line does not end with two spaces"))
        elif k == "instruction":
            if "**" in s or "|" in s:
                issues.append(("STRAY", n, f"instruction line contains bold or table text: {s[:90]}"))
            words = len(s.split()) - 1
            if words > MAX_INSTRUCTION_WORDS:
                issues.append(("WARN", n, f"instruction line has {words} words; keep only who "
                                          "speaks, when, and short setup (style spec §12.1)"))
        elif k == "heading":
            words = re.findall(r"[^\W\d_]+", s.lower())
            if any(w in stop for w in words):
                issues.append(("STRAY", n, f"English section heading: {s}"))
            if options.get("heading-numbers"):
                if not re.match(r"^#{2,6} \d+(\.\d+)* \S", s) or re.match(r"^#{2,6} [\d.]+\. ", s):
                    issues.append(("WARN", n, "heading should be '### <SC number without "
                                              f"final dot> <Pāli heading>': {s}"))
            elif re.search(r"\d", s):
                issues.append(("STRAY", n, f"digit in section heading: {s}"))
            if options.get("heading-gloss"):
                nxt = next((x.kind for x in lines[idx + 1:] if x.kind != "blank"), None)
                if nxt != "gloss":
                    issues.append(("WARN", n, "heading has no *English gloss* line beneath it"))


def unit_issues(cf, spec, options, issues):
    stop = {w.lower() for w in spec["english-stopwords"]}
    units = cf.units
    seen_pali = [(u.line, norm_line(u.pali)) for u in units] + [
        (v.line, norm_line(new)) for u in units for v in u.variants for _, new in v.pairs
    ]
    for u in units:
        for v in u.variants:
            variant_issues(v, seen_pali, spec, issues)
        n, p = u.line, u.pali
        if re.search(r"[\[\]]", p):
            issues.append(("ERROR", n, "square brackets in Pāli line (leader brackets must be removed)"))
        rest = re.sub(r"\(×\d\)", "", p)
        if re.search(r"[()]", rest):
            issues.append(("STRAY", n, f"parenthesis in Pāli line: {p}"))
        eng = [w for w in re.findall(r"[^\W\d_]+", rest) if w.lower() in stop]
        if eng:
            issues.append(("STRAY", n, f"English word(s) in Pāli line: {', '.join(eng)}"))
        if re.search(r"\d", rest):
            issues.append(("STRAY", n, f"digit in Pāli line: {p}"))
        bad = non_pali_letters(rest)
        if bad:
            issues.append(("ERROR", n, f"letter(s) outside the Pāli alphabet: {' '.join(bad)}"))
        if not u.literal_line:
            issues.append(("ERROR", n, "missing **Literal:** line"))
        if not u.faithful_line:
            issues.append(("ERROR", n, "missing **Faithful:** line"))
        if u.repeat:
            if u.rows:
                issues.append(("ERROR", n, "repeat note and a table on the same line"))
            continue
        if not u.header:
            issues.append(("ERROR", n, "missing word table header"))
        if not u.rows:
            issues.append(("ERROR", n, "no word rows"))
            continue
        for r in u.rows + [r for v in u.variants for r in v.rows]:
            if r and non_pali_letters(r.word):
                issues.append(("ERROR", r.line, "letter(s) outside the Pāli alphabet in "
                                                f"`{r.word}`: {' '.join(non_pali_letters(r.word))}"))
        row_issues(u.rows, spec, issues)
        cov = coverage_problem(p, u.rows)
        if cov:
            issues.append(("ERROR", n, cov))

    # A later identical line uses the repeat note (style spec §8).
    seen = {}
    for u in units:
        key = norm_line(u.pali)
        if key in seen and not u.repeat:
            issues.append(("WARN", u.line, f"repeat of line {seen[key]} written out in full; "
                                           "use the repeat note"))
        seen.setdefault(key, u.line)
    earlier = (earlier_tables(cf.path, spec, options)
               if options.get("repeat-across-files") and cf.path else set())
    for u in units:
        if not u.repeat:
            continue
        before = {norm_line(x.pali) for x in units if x.line < u.line and not x.repeat}
        if norm_line(u.pali) not in earlier | before:
            issues.append(("ERROR", u.line, "repeat note used, but no earlier full table for this line"))


def lint_text(text, spec, options, path=None):
    """Return the issues of one file's text, as (severity, line, message)."""
    issues = []
    char_issues(text, issues)
    cf = parse_text(text, spec, options)
    cf.path = Path(path) if path else None
    line_issues(cf, spec, options, issues)
    unit_issues(cf, spec, options, issues)
    return sorted(issues, key=lambda i: (i[1], SEVERITIES.index(i[0])))


# ------------------------------------------------------------------ fixes

def fix_tags(group):
    """Map the unambiguous synonyms to canonical tokens; drop a repeated token."""
    group = re.sub(r"\bin (?:cmpd|compound)\b", "comp", group)
    toks = []
    for tok in group.split():
        t = "/".join(TAG_SYNONYMS.get(x, x) for x in tok.split("/"))
        if t not in toks:
            toks.append(t)
    return " ".join(toks)


def safe_fixes(text):
    """Apply the safe fixes; returns the new text."""
    text = nfc(text).replace("ṃ", "ṁ").replace("Ṃ", "Ṁ")
    out = []
    lines = text.split("\n")
    skip_blank = False
    for i, line in enumerate(lines):
        if line.strip() == "---":
            # Drop the separator, and one blank line if it sat between two.
            prev_blank = not out or not out[-1].strip()
            next_blank = i + 1 < len(lines) and not lines[i + 1].strip()
            skip_blank = prev_blank and next_blank
            continue
        if skip_blank and not line.strip():
            skip_blank = False
            continue
        skip_blank = False
        out.append(line)
    text = "\n".join(out)
    return TAG_GROUP_RE.sub(lambda m: "`(" + fix_tags(m.group(1)) + ")`", text)


# ------------------------------------------------------------------ main

def main(argv=None):
    ap = argparse.ArgumentParser(
        description=(__doc__ or "").split("\n\n")[0],
        epilog="See docs/style-spec.md and docs/quality-process.md.",
    )
    ap.add_argument("paths", nargs="+", metavar="PATH")
    ap.add_argument("--fix", action="store_true", help="apply the safe fixes in place")
    ap.add_argument("--book", help="take book options from books/BOOK/metadata.txt")
    ap.add_argument("--spec", default=None, help="style spec (default: docs/style-spec.md)")
    a = ap.parse_args(argv)

    try:
        spec = load_spec(a.spec) if a.spec else load_spec()
    except SpecError as e:
        sys.exit(f"lint.py: {e}")

    total = Counter()
    files = text_files(a.paths)
    if not files:
        sys.exit("lint.py: no chant files found")
    for f in files:
        options = books.book_options(a.book) if a.book else books.options_for_text(f)
        text = f.read_text(encoding="utf-8")
        if a.fix:
            new = safe_fixes(text)
            if new != text:
                f.write_text(new, encoding="utf-8")
                print(f"{f}: safe fixes applied")
                text = new
        for sev, n, msg in lint_text(text, spec, options, f):
            total[sev] += 1
            print(f"{f}:{n}: {sev} {msg}")
    summary = ", ".join(f"{total[s]} {s}" for s in SEVERITIES)
    print(f"TOTAL ({len(files)} files): {summary}")
    return 1 if total["ERROR"] or total["STRAY"] else 0


if __name__ == "__main__":
    sys.exit(main())
