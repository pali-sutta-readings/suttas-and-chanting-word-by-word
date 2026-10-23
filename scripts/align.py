#!/usr/bin/env python3
"""Bulk alignment of word-table rows by rules, with a log for the changelog.

Usage:
    align.py TREE RULES.json LOG.json            dry run: print the diff
    align.py TREE RULES.json LOG.json --apply    write the files and the log
    align.py --changelog LOG.json                the Was/Now tables for CHANGELOG.md

TREE is a folder (books/, a book, or a text folder) or one text file.
RULES.json is a list of rules:

    {"word": "bhagav",                regex, searched in the row's word cell
     "cell": "etym",                  etym (default) | tags | meaning
     "old": "√bhaj + a + vant",
     "new": "√bhaj > bhag + a + vant",
     "match": "cell",                 cell (default) | substring
     "why": "DPD construction of bhagavant",
     "ref": "DPD bhagavant 1"}

A rule changes only the named cell of a row whose word cell matches `word`.
With "match": "cell", `old` must equal the whole cell: the etymology inside
**[…]**, the tag part (`(masc nom sg)`, with or without the backticks) or
the meaning. With "substring", `old` is replaced inside the cell, and a cell
that already contains `new` is skipped, so that running the rules again
changes nothing (docs/script-or-skill.md, spike 1). The rules and the "why"
are the agent's work (the dpd-review skill); this script only applies them.
"""

import argparse
import difflib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib.parse import ROW_RE, split_note

ROOT = Path(__file__).resolve().parents[1]
CELLS = ("etym", "tags", "meaning")
MATCHES = ("cell", "substring")


class RuleError(Exception):
    pass


def load_rules(path):
    rules = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rules, list):
        raise RuleError(f"{path}: expected a list of rules")
    for n, r in enumerate(rules, 1):
        for k in ("word", "old", "new"):
            if not isinstance(r.get(k), str) or (k != "new" and not r[k]):
                raise RuleError(f"{path}: rule {n}: '{k}' is required")
        r.setdefault("cell", "etym")
        r.setdefault("match", "cell")
        if r["cell"] not in CELLS:
            raise RuleError(f"{path}: rule {n}: cell must be one of {', '.join(CELLS)}")
        if r["match"] not in MATCHES:
            raise RuleError(f"{path}: rule {n}: match must be one of {', '.join(MATCHES)}")
        try:
            r["_re"] = re.compile(r["word"])
        except re.error as e:
            raise RuleError(f"{path}: rule {n}: bad word regex: {e}")
    return rules


def text_files(tree):
    tree = Path(tree)
    if tree.is_file():
        return [tree]
    return sorted(p for p in tree.rglob("[0-9][0-9]*.md") if not p.name.startswith("00_"))


def cell_span(line, cell):
    """(start, end) of a cell's content in a row, or None if the line is not a row."""
    m = ROW_RE.match(line)
    if not m:
        return None
    if cell == "etym":
        return m.span("ety")
    if cell == "tags":
        return m.span("tags")
    meaning = split_note(m.group("rest"))[1]
    end = m.end("rest")
    return end - len(meaning), end


def _same_tags(cell, old):
    plain = " / ".join(re.findall(r"`\(([^)`]+)\)`", cell))
    return old.strip() in (cell.strip(), plain, f"({plain})")


def apply_rule(line, rule):
    """(new line, old cell, new cell) if the rule changes the line; ('skip', …) if
    a substring rule finds `new` already there; None otherwise."""
    if not line.startswith("|"):
        return None
    word_cell = line.split("|")[1]
    if not rule["_re"].search(word_cell):
        return None
    span = cell_span(line.rstrip("\n"), rule["cell"])
    if span is None:
        return None
    a, b = span
    cell = line[a:b]
    old, new = rule["old"], rule["new"]
    if rule["match"] == "cell":
        if rule["cell"] == "tags":
            if not _same_tags(cell, old):
                return None
            # Keep the backticked form of the file if the rule omits it.
            if not new.startswith("`"):
                new = " / ".join(f"`({g.strip().strip('()')})`" for g in new.split(" / "))
        elif cell.strip() != old.strip():
            return None
        changed = new
    else:
        if new and new in cell:
            return ("skip", cell, cell)
        if old not in cell:
            return None
        changed = cell.replace(old, new)
    return line[:a] + changed + line[b:], cell, changed


