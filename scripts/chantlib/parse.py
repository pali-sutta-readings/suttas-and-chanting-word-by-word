"""Parse chant files into typed lines and units.

The file layout is described in docs/style-spec.md §1 (and §12 for the
Vinaya formulae and book 10). Each line gets one kind:

    title, subtitle          `# …`, then `*…*` directly after it
    heading, gloss           `### …`; with the heading-gloss option, an
                             italic English gloss directly under a heading
    pali, literal, faithful  `**…**`, `**Literal:** …`, `**Faithful:** …`
    thead, tsep              the word-table header and separator rows
    row, member, badrow      word rows, `↳` member rows, malformed rows
    repeat, citation,        italic lines: the repeat note, a SuttaCentral
    bm-citation, rubric      or commentary citation, a BM-style (PTS)
                             citation, a listed rubric
    instruction              `> …` (Vinaya)
    variant, badvariant      `**Variant:** …`; badvariant has no unit before it
    blank, other             other = text outside the allowed structure

Lines are grouped into units: a Pāli line with its Literal and Faithful
lines, its table or repeat note, and any variants that follow it.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .spec import load_spec

PALI_RE = re.compile(r"^\*\*(?!Literal:|Faithful:|Variant:)(.+?)\*\*\s*$")
LITERAL_RE = re.compile(r"^\*\*Literal:\*\*\s+(\S.*?)\s*$")
FAITHFUL_RE = re.compile(r"^\*\*Faithful:\*\*\s+(\S.*?)\s*$")
VARIANT_RE = re.compile(r"^\*\*Variant:\*\*\s+(.+?)\s*$")
PAIR_RE = re.compile(r"\*([^*]+)\*\s*→\s*(?:\*([^*]+)\*|\(omit\))")
INSTRUCTION_RE = re.compile(r"^> (\S.*)$")
HEADING_RE = re.compile(r"^#{2,6} ")
ITALIC_RE = re.compile(r"^\*(?!\*)(.+?)\*\s*$")

TABLE_HEADER = "| Word | Analysis & Meaning |"
TABLE_SEP_RE = re.compile(r"^\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|\s*$")
ROW_RE = re.compile(
    r"^\| (?P<member>↳ )?\*\*`(?P<word>[^`]+)`\*\* \| "
    r"(?P<tags>(?:`\([^`]+\)`(?: / )?)+) (?P<rest>.+?); "
    r"\*\*\[(?P<ety>.+)\]\*\* \|\s*$"
)
TAG_GROUP_RE = re.compile(r"`\(([^)`]+)\)`")

SC_ID_RE = re.compile(
    r"^(DN|MN|SN|AN|Kp|Dhp|Ud|Iti|Snp|Vv|Pv|Thag|Thig|Ja|Cp|Bv|Mil|Ds|Vb|Dt|Pp|Kv|Ya|"
    r"Patthana|Kd|Pvr|Bu [A-Za-z]+|Bi [A-Za-z]+|Pli Tv [A-Za-z ]+) ?\d[\d.:–-]*"
    r"( \(v\. ?\d+\))?$"
)
# Commentaries keep BM's form (style spec §7); Kv. is the Kaṅkhāvitaraṇī.
COMMENTARY_RE = re.compile(
    r"^((DhpA|DhsA|Sp|Vism|Kkh|SnA|KhpA|MA|SA|AA|DA|JaA|UdA|ItA)[.\s]|Kv\.|Vinaya Mukha )"
)
BM_CITATION_RE = re.compile(r"^[A-Z][A-Za-z]*\.[IVXL]+|^(Khp|Dhp|Snp|S|A|M|D)\.")


@dataclass
class Line:
    no: int
    kind: str
    text: str


@dataclass
class Row:
    line: int
    word: str
    member: bool
    tags: str               # the raw tag part, e.g. "`(fem nom pl)` / `(ind)`"
    groups: list            # the tag groups, e.g. ["fem nom pl", "ind"]
    note: str               # the leading [note], without brackets, or ""
    meaning: str
    ety: str


@dataclass
class Variant:
    line: int
    cue: str
    pairs: list             # [(old, new)]; new is "" for (omit)
    header: bool = False
    rows: list = field(default_factory=list)      # Row, or None for a badrow
    row_lines: list = field(default_factory=list)


@dataclass
class Unit:
    line: int
    pali: str
    literal: Optional[str] = None
    literal_line: Optional[int] = None
    faithful: Optional[str] = None
    faithful_line: Optional[int] = None
    header: bool = False
    rows: list = field(default_factory=list)      # Row, or None for a badrow
    row_lines: list = field(default_factory=list)
    repeat: bool = False
    variants: list = field(default_factory=list)
    citation: Optional[str] = None


@dataclass
class ChantFile:
    path: Optional[Path]
    lines: list
    title: Optional[str] = None
    subtitle: Optional[str] = None
    units: list = field(default_factory=list)

    @property
    def stray(self):
        return [ln for ln in self.lines if ln.kind == "other"]

    def kinds(self, *kinds):
        return [ln for ln in self.lines if ln.kind in kinds]


def split_tags(tags):
    """The tag groups of a row's tag part: "`(a b)` / `(c)`" → ["a b", "c"]."""
    return [g.strip() for g in TAG_GROUP_RE.findall(tags)]


