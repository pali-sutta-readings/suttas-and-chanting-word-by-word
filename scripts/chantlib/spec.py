"""Read the machine-readable rule blocks from docs/style-spec.md.

The style spec keeps four rule lists in fenced code blocks, named by their
info string: ``tags``, ``rubrics``, ``english-stopwords`` and ``repeat-note``
(see the note at the top of docs/style-spec.md). The checks read them from
there, so that the rules and the checks never drift apart.
"""

from pathlib import Path

SPEC_PATH = Path(__file__).resolve().parents[2] / "docs" / "style-spec.md"

# Blocks that hold a list, one entry per line.
LIST_BLOCKS = ("tags", "rubrics", "english-stopwords")
# Blocks that hold one line of text.
TEXT_BLOCKS = ("repeat-note",)

FENCE = "```"


class SpecError(Exception):
    """The style spec is missing, or lacks a required block."""


def read_blocks(text):
    """Return {info string: [lines]} for every fenced block in text.

    A block opens with a line that is the fence followed by an info string
    (e.g. ```tags) and closes with a line that is the bare fence.
    """
    blocks = {}
    name = None
    for line in text.splitlines():
        stripped = line.strip()
        if name is None:
            if stripped.startswith(FENCE) and len(stripped) > len(FENCE):
                name = stripped[len(FENCE):].strip()
                blocks.setdefault(name, [])
        elif stripped == FENCE:
            name = None
        else:
            blocks[name].append(line)
    if name is not None:
        raise SpecError(f"unclosed {FENCE}{name} block")
    return blocks


def load_spec(path=SPEC_PATH):
    """Load the rule blocks from the style spec.

    Returns a dict: each list block maps to its entries (stripped, blank lines
    and lines starting with # skipped), in file order; ``repeat-note`` maps to
    its text. Raises SpecError if the file or a block is missing, or if
    ``repeat-note`` is empty.
    """
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SpecError(f"style spec not found: {path}") from None

    blocks = read_blocks(text)
    spec = {}
    for name in LIST_BLOCKS + TEXT_BLOCKS:
        if name not in blocks:
            raise SpecError(f"{path} has no {FENCE}{name} block")
        entries = [
            s for s in (line.strip() for line in blocks[name])
            if s and not s.startswith("#")
        ]
        if name in TEXT_BLOCKS:
            if not entries:
                raise SpecError(f"{path}: the {FENCE}{name} block is empty")
            spec[name] = " ".join(entries)
        else:
            spec[name] = entries
    return spec