def word_of(line):
    m = ROW_RE.match(line.rstrip("\n"))
    return m.group("word") if m else re.sub(r"[*`↳ ]", "", line.split("|")[1])


def align(files, rules, root=ROOT):
    """{path: (old text, new text)} for changed files, the log, and the skip count."""
    changed, log, skipped = {}, [], 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        for i, line in enumerate(lines):
            for r in rules:
                res = apply_rule(line, r)
                if res is None:
                    continue
                if res[0] == "skip":
                    skipped += 1
                    continue
                new_line, was, now = res
                log.append(dict(file=_rel(f, root), line=i + 1, word=word_of(line), cell=r["cell"],
                                old=was, new=now, why=r.get("why", ""), ref=r.get("ref", "")))
                lines[i] = line = new_line
        new_text = "\n".join(lines)
        if new_text != text:
            changed[f] = (text, new_text)
    return changed, log, skipped


def _rel(path, root=ROOT):
    try:
        return str(Path(path).resolve().relative_to(Path(root).resolve()))
    except ValueError:
        return str(path)


def changelog(log):
    """The Was/Now tables, one per file, in the changelog format (style spec §11)."""
    by_file = defaultdict(lambda: defaultdict(list))
    for e in log:
        key = (e["word"], e["cell"], e["old"], e["new"], e["why"], e["ref"])
        by_file[e["file"]][key].append(e["line"])
    out = []
    for f in sorted(by_file):
        out += [f"### {Path(f).name}", "| Line | Was | Now | Why | Reference |", "| :--- | :--- | :--- | :--- | :--- |"]
        for (word, cell, old, new, why, ref), nos in sorted(by_file[f].items(), key=lambda kv: kv[1][0]):
            was = f"*{word}* {old}" if cell != "tags" else f"*{word}* {old.strip()}"
            out.append(f"| {', '.join(map(str, nos))} | {was} | {new} | {why} | {ref} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0],
                                 epilog="See docs/quality-process.md §6.")
    ap.add_argument("tree", nargs="?", help="folder or text file")
    ap.add_argument("rules", nargs="?", help="rules JSON")
    ap.add_argument("log", nargs="?", help="log JSON, written with --apply")
    ap.add_argument("--apply", action="store_true", help="write the files and the log")
    ap.add_argument("--changelog", metavar="LOG", help="print the Was/Now tables from a log")
    a = ap.parse_args(argv)

    if a.changelog:
        print(changelog(json.loads(Path(a.changelog).read_text(encoding="utf-8"))), end="")
        return 0
    if not (a.tree and a.rules and a.log):
        ap.error("TREE, RULES and LOG are required (or --changelog LOG)")
    try:
        rules = load_rules(a.rules)
    except RuleError as e:
        sys.exit(f"align.py: {e}")
    files = text_files(a.tree)
    if not files:
        sys.exit(f"align.py: no text files in {a.tree}")
    changed, log, skipped = align(files, rules)
    for f, (old, new) in changed.items():
        sys.stdout.writelines(difflib.unified_diff(
            old.splitlines(keepends=True), new.splitlines(keepends=True),
            fromfile=_rel(f), tofile=_rel(f), n=0))
        if a.apply:
            f.write_text(new, encoding="utf-8")
    if a.apply:
        Path(a.log).write_text(json.dumps(log, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    mode = "applied" if a.apply else "dry run, nothing written"
    print(f"{len(log)} changes in {len(changed)} files; {skipped} cells already aligned ({mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
