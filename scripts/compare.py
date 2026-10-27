#!/usr/bin/env python3
"""Compare the Pāli lines of the texts with their reference passages.

Usage:
    compare.py extract FILE              our text's normalised Pāli stream
    compare.py extract --ref TEXT        the mapped reference passage of TEXT
    compare.py diff [TEXT...]            report over sources/ref-map.tsv

sources/ref-map.tsv names each text's reference passage. It is written and
kept by the source-compare skill (.claude/skills/source-compare/); this
script never guesses it. The key syntax, the two modes and the structural
rules are described in docs/script-or-skill.md (spike 1) and
docs/quality-process.md §2:

    bm, ccb,        anchor | anchor..end | anchor..END
    original
    sc              segment..segment          (inclusive)
    chanting-guide  heading | heading..end heading  (contain mode only)
    none            no reference; the note says why

An `sc` entry names a SuttaCentral text by its Simsapa uid (`dn22/pli/ms`)
in the file column; its segments come from the Simsapa API, GET /sutta.json
(docs/simsapa-cli-and-localhost-api.md §13.4). When Simsapa is not
running, those entries are skipped and listed; SIMSAPA_FIXTURES answers them
from recorded responses, as for simsapa.py.

Mode `diff` compares our stream with the extracted reference stream.
Mode `contain` checks that each of our Pāli lines occurs, in order, in the
normalised raw passage, English included (the BM Vinaya pages, where no
markup separates the Pāli from the English).

`diff` is a report: it exits 0 whatever the differences, and 1 only when a
map entry is broken (a missing anchor, segment, file or column).
"""

import argparse
import difflib
import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib import books
from chantlib.parse import parse_file
from chantlib.text import norm_line

import simsapa

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "sources" / "ref-map.tsv"
COLUMNS = ("text", "source", "file", "key", "mode", "note")
SOURCES = ("bm", "ccb", "original", "sc", "chanting-guide", "none")
MODES = ("diff", "contain")
CONTEXT = 40

HEADING_RE = re.compile(r"^(#+)\s")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"')
DIV_RE = re.compile(r'^<div class="(english|instr)">')
ITALIC_LINE_RE = re.compile(r"^\*(?!\*)[^*].*\*$")
LINK_RE = re.compile(r"\]\(https?://")
TAG_RE = re.compile(r"<[^>]+>")
# SuttaCentral title (`:0.n`) and heading (`.0`, `.0.n`) segments.
SC_HEADING_RE = re.compile(r":0\.|\.0(\.\d+)?$")


class MapError(Exception):
    """A map entry that cannot be resolved; the message names the entry."""


@dataclass
class Entry:
    line: int
    text: str
    source: str
    file: str
    key: str
    mode: str
    note: str

    def where(self):
        return f"ref-map.tsv:{self.line} ({self.text})"


def read_map(path=MAP):
    """The map entries, in file order. The first line is the column header."""
    path = Path(path)
    entries = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != COLUMNS:
        raise MapError(f"{path.name}:1: header must be: {' '.join(COLUMNS)}")
    for no, raw in enumerate(lines[1:], 2):
        if not raw.strip() or raw.startswith("#"):
            continue
        cols = raw.split("\t")
        if len(cols) != len(COLUMNS):
            raise MapError(f"{path.name}:{no}: expected {len(COLUMNS)} tab-separated columns, got {len(cols)}")
        e = Entry(no, *cols)
        e.mode = e.mode or "diff"
        if e.source not in SOURCES:
            raise MapError(f"{e.where()}: unknown source {e.source!r}")
        if e.mode not in MODES:
            raise MapError(f"{e.where()}: unknown mode {e.mode!r}")
        if e.source == "chanting-guide" and e.mode != "contain":
            raise MapError(f"{e.where()}: chanting-guide entries need mode contain")
        entries.append(e)
    return entries


# ------------------------------------------------------------------ our texts

def our_units(path):
    """[(line, normalised Pāli)] for each unit of one of our texts.

    Only the Pāli lines count: variant cues, rubrics, instructions and
    headings are other line kinds, and norm_line() drops `(×3)`.
    """
    cf = parse_file(path, options=books.options_for_text(path))
    return [(u.line, norm_line(u.pali)) for u in cf.units]


# ------------------------------------------------------------------ BM Markdown

def bm_passage(lines, key, where):
    """The lines of a keyed BM passage, without its own heading.

    `anchor` runs to the next heading that carries an anchor; `anchor..end`
    runs up to the line with anchor `end`, and `anchor..END` to the end.
    An anchor is usually on a heading; BM also puts a few on other lines
    (`**1.**<a id="yankinci-vittam"></a>`), and then the passage starts
    with that line.
    """
    start, sep, end = key.partition("..")
    anchors = [(i, m.group(1), bool(HEADING_RE.match(s)))
               for i, s in enumerate(lines) for m in ANCHOR_RE.finditer(s)]
    at = [(i, head) for i, a, head in anchors if a == start]
    if len(at) != 1:
        raise MapError(f"{where}: anchor {start!r} {'not found' if not at else 'found twice'}")
    i0, on_heading = at[0]
    if not sep:
        later = [i for i, _, head in anchors if head and i > i0]
        i1 = later[0] if later else len(lines)
    elif end == "END":
        i1 = len(lines)
    else:
        ends = [i for i, a, _ in anchors if a == end and i > i0]
        if not ends:
            raise MapError(f"{where}: end anchor {end!r} not found after {start!r}")
        i1 = ends[0]
    return lines[i0 + 1 if on_heading else i0:i1]


