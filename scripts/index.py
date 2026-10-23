#!/usr/bin/env python3
"""Cross-file index of the word tables: consistency reports and lookups.

Usage:
    index.py index [--folder X] [--all-tags]   same word, different etymology or tags
    index.py dupes [--lines]                   texts (or Pāli lines) that occur twice
    index.py stats                             counts per book
    index.py rows WORD... [--json]             the commonest settled rows for a word
    index.py overlaps FILE...                  Pāli lines equal to a line elsewhere

All subcommands read every text in books/ (--books for another tree). They
are reports, never a gate: many conflicts are legitimate (homonyms, tags
set by the line), and the dpd-review skill decides which to align
(docs/quality-process.md §6). Tag conflicts are compared by word class by
default, leaving out case, number and the gender of words that agree with
another (docs/script-or-skill.md, spike 1); --all-tags compares whole tags.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib import books
from chantlib.parse import parse_file
from chantlib.text import nfc, norm_line

ROOT = Path(__file__).resolve().parents[1]

# Tags that name a word's class, and the classes whose gender follows the
# word they agree with (style spec §5).
CLASS_TAGS = set("pp prp ptp abs inf ind adv adj pron rel dem interr card ord "
                 "prefix sandhi interj comp caus denom".split())
AGREEING = {"adj", "pp", "prp", "ptp", "pron", "rel", "dem", "interr", "card", "ord"}
GENDERS = ("masc", "fem", "nt")


@dataclass
class Occurrence:
    path: Path
    line: int
    raw: str          # the row as written
    row: object       # chantlib.parse.Row

    def where(self, root=ROOT):
        return f"{_rel(self.path, root)}:{self.line}"


def _rel(path, root=ROOT):
    try:
        return str(Path(path).resolve().relative_to(Path(root).resolve()))
    except ValueError:
        return str(path)


def all_texts(books_dir=books.BOOKS_DIR):
    out = []
    for b in books.list_books(books_dir):
        book = books.load_book(b, books_dir)
        out += [f for _, fs in books.book_files(book) for f in fs]
    return out


def parsed(paths):
    """[(path, ChantFile)] with each book's options."""
    return [(p, parse_file(p, options=books.options_for_text(p))) for p in paths]


def word_key(word):
    return nfc(word).lower()


def occurrences(files):
    """{word: [Occurrence]} for every table row, variant rows included."""
    out = defaultdict(list)
    for path, cf in files:
        lines = cf.lines
        by_no = {ln.no: ln.text for ln in lines}
        for u in cf.units:
            pairs = list(zip(u.rows, u.row_lines))
            for v in u.variants:
                pairs += list(zip(v.rows, v.row_lines))
            for row, no in pairs:
                if row is not None:
                    out[word_key(row.word)].append(Occurrence(path, no, by_no[no].rstrip(), row))
    return out


def tag_class(groups):
    """A row's tags reduced to its word class (see the module docstring)."""
    out = []
    for g in groups:
        toks = [t for tok in g.split() for t in tok.split("/")]
        keep = [t for t in toks if t in CLASS_TAGS]
        if not AGREEING & set(toks):
            keep += [t for t in toks if t in GENDERS]
        out.append(" ".join(keep))
    return " / ".join(sorted(set(out)))


# ------------------------------------------------------------------ index

def conflicts(occ, key):
    """{word: {value: [Occurrence]}} for words with more than one value."""
    out = {}
    for w, os in occ.items():
        groups = defaultdict(list)
        for o in os:
            groups[key(o.row)].append(o)
        if len(groups) > 1:
            out[w] = dict(groups)
    return out


def _in_folder(os, folder, root):
    return any(folder in _rel(o.path, root) for o in os)


def _locs(os, root, n=6):
    return ", ".join(o.where(root) for o in os[:n]) + (" …" if len(os) > n else "")


def index_report(occ, folder=None, all_tags=False, root=ROOT):
    ety = conflicts(occ, lambda r: r.ety.strip())
    tags = conflicts(occ, (lambda r: " / ".join(r.groups)) if all_tags else (lambda r: tag_class(r.groups)))
    if folder:
        ety = {w: g for w, g in ety.items() if _in_folder([o for os in g.values() for o in os], folder, root)}
        tags = {w: g for w, g in tags.items() if _in_folder([o for os in g.values() for o in os], folder, root)}
    out = ["# Cross-file consistency report", ""]
    out += [f"## Same word, different etymology ({len(ety)} words)", "",
            "E lines. Align unless the words are different lemmas (homonyms).", ""]
    for w in sorted(ety):
        out.append(f"### `{w}`")
        for value, os in sorted(ety[w].items(), key=lambda kv: -len(kv[1])):
            out.append(f"- E [{value}] — {len(os)}×: {_locs(os, root)}")
        out.append("")
    what = "tags" if all_tags else "word class"
    out += [f"## Same word, different {what} ({len(tags)} words)", "",
            "T lines. " + ("Case, number and gender often depend on the line; check each."
                           if all_tags else "Case, number and agreeing gender are left out (--all-tags shows them)."), ""]
    for w in sorted(tags):
        parts = [f"({v or '—'}) {len(os)}×, e.g. {os[0].where(root)}"
                 for v, os in sorted(tags[w].items(), key=lambda kv: -len(kv[1]))]
        out.append(f"- T `{w}`: " + "; ".join(parts))
    return "\n".join(out)


# ------------------------------------------------------------------ dupes, stats

