"""Read the per-book metadata in books/<book>/metadata.txt.

metadata.txt is YAML-compatible, so that pandoc can read it with
--metadata-file. This module reads the small subset it uses: `key: value`
lines, quoted or plain strings, true/false, lists (`- item`), lists of
mappings (`- folder: …` with more keys indented beneath), and one level of
nested mapping (`options:` with indented `key: value` lines).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOKS_DIR = ROOT / "books"

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


def list_books(books_dir=BOOKS_DIR):
    return sorted(
        p.parent.name for p in Path(books_dir).glob("*/metadata.txt")
    )


def text_folders(meta):
    """The texts/ folders of a book, in order (a part is a {folder: …} mapping)."""
    return [t["folder"] if isinstance(t, dict) else t for t in meta.get("texts") or []]


def book_options(book, books_dir=BOOKS_DIR):
    options = dict(DEFAULT_OPTIONS)
    options.update(load_metadata(book, books_dir).get("options") or {})
    return options


def book_for_folder(folder, books_dir=BOOKS_DIR):
    """The book whose `texts` lists this texts/ folder, or None."""
    for book in list_books(books_dir):
        if folder in text_folders(load_metadata(book, books_dir)):
            return book
    return None


def options_for_text(path, books_dir=BOOKS_DIR):
    """The options of the book that contains a text file (defaults if none)."""
    book = book_for_folder(Path(path).resolve().parent.name, books_dir)
    return book_options(book, books_dir) if book else dict(DEFAULT_OPTIONS)