def bm_clean(lines):
    """The Pāli lines of a BM passage, by BM's markup only.

    Drops the English and rubric divs, headings, the Contents list, wholly
    italic lines (citations, English titles), wholly italic table cells
    (English glosses) and link lines; removes HTML
    tags and entities, the blockquote `>`, the line-end `\\` and the leader
    brackets (keeping their words). Nothing here decides by language.
    """
    out, in_div, in_contents = [], False, False
    for raw in lines:
        s = raw.strip()
        if in_div:
            in_div = not s.startswith("</div>")
            continue
        if DIV_RE.match(s):
            in_div = True
            continue
        if s == "**Contents**":
            in_contents = True
            continue
        if in_contents:
            if not s or s.startswith("- ["):
                continue
            in_contents = False
        if HEADING_RE.match(s) or LINK_RE.search(s):
            continue
        if s.startswith("|"):
            # A table row: wholly italic cells are English (the 32 parts).
            cells = [c.strip() for c in s.strip("|").split("|")]
            s = " ".join(c for c in cells if c and not ITALIC_LINE_RE.match(c)
                         and not re.fullmatch(r":?-+:?", c))
        s = html.unescape(TAG_RE.sub("", s)).strip()
        s = re.sub(r"^>\s?", "", s)
        s = re.sub(r"\\$", "", s).strip()
        if not s or ITALIC_LINE_RE.match(s):
            continue
        out.append(s.replace("[", "").replace("]", ""))
    return out


def raw_text(lines):
    """A passage with only HTML tags and entities removed (for contain mode)."""
    return [html.unescape(TAG_RE.sub(" ", s)) for s in lines]


# ------------------------------------------------------------------ segments

def segment_range(ids, key, where):
    first, sep, last = key.partition("..")
    if not sep:
        raise MapError(f"{where}: segment key must be first..last, got {key!r}")
    for k in (first, last):
        if k not in ids:
            raise MapError(f"{where}: segment {k!r} not found")
    i, j = ids.index(first), ids.index(last)
    if j < i:
        raise MapError(f"{where}: segment {last!r} comes before {first!r}")
    return ids[i:j + 1]


_suttas = {}


def sutta_segments(uid, where):
    """{segment id: text} of a SuttaCentral text, in the text's order, from Simsapa."""
    if uid not in _suttas:
        try:
            status, data = simsapa.client().get("/sutta.json", uid=uid)
        except simsapa.SimsapaError as err:
            raise Skipped(err) from None
        if status != 200:
            try:
                reason = json.loads(data).get("reason")
            except ValueError:
                reason = f"HTTP {status}"
            raise MapError(f"{where}: Simsapa has no SuttaCentral text {uid!r} ({reason})")
        _suttas[uid] = json.loads(data)  # keeps the key order, which is the text's
    return _suttas[uid]


def sc_lines(uid, key, where):
    segs = sutta_segments(uid, where)
    ids = segment_range(list(segs), key, where)
    return [segs[k] for k in ids if not SC_HEADING_RE.search(k)]


def heading_passage(lines, key, where):
    """From the heading whose text is `start` up to the heading `end` (or the end of the file).

    The key is `start` or `start..end`. Each heading must occur exactly once.
    """
    start, sep, end = key.partition("..")

    def find(text, after=-1):
        at = [i for i, s in enumerate(lines) if i > after and HEADING_RE.match(s)
              and HEADING_RE.sub("", s).strip() == text.strip()]
        if len(at) != 1:
            raise MapError(f"{where}: heading {text!r} {'not found' if not at else 'found twice'}")
        return at[0]

    i0 = find(start)
    i1 = find(end, i0) if sep else len(lines)
    return lines[i0 + 1:i1]


# ------------------------------------------------------------------ references

class Skipped(Exception):
    """A reference that is not available here (an optional local copy)."""


def ref_lines(e, root=ROOT):
    """The reference passage of an entry: cleaned lines (diff mode) or raw lines (contain)."""
    if e.source == "sc":
        return sc_lines(e.file, e.key, e.where())
    path = root / e.file
    if not path.is_file():
        if e.source == "chanting-guide":
            raise Skipped(f"no local copy at {e.file}")
        raise MapError(f"{e.where()}: file {e.file} not found")
    if e.source in ("bm", "ccb", "original"):
        sec = bm_passage(path.read_text(encoding="utf-8").splitlines(), e.key, e.where())
        return raw_text(sec) if e.mode == "contain" else bm_clean(sec)
    if e.source == "chanting-guide":
        return raw_text(heading_passage(path.read_text(encoding="utf-8").splitlines(), e.key, e.where()))
    raise MapError(f"{e.where()}: source {e.source} has no reference")


