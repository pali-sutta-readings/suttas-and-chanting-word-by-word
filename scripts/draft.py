#!/usr/bin/env python3
"""Compact draft format ↔ chant file.

Usage:
    draft.py build DRAFT OUT.md        write a chant file from a draft
    draft.py extract FILE.md           print a chant file as a draft

A draft has one item per line; `#` lines and blank lines are ignored.
docs/drafting-workflow.md describes the workflow; the file layout is
docs/style-spec.md §1.

    T|title                    # title
    E|English title            *English title* (after T); after H, the gloss (book 10)
    H|heading                  ### heading
    U|rubric                   *(rubric)*
    S|instruction              > instruction (Vinaya)
    P|Pāli line                a unit; a full table, or the repeat note if the
                               same line came earlier in the draft
    P!|Pāli line               force a full table
    P~|Pāli line               force the repeat note
    L|literal  F|faithful      the unit's Literal and Faithful lines
    R|word|tags|meaning|etym   a table row; tags without parentheses, groups
                               separated by " / "; meaning may start with a [note]
    M|word|tags|meaning|etym   a ↳ member row
    T0|                        a table header with no rows (after P or V)
    V|cue                      **Variant:** cue; the R|/M| rows after it are its table
    C|citation                 *citation*
    I|text path|Pāli line      copy the unit of another text whose Pāli line
                               has the same normalised key (text.norm_line);
                               an error if no unit or more than one has it

`extract` then `build` gives the file back byte for byte, for any file that
follows the layout of the style spec.
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib import books
from chantlib.parse import parse_file, parse_text
from chantlib.spec import load_spec
from chantlib.text import norm_line

ROOT = Path(__file__).resolve().parents[1]
TABLE_HEADER = "| Word | Analysis & Meaning |"
TABLE_SEP = "| :--- | :--- |"


class DraftError(Exception):
    pass


def repeat_note():
    return load_spec()["repeat-note"]


def row_line(fields, member):
    word, tags, rest, ety = (fields + ["", "", "", ""])[:4]
    tagf = " / ".join(f"`({g.strip()})`" for g in tags.split(" / "))
    return f"| {'↳ ' if member else ''}**`{word.strip()}`** | {tagf} {rest.strip()}; **[{ety.strip()}]** |"


# ------------------------------------------------------------------ build

def unit_block(path, key, where, root=ROOT):
    """The lines of the unit in `path` whose Pāli line has normalised key `key`."""
    p = root / path
    if not p.is_file():
        raise DraftError(f"{where}: {path} not found")
    cf = parse_file(p, options=books.options_for_text(p))
    hits = [u for u in cf.units if norm_line(u.pali) == key]
    if len(hits) != 1:
        raise DraftError(f"{where}: {'no unit' if not hits else f'{len(hits)} units'} with that Pāli line in {path}")
    u = hits[0]
    stop = {"pali", "heading", "gloss", "citation", "bm-citation", "rubric", "instruction", "title"}
    last = u.line
    for ln in cf.lines:
        if ln.no <= u.line:
            continue
        if ln.kind in stop:
            break
        if ln.kind != "blank":
            last = ln.no
    return [ln.text.rstrip("\n") for ln in cf.lines if u.line <= ln.no <= last]


def build(draft_text, root=ROOT, name="draft"):
    """The chant file for a draft."""
    note = f"*{repeat_note()}*"
    out, seen, cur = [], set(), None

    def flush():
        nonlocal cur
        if cur is None:
            return
        if cur["kind"] == "V":
            out.extend([f"**Variant:** {cur['text']}  ", ""])
            if cur["rows"] or cur["header"]:
                out.extend([TABLE_HEADER, TABLE_SEP] + cur["rows"] + [""])
        else:
            k = norm_line(cur["text"])
            rep = (k in seen and cur["force"] != "!") or cur["force"] == "~"
            seen.add(k)
            out.extend([f"**{cur['text']}**", ""])
            if cur["L"] is not None or cur["F"] is not None:
                if cur["L"] is not None:
                    out.append(f"**Literal:** {cur['L']}  ")
                if cur["F"] is not None:
                    out.append(f"**Faithful:** {cur['F']}  ")
                out.append("")
            if rep:
                out.extend([note, ""])
            elif cur["rows"] or cur["header"]:
                out.extend([TABLE_HEADER, TABLE_SEP] + cur["rows"] + [""])
        cur = None

    for no, raw in enumerate(draft_text.splitlines(), 1):
        where = f"{name}:{no}"
        line = raw.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        tag, sep, rest = line.partition("|")
        if not sep:
            raise DraftError(f"{where}: no '|' after the item tag")
        if tag in ("P", "P!", "P~"):
            flush()
            cur = dict(kind="P", text=rest.strip(), force=tag[1:], L=None, F=None, rows=[], header=False)
        elif tag == "V":
            flush()
            cur = dict(kind="V", text=rest.strip(), rows=[], header=False)
        elif tag in ("L", "F", "R", "M", "T0"):
            if cur is None or (tag in ("L", "F") and cur["kind"] != "P"):
                raise DraftError(f"{where}: {tag}| needs a P| line before it")
            if tag in ("L", "F"):
                cur[tag] = rest.strip()
            elif tag == "T0":
                cur["header"] = True
            else:
                cur["rows"].append(row_line(rest.split("|"), tag == "M"))
        else:
            flush()
            if tag == "T":
                out.extend([f"# {rest.strip()}", ""])
            elif tag == "E":
                out.extend([f"*{rest.strip()}*", ""])
            elif tag == "H":
                out.extend([f"### {rest.strip()}", ""])
            elif tag == "U":
                out.extend([f"*({rest.strip()})*", ""])
            elif tag == "C":
                out.extend([f"*{rest.strip()}*", ""])
            elif tag == "S":
                out.extend([f"> {rest.strip()}", ""])
            elif tag == "I":
                path, sep2, pali = rest.partition("|")
                if not sep2:
                    raise DraftError(f"{where}: I| needs a text path and a Pāli line")
                block = unit_block(path.strip(), norm_line(pali), where, root)
                for x in block:
                    m = re.match(r"^\*\*(?!Literal:|Faithful:|Variant:)(.+?)\*\*\s*$", x)
                    if m:
                        seen.add(norm_line(m.group(1)))
                out.extend(block + [""])
            else:
                raise DraftError(f"{where}: unknown item {tag}|")
    flush()
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
    return unicodedata.normalize("NFC", text)


# ------------------------------------------------------------------ extract

def extract(path, options=None):
    """The draft for a chant file. Raises DraftError for a line outside the layout."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    options = options if options is not None else books.options_for_text(path)
    cf = parse_text(text, options=options)
    out, seen = [], set()
    units = {u.line: u for u in cf.units}
    variants = {v.line: v for u in cf.units for v in u.variants}
    for ln in cf.lines:
        s = ln.text.rstrip("\n").rstrip()
        k = ln.kind
        if k in ("blank", "thead", "tsep", "repeat", "literal", "faithful", "row", "member"):
            continue          # written with their unit
        if k == "title":
            out.append(f"T|{cf.title}")
        elif k in ("subtitle", "gloss"):
            out.append(f"E|{s[1:-1].strip()}")
        elif k == "heading":
            if not s.startswith("### "):
                raise DraftError(f"{path}:{ln.no}: only ### headings are allowed")
            out.append(f"H|{s[4:]}")
        elif k == "rubric":
            out.append(f"U|{s[2:-2]}")
        elif k in ("citation", "bm-citation"):
            out.append(f"C|{s[1:-1]}")
        elif k == "instruction":
            out.append(f"S|{s[2:]}")
        elif k == "pali":
            u = units[ln.no]
            key = norm_line(u.pali)
            auto_rep = key in seen
            seen.add(key)
            force = "" if u.repeat == auto_rep else ("~" if u.repeat else "!")
            out.append(f"P{force}|{u.pali}")
            if u.literal is not None:
                out.append(f"L|{u.literal}")
            if u.faithful is not None:
                out.append(f"F|{u.faithful}")
            out += _rows(u, path)
        elif k == "variant":
            v = variants[ln.no]
            out.append(f"V|{v.cue}")
            out += _rows(v, path)
        else:
            raise DraftError(f"{path}:{ln.no}: line kind {k!r} has no draft form: {s[:60]}")
    draft = "\n".join(out) + "\n"
    rebuilt = build(draft, name=str(path))
    if rebuilt != text:
        a, b = text.splitlines(), rebuilt.splitlines()
        no = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b))) + 1
        raise DraftError(f"{path}:{no}: the layout differs from the style spec's, so a draft "
                         f"would not give this file back: {a[no - 1] if no <= len(a) else '(end of file)'!r}")
    return draft


def _rows(target, path):
    out = []
    for row, no in zip(target.rows, target.row_lines):
        if row is None:
            raise DraftError(f"{path}:{no}: malformed table row")
        groups = " / ".join(row.groups)
        rest = (f"[{row.note}] " if row.note else "") + row.meaning
        out.append(f"{'M' if row.member else 'R'}|{row.word}|{groups}|{rest}|{row.ety}")
    if target.header and not target.rows:
        out.append("T0|")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0],
                                 epilog="See docs/drafting-workflow.md.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("build", help="write a chant file from a draft")
    p.add_argument("draft")
    p.add_argument("out")
    p = sub.add_parser("extract", help="print a chant file as a draft")
    p.add_argument("file")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "build":
            text = build(Path(a.draft).read_text(encoding="utf-8"), name=a.draft)
            Path(a.out).write_text(text, encoding="utf-8")
            print(f"wrote {a.out}")
        else:
            sys.stdout.write(extract(a.file))
    except DraftError as e:
        print(f"draft.py: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
