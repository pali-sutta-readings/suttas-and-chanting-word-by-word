"""Read the per-book metadata in books/<book>/metadata.txt.

A book's folder holds its metadata, its About page and its texts:

    books/<book>/metadata.txt
    books/<book>/00_about.md
    books/<book>/texts/NN_*.md, CHANGELOG.md          a book in one part
    books/<book>/NN_<part>/NN_*.md, CHANGELOG.md      a book in parts

The `texts` key lists the text folders, relative to the book's folder.

metadata.txt is YAML-compatible, so that pandoc can read it with
--metadata-file. This module reads the small subset it uses: `key: value`
lines, quoted or plain strings, true/false, lists (`- item`), lists of
mappings (`- folder: …` with more keys indented beneath), and one level of
nested mapping (`options:` with indented `key: value` lines).
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[2]
BOOKS_DIR = ROOT / "books"

# Keys every metadata.txt must have (docs/book-build.md).
REQUIRED = ("title", "subtitle", "lang", "pali-title-first", "texts",
            "sources", "rights", "cover-image", "about", "author", "publisher")

# Book options (docs/style-spec.md §12.2) and their values when not set.
DEFAULT_OPTIONS = {
    "heading-gloss": False,
    "heading-numbers": False,
    "repeat-across-files": False,
    "dpd-variant-rows": False,
}


class MetadataError(Exception):
    """A metadata.txt file uses syntax outside the supported subset."""


def _scalar(s):
    s = s.strip()
    if s in ("true", "false"):
        return s == "true"
    if len(s) >= 2 and s[0] == s[-1] == '"':
        return json.loads(s)
    if len(s) >= 2 and s[0] == s[-1] == "'":
        return s[1:-1].replace("''", "'")
    return s


def _split_key(s, where):
    key, sep, value = s.partition(":")
    if not sep or not key.strip() or " " in key.strip():
        raise MetadataError(f"{where}: expected 'key: value'")
    return key.strip(), value.strip()


def read_metadata(text, name="metadata.txt"):
    """Parse metadata text into a dict."""
    data = {}
    key = None          # the top-level key whose block is open
    item = None         # the mapping of the list item being read
    for no, raw in enumerate(text.splitlines(), 1):
        where = f"{name}:{no}"
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        s = raw.strip()
        if indent == 0:
            key, value = _split_key(s, where)
            item = None
            data[key] = _scalar(value) if value else None
            continue
        if key is None:
            raise MetadataError(f"{where}: indented line with no key above it")
        block = data[key]
        if s.startswith("- "):
            if block is None:
                block = data[key] = []
            if not isinstance(block, list):
                raise MetadataError(f"{where}: list item under a mapping")
            body = s[2:].strip()
            if ":" in body and not body.startswith(('"', "'")):
                k, v = _split_key(body, where)
                item = {k: _scalar(v)}
                block.append(item)
            else:
                item = None
                block.append(_scalar(body))
            continue
        k, v = _split_key(s, where)
        if item is not None:
            item[k] = _scalar(v)
            continue
        if block is None:
            block = data[key] = {}
        if not isinstance(block, dict):
            raise MetadataError(f"{where}: mapping entry under a list")
        block[k] = _scalar(v)
    return data


def load_metadata(book, books_dir=BOOKS_DIR):
    path = Path(books_dir) / book / "metadata.txt"
    return read_metadata(path.read_text(encoding="utf-8"), str(path))


@dataclass
class Part:
    folder: str                 # relative to the book's folder
    heading: Optional[str]      # part heading (books in parts), else None


@dataclass
class Book:
    id: str
    dir: Path
    meta: dict
    parts: list                 # Part, in book order

    @property
    def options(self):
        options = dict(DEFAULT_OPTIONS)
        options.update(self.meta.get("options") or {})
        return options


def load_book(book, books_dir=BOOKS_DIR):
    """Read and validate books/<book>/metadata.txt; returns a Book."""
    d = Path(books_dir) / book
    meta = load_metadata(book, books_dir)
    where = d / "metadata.txt"
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise MetadataError(f"{where}: missing keys: {', '.join(missing)}")
    for k in ("title", "lang", "rights", "about"):
        if not isinstance(meta[k], str) or not meta[k]:
            raise MetadataError(f"{where}: '{k}' must be a non-empty string")
    if not isinstance(meta["pali-title-first"], bool):
        raise MetadataError(f"{where}: 'pali-title-first' must be true or false")
    if not isinstance(meta["sources"], list) or not meta["sources"]:
        raise MetadataError(f"{where}: 'sources' must be a list")
    if not isinstance(meta["texts"], list) or not meta["texts"]:
        raise MetadataError(f"{where}: 'texts' must be a list")
    parts = []
    for t in meta["texts"]:
        if isinstance(t, dict):
            if "folder" not in t or "heading" not in t:
                raise MetadataError(f"{where}: a part needs 'folder' and 'heading'")
            parts.append(Part(t["folder"], t["heading"]))
        else:
            parts.append(Part(t, None))
    for p in parts:
        if Path(p.folder).is_absolute() or ".." in Path(p.folder).parts:
            raise MetadataError(f"{where}: text folder '{p.folder}' must be inside the book folder")
        if not (d / p.folder).is_dir():
            raise MetadataError(f"{where}: no text folder '{p.folder}' in {d}")
    if len({p.heading is None for p in parts}) > 1:
        raise MetadataError(f"{where}: give every text a heading, or none")
    unknown = set(meta.get("options") or {}) - set(DEFAULT_OPTIONS)
    if unknown:
        raise MetadataError(f"{where}: unknown options: {', '.join(sorted(unknown))}")
    return Book(book, d, meta, parts)


def folder_files(folder):
    """The text files of one text folder, in name order.

    Only `NN_name.md` files count, so CHANGELOG.md is never included. `00_`
    files are not texts and are skipped too: `00_about.md` (if a book
    folder is given) and `00_original_*`, which belong in sources/originals/.
    """
    return sorted(
        p for p in Path(folder).glob("[0-9][0-9]_*.md")
        if not p.name.startswith("00_")
    )


def book_files(book):
    """[(Part, [paths])] for a Book, in book order."""
    return [(part, folder_files(book.dir / part.folder)) for part in book.parts]


def list_books(books_dir=BOOKS_DIR):
    return sorted(
        p.parent.name for p in Path(books_dir).glob("*/metadata.txt")
    )


def book_options(book, books_dir=BOOKS_DIR):
    options = dict(DEFAULT_OPTIONS)
    options.update(load_metadata(book, books_dir).get("options") or {})
    return options


def book_for_text(path, books_dir=BOOKS_DIR):
    """The id of the book whose folder holds a text file, or None."""
    books_dir = Path(books_dir).resolve()
    for d in Path(path).resolve().parents:
        if d.parent == books_dir and (d / "metadata.txt").is_file():
            return d.name
    return None


def options_for_text(path, books_dir=BOOKS_DIR):
    """The options of the book that contains a text file (defaults if none)."""
    book = book_for_text(path, books_dir)
    return book_options(book, books_dir) if book else dict(DEFAULT_OPTIONS)