def stream(lines):
    return "".join(norm_line(s) for s in lines)


# ------------------------------------------------------------------ reports

def _unit_at(units, offsets, pos):
    """The line number of the unit that holds stream position pos."""
    for (line, _), off in zip(reversed(units), reversed(offsets)):
        if pos >= off:
            return line
    return units[0][0] if units else 0


def diff_report(units, ref, ctx=CONTEXT):
    """Difference lines between our units and a reference stream."""
    ours = "".join(k for _, k in units)
    offsets, n = [], 0
    for _, k in units:
        offsets.append(n)
        n += len(k)
    sm = difflib.SequenceMatcher(None, ours, ref, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        line = _unit_at(units, offsets, i1)
        out.append(f"  line {line}: {op}\n"
                   f"    ours …{ours[max(0, i1 - ctx):i1]}⟦{ours[i1:i2]}⟧{ours[i2:i2 + ctx]}…\n"
                   f"    ref  …{ref[max(0, j1 - ctx):j1]}⟦{ref[j1:j2]}⟧{ref[j2:j2 + ctx]}…")
    return out


def contain_report(units, ref):
    """Our Pāli lines that do not occur, in order, in the reference stream."""
    out, pos = [], 0
    for line, k in units:
        if not k:
            continue
        at = ref.find(k, pos)
        if at >= 0:
            pos = at + len(k)
        elif k in ref:
            out.append(f"  line {line}: out of order: {k}")
        else:
            out.append(f"  line {line}: not found: {k}")
    return out


def compare_entry(e, root=ROOT):
    """(status, lines) for one map entry; raises MapError for a broken entry."""
    text = root / e.text
    if not text.is_file():
        raise MapError(f"{e.where()}: text not found")
    if e.source == "none":
        return "no reference", [f"  {e.note}"] if e.note else []
    try:
        ref = stream(ref_lines(e, root))
    except Skipped as s:
        return f"skipped: {s}", []
    units = our_units(text)
    found = contain_report(units, ref) if e.mode == "contain" else diff_report(units, ref)
    if not found:
        return "identical" if e.mode == "diff" else "all lines found", []
    n = len(found)
    if e.mode == "diff":
        return f"{n} difference{'s' if n > 1 else ''}", found
    return f"{n} line{'s' if n > 1 else ''} not found", found


def all_texts(root=ROOT):
    """Every text in books/, repo-relative, in book order."""
    out = []
    bd = root / "books"
    for b in books.list_books(bd):
        book = books.load_book(b, bd)
        out += [str(f.relative_to(root)) for _, fs in books.book_files(book) for f in fs]
    return out


def run_diff(entries, only=None, root=ROOT, out=None):
    """Print the report; return the number of broken entries."""
    out = out or sys.stdout
    errors = 0
    only = {str(Path(t)) for t in only} if only else None
    for e in entries:
        if only and e.text not in only:
            continue
        head = f"## {e.text}  [{e.source}{' ' + e.file if e.file else ''}{' ' + e.key if e.key else ''}; {e.mode}]"
        try:
            status, lines = compare_entry(e, root)
        except MapError as m:
            errors += 1
            print(f"{head}\nMAP ERROR: {m}\n", file=out)
            continue
        print(f"{head}\n{status}", file=out)
        for ln in lines:
            print(ln, file=out)
        print(file=out)
    if not only and (root / "books").is_dir():
        mapped = {e.text for e in entries}
        missing = [t for t in all_texts(root) if t not in mapped]
        if missing:
            print(f"## Texts with no map entry ({len(missing)})", file=out)
            for t in missing:
                print(f"  {t}", file=out)
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0],
                                 epilog="See docs/quality-process.md §2.")
    ap.add_argument("--map", default=str(MAP), help="the reference map (default: sources/ref-map.tsv)")
    ap.add_argument("--root", default=str(ROOT), help="base folder of the paths in the map")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("extract", help="print a normalised Pāli stream")
    p.add_argument("file", metavar="FILE|TEXT")
    p.add_argument("--ref", action="store_true", help="print the mapped reference passage of TEXT")
    p.add_argument("--plain", action="store_true", help="print the reference lines without normalising them")
    p = sub.add_parser("diff", help="report differences over the map")
    p.add_argument("texts", nargs="*", metavar="TEXT")
    a = ap.parse_args(argv)
    root = Path(a.root)

    try:
        if a.cmd == "extract" and not a.ref:
            for line, k in our_units(Path(a.file)):
                print(f"{line}\t{k}")
            return 0
        entries = read_map(a.map)
        if a.cmd == "extract":
            hits = [e for e in entries if e.text == str(Path(a.file))]
            if not hits:
                raise MapError(f"{a.file}: no map entry")
            for e in hits:
                try:
                    lines = ref_lines(e, root) if e.source != "none" else []
                except Skipped as s:
                    print(f"skipped: {s}", file=sys.stderr)
                    continue
                for s in lines:
                    s = s.strip()
                    if s:
                        print(s if a.plain else norm_line(s))
            return 0
        return 1 if run_diff(entries, a.texts, root) else 0
    except MapError as m:
        print(f"compare.py: {m}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