def tag_tokens(groups):
    """Every single tag in the groups; `dat/gen` gives both dat and gen."""
    return {t for g in groups for tok in g.split() for t in tok.split("/") if t}


def split_note(rest):
    """Split "[note] meaning" into (note, meaning); the note may nest brackets."""
    if not rest.startswith("["):
        return "", rest
    depth = 0
    for i, ch in enumerate(rest):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return rest[1:i], rest[i + 1:].lstrip()
    return "", rest


def split_row(line, no=0):
    """Parse one table row; returns a Row, or None if it breaks the row format."""
    m = ROW_RE.match(line.rstrip())
    if not m:
        return None
    note, meaning = split_note(m.group("rest"))
    return Row(
        line=no,
        word=m.group("word"),
        member=bool(m.group("member")),
        tags=m.group("tags"),
        groups=split_tags(m.group("tags")),
        note=note,
        meaning=meaning,
        ety=m.group("ety"),
    )


def _last_kind(lines):
    return next((ln.kind for ln in reversed(lines) if ln.kind != "blank"), None)


def classify(lines, spec=None, options=None):
    """Parse a list of text lines; returns a ChantFile (with path None).

    spec is the dict from chantlib.spec.load_spec() (loaded if not given);
    options are the book options (only heading-gloss changes the parse).
    """
    spec = spec or load_spec()
    options = options or {}
    rubrics = set(spec["rubrics"])
    repeat_note = spec["repeat-note"]

    cf = ChantFile(path=None, lines=[])
    out = cf.lines
    unit = None      # the current unit
    target = None    # the unit or variant that receives table rows
    subtitle_open = False

    def add(no, kind, text):
        out.append(Line(no, kind, text))

    for no, raw in enumerate(lines, 1):
        s = raw.rstrip("\n").rstrip()
        if not s.strip():
            add(no, "blank", raw)
            continue
        if s.startswith("# ") and cf.title is None:
            cf.title = s[2:].strip()
            subtitle_open = True
            add(no, "title", raw)
            continue
        m = ITALIC_RE.match(s)
        if subtitle_open and m and not m.group(1).strip().startswith("("):
            # A rubric (in parentheses) is never the English title.
            subtitle_open = False
            cf.subtitle = m.group(1).strip()
            add(no, "subtitle", raw)
            continue
        subtitle_open = False

        if HEADING_RE.match(s):
            unit = target = None
            add(no, "heading", raw)
            continue
        if options.get("heading-gloss") and m and _last_kind(out) == "heading":
            add(no, "gloss", raw)
            continue

        mv = VARIANT_RE.match(s)
        if mv:
            if unit is None:
                target = None
                add(no, "badvariant", raw)
                continue
            pairs = [(old, new or "") for old, new in PAIR_RE.findall(mv.group(1))]
            target = Variant(line=no, cue=mv.group(1), pairs=pairs)
            unit.variants.append(target)
            add(no, "variant", raw)
            continue
        if INSTRUCTION_RE.match(s):
            add(no, "instruction", raw)
            continue

        mp = PALI_RE.match(s)
        if mp:
            unit = target = Unit(line=no, pali=mp.group(1).strip())
            cf.units.append(unit)
            add(no, "pali", raw)
            continue
        ml = LITERAL_RE.match(s)
        if ml:
            if unit:
                unit.literal, unit.literal_line = ml.group(1), no
            add(no, "literal", raw)
            continue
        mf = FAITHFUL_RE.match(s)
        if mf:
            if unit:
                unit.faithful, unit.faithful_line = mf.group(1), no
            add(no, "faithful", raw)
            continue

        if s.startswith("|"):
            if s.strip() == TABLE_HEADER:
                if target:
                    target.header = True
                add(no, "thead", raw)
                continue
            if TABLE_SEP_RE.match(s):
                add(no, "tsep", raw)
                continue
            row = split_row(s, no)
            if target is not None:
                target.rows.append(row)
                target.row_lines.append(no)
            kind = "badrow" if row is None else ("member" if row.member else "row")
            add(no, kind, raw)
            continue

        if m:
            inner = m.group(1).strip()
            if inner == repeat_note:
                if unit:
                    unit.repeat = True
                add(no, "repeat", raw)
                continue
            if inner in rubrics:
                add(no, "rubric", raw)
                continue
            parts = [p.strip() for p in inner.split(";")]
            if all(SC_ID_RE.match(p) or COMMENTARY_RE.match(p) for p in parts):
                if cf.units:
                    cf.units[-1].citation = inner
                add(no, "citation", raw)
                continue
            if BM_CITATION_RE.match(inner):
                add(no, "bm-citation", raw)
                continue
        add(no, "other", raw)
    return cf


def parse_text(text, spec=None, options=None):
    return classify(text.splitlines(), spec, options)


def parse_file(path, spec=None, options=None):
    path = Path(path)
    cf = parse_text(path.read_text(encoding="utf-8"), spec, options)
    cf.path = path
    return cf