def dupes_report(files, lines=False, root=ROOT):
    out = []
    streams = defaultdict(list)
    for path, cf in files:
        s = "".join(norm_line(u.pali) for u in cf.units)
        if s:
            streams[s].append(path)
    same = [ps for ps in streams.values() if len(ps) > 1]
    out.append(f"## Texts with identical Pāli ({len(same)})")
    for ps in same:
        out.append("- " + " = ".join(_rel(p, root) for p in ps))
    if lines:
        seen = defaultdict(list)
        for path, cf in files:
            for u in cf.units:
                k = norm_line(u.pali)
                if k:
                    seen[k].append((path, u.line, u.pali))
        rep = {k: v for k, v in seen.items() if len({p for p, _, _ in v}) > 1}
        out += ["", f"## Pāli lines in more than one text ({len(rep)})"]
        for k, v in sorted(rep.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- {v[0][2]} — {len(v)}×: " + ", ".join(f"{_rel(p, root)}:{n}" for p, n, _ in v[:6])
                       + (" …" if len(v) > 6 else ""))
    return "\n".join(out)


def book_of(path):
    return books.book_for_text(path) or Path(path).parent.name


def stats_report(files):
    total = Counter()
    per = defaultdict(Counter)
    words = defaultdict(set)
    for path, cf in files:
        c = per[book_of(path)]
        c["texts"] += 1
        for u in cf.units:
            c["units"] += 1
            c["tables"] += bool(u.rows)
            c["repeat notes"] += u.repeat
            c["variants"] += len(u.variants)
            for r in u.rows + [r for v in u.variants for r in v.rows]:
                if r is None:
                    continue
                c["member rows" if r.member else "rows"] += 1
                words[book_of(path)].add(word_key(r.word))
    cols = ["texts", "units", "tables", "repeat notes", "variants", "rows", "member rows"]
    out = ["| Book | " + " | ".join(cols) + " | distinct words |",
           "| :--- |" + " ---: |" * (len(cols) + 1)]
    allw = set()
    for b in sorted(per):
        out.append(f"| {b} | " + " | ".join(str(per[b][k]) for k in cols) + f" | {len(words[b])} |")
        total.update(per[b])
        allw |= words[b]
    out.append("| **all** | " + " | ".join(str(total[k]) for k in cols) + f" | {len(allw)} |")
    return "\n".join(out)


# ------------------------------------------------------------------ rows, overlaps

def common_rows(occ, word, n=2, root=ROOT):
    """The n commonest rows for a word, as written: [(row, count, first place)]."""
    key = word_key(word).replace("'", "").replace("’", "")
    os = occ.get(word_key(word)) or [o for w, oss in occ.items()
                                     if w.replace("'", "").replace("’", "") == key for o in oss]
    counts = Counter()
    first = {}
    for o in os:
        text = re.sub(r"^\| ↳ ", "| ", o.raw)
        counts[text] += 1
        first.setdefault(text, o.where(root))
    return [(r, c, first[r]) for r, c in counts.most_common(n)]


def overlaps_report(targets, files, root=ROOT):
    """Pāli lines of the targets that equal a line in another text folder."""
    where = defaultdict(list)
    for path, cf in files:
        for u in cf.units:
            k = norm_line(u.pali)
            if k:
                kind = "table" if u.rows else ("repeat" if u.repeat else "no table")
                where[k].append((Path(path).resolve(), u.line, kind))
    out = []
    for path, cf in targets:
        folder = Path(path).resolve().parent
        for u in cf.units:
            others = [w for w in where.get(norm_line(u.pali), []) if w[0].parent != folder]
            if not others:
                continue
            best = sorted(others, key=lambda w: w[2] != "table")
            out.append(f"{_rel(path, root)}:{u.line}: {u.pali}\n    = "
                       + "; ".join(f"{_rel(p, root)}:{n} ({kind})" for p, n, kind in best[:4]))
    return "\n".join(out) if out else "no overlaps"


def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0],
                                 epilog="See docs/quality-process.md §6.")
    ap.add_argument("--books", default=str(books.BOOKS_DIR), help="the books folder (default: books/)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index", help="same word, different etymology or tags")
    p.add_argument("--folder", help="only conflicts with a row in a path containing FOLDER")
    p.add_argument("--all-tags", action="store_true", help="compare whole tags, not word class")
    p = sub.add_parser("dupes", help="texts with identical Pāli")
    p.add_argument("--lines", action="store_true", help="also list Pāli lines found in more than one text")
    sub.add_parser("stats", help="counts per book")
    p = sub.add_parser("rows", help="the commonest settled rows for a word")
    p.add_argument("words", nargs="+", metavar="WORD")
    p.add_argument("-n", type=int, default=2, help="how many rows (default 2)")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("overlaps", help="Pāli lines equal to a line in another folder")
    p.add_argument("files", nargs="+", metavar="FILE")
    a = ap.parse_args(argv)

    bd = Path(a.books)
    root = bd.resolve().parent
    files = parsed(all_texts(bd))
    if a.cmd == "index":
        print(index_report(occurrences(files), a.folder, a.all_tags, root))
    elif a.cmd == "dupes":
        print(dupes_report(files, a.lines, root))
    elif a.cmd == "stats":
        print(stats_report(files))
    elif a.cmd == "rows":
        occ = occurrences(files)
        found = {w: common_rows(occ, w, a.n, root) for w in a.words}
        if a.json:
            print(json.dumps([{"word": w, "rows": [{"row": r, "count": c, "first": f} for r, c, f in rs]}
                              for w, rs in found.items()], ensure_ascii=False, indent=1))
        else:
            for w, rs in found.items():
                print(f"## {w}" + ("" if rs else ": no settled rows"))
                for r, c, f in rs:
                    print(f"{r}    ← {c}×, first {f}")
    elif a.cmd == "overlaps":
        print(overlaps_report(parsed([Path(f) for f in a.files]), files, root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
