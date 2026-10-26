#!/usr/bin/env python3
"""Assemble one book into a single pandoc-Markdown file.

Writes three files to the output folder (default build/tmp/):

    <book>.md           the About page and every text, with each element
                        wrapped in a classed fenced div (docs/book-build.md)
    <book>.meta.json    pandoc metadata from books/<book>/metadata.txt:
                        typed title and subtitle, language, rights, sources,
                        cover; keys with empty values are dropped
    <book>.pandoc.json  pandoc defaults: input, metadata file, TOC depth and
                        split level (2 for a book in parts, else 1)

With --cover-data it prints instead the JSON that templates/typst/cover.typ
reads (build/covers/<book>.json): title, subtitle, pali-title-first,
series-line, accent, site-url.

The EPUB and PDF builds both start from <book>.md, so the two formats
cannot drift apart. A lint ERROR or STRAY in the book's files gives a
warning, not a failure.
"""

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

from chantlib import books
from chantlib.books import MetadataError
from chantlib.parse import INSTRUCTION_RE, PALI_RE, parse_text
from chantlib.spec import SpecError, load_spec

import lint

ROOT = books.ROOT
COVERS_DIR = ROOT / "build" / "covers"
# Where the books are published: on the cover, the EPUB title page, and in
# the About text as {site-url}.
SITE_URL = "https://pali-sutta-readings.github.io/pali-chanting-word-by-word/"

# Line kinds that become a one-line classed div, and their class.
DIV_CLASS = {
    "subtitle": "subtitle",
    "gloss": "gloss",
    "literal": "literal",
    "faithful": "faithful",
    "repeat": "repeat",
    "rubric": "rubric",
    "variant": "variant",
    "badvariant": "variant",
}
# Line kinds that end the open unit before they are written.
CLOSES_UNIT = {"title", "heading", "pali", "citation", "bm-citation", "instruction"}
TABLE_KINDS = {"thead", "tsep", "row", "member", "badrow"}


def fenced(cls, text):
    return f"::: {cls}\n{text}\n:::\n"


def render_text(cf, shift=0):
    """One parsed chant file as pandoc Markdown; shift demotes its headings."""
    out = []
    open_unit = False

    def close():
        nonlocal open_unit
        if open_unit:
            out.append(":::\n")
            open_unit = False

    lines = cf.lines
    for i, ln in enumerate(lines):
        kind, s = ln.kind, ln.text.rstrip("\n").rstrip()
        if kind in CLOSES_UNIT:
            close()
        if kind in ("title", "heading"):
            s = "#" * shift + s
        if kind == "title":
            # The English title follows the Pāli in the table of contents;
            # epub.css hides it in the heading itself.
            en = f" [— {cf.subtitle}]{{.toc-en}}" if cf.subtitle else ""
            out.append(s + en + "\n")
        elif kind == "heading":
            out.append(s + "\n")
        elif kind == "pali":
            out.append("::: unit")
            open_unit = True
            pali = PALI_RE.match(s).group(1).strip()
            out.append(fenced('{.pali lang="pi"}', pali))
        elif kind in TABLE_KINDS:
            out.append(s)
            nxt = lines[i + 1].kind if i + 1 < len(lines) else None
            if nxt not in TABLE_KINDS:
                out.append("")
        elif kind in ("citation", "bm-citation"):
            out.append(fenced("citation", s))
        elif kind == "instruction":
            out.append(fenced("instruction", INSTRUCTION_RE.match(s).group(1)))
        elif kind in DIV_CLASS:
            out.append(fenced(DIV_CLASS[kind], s))
        elif kind == "other":
            out.append(s + "\n")
    close()
    return "\n".join(out) + "\n"


def about_text(book, today):
    text = (book.dir / book.meta["about"]).read_text(encoding="utf-8")
    text = text.replace("{today}", today).replace("{site-url}", SITE_URL)
    return text.rstrip("\n") + "\n"


def cover_path(book, covers_dir=COVERS_DIR):
    """The cover image: the metadata override, else the generated PNG if built."""
    if book.meta.get("cover-image"):
        return book.dir / book.meta["cover-image"]
    png = Path(covers_dir) / f"{book.id}.png"
    return png if png.exists() else None


def cover_data(book):
    """The cover's text, for templates/typst/cover.typ."""
    m = book.meta
    return {
        "title": m["title"],
        "subtitle": m.get("subtitle") or "",
        "pali-title-first": bool(m.get("pali-title-first")),
        "series-line": m.get("series-line") or "",
        "accent": m.get("accent") or "",
        "site-url": SITE_URL,
    }


def pandoc_metadata(book, cover=None):
    """The metadata pandoc gets; empty values are dropped (else pandoc writes
    empty dc:creator / dc:publisher elements).

    book-id and cover-pdf are for the PDF only (templates/pandoc/chant.lua):
    the book's cover data is build/covers/<book-id>.json, and cover-pdf is
    the override image, relative to the repo root."""
    m = book.meta
    title = [{"type": "main", "text": m["title"]}]
    if m.get("subtitle"):
        title.append({"type": "subtitle", "text": m["subtitle"]})
    meta = {
        "title": title,
        "lang": m["lang"],
        "rights": m["rights"],
        "source": "; ".join(m["sources"]),
        "author": m.get("author"),
        "publisher": m.get("publisher"),
        "cover-image": str(cover) if cover else None,
        "series-line": m.get("series-line"),
        "site-url": SITE_URL,
        "book-id": book.id,
        "cover-pdf": (os.path.relpath(book.dir / m["cover-image"], ROOT)
                      if m.get("cover-image") else None),
    }
    return {k: v for k, v in meta.items() if v}


def assemble(book_id, out_dir, books_dir=books.BOOKS_DIR,
             covers_dir=COVERS_DIR, today=None):
    """Write the three output files; returns the path of <book>.md."""
    book = books.load_book(book_id, books_dir)
    spec = load_spec()
    options = book.options
    parts = books.book_files(book)
    empty = [part.folder for part, fs in parts if not fs]
    if empty:
        raise MetadataError(f"{book_id}: no text files in {', '.join(empty)}")

    bad = []
    chunks = [about_text(book, today or date.today().isoformat())]
    in_parts = book.parts[0].heading is not None
    for part, fs in parts:
        if in_parts:
            chunks.append(f"# {part.heading}\n")
        for f in fs:
            text = f.read_text(encoding="utf-8")
            if any(sev in ("ERROR", "STRAY") for sev, _, _ in lint.lint_text(text, spec, options, f)):
                bad.append(f)
            chunks.append(render_text(parse_text(text, spec, options), 1 if in_parts else 0))
    if bad:
        print(f"WARNING: {book_id}: building with unresolved lint errors in: "
              + ", ".join(str(f) for f in bad), file=sys.stderr)

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / f"{book_id}.md"
    meta = out_dir / f"{book_id}.meta.json"
    defaults = out_dir / f"{book_id}.pandoc.json"
    md.write_text("\n".join(chunks), encoding="utf-8")
    # pandoc reads both files as YAML; JSON is valid YAML and needs no
    # quoting rules of its own.
    dump = lambda d: json.dumps(d, ensure_ascii=False, indent=2) + "\n"
    meta.write_text(dump(pandoc_metadata(book, cover_path(book, covers_dir))), encoding="utf-8")
    depth = 2 if in_parts else 1
    defaults.write_text(dump({
        "from": "markdown+fenced_divs",
        "input-files": [str(md)],
        "metadata-files": [str(meta)],
        "table-of-contents": True,
        "toc-depth": depth,
        "split-level": depth,
    }), encoding="utf-8")
    return md


def make_deps(book_id, books_dir=books.BOOKS_DIR):
    """A make fragment for build/deps/<book>.mk (see the Makefile).

    The book's outputs depend on its text files and on the deps file. The deps
    file depends on the text folders, so it is remade when a file is added or
    removed; the Makefile only replaces it when the list has changed.
    """
    book = books.load_book(book_id, books_dir)
    rel = lambda p: os.path.relpath(p, ROOT)
    deps_file = f"build/deps/{book_id}.mk"
    folders, files = [], []
    for part, fs in books.book_files(book):
        folders.append(rel(book.dir / part.folder))
        files += [rel(f) for f in fs]
    targets = f"build/tmp/{book_id}.md build/epub/{book_id}.epub build/pdf/{book_id}.pdf"
    rule = lambda target, deps: f"{target}: \\\n  " + " \\\n  ".join(deps) + "\n"
    return (rule(targets, [deps_file] + files)
            + rule(deps_file, [rel(book.dir / "metadata.txt")] + folders))


def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    ap.add_argument("book", help="book id, a folder name under books/")
    ap.add_argument("--out", default=str(ROOT / "build" / "tmp"), help="output folder")
    ap.add_argument("--books-dir", default=str(books.BOOKS_DIR))
    ap.add_argument("--covers-dir", default=str(COVERS_DIR))
    ap.add_argument("--today", default=os.environ.get("BUILD_DATE"),
                    help="date for {today} in the About page (default: $BUILD_DATE, else today)")
    ap.add_argument("--deps", action="store_true",
                    help="print the book's make dependencies instead of assembling")
    ap.add_argument("--cover-data", action="store_true",
                    help="print the book's cover data (JSON) instead of assembling")
    a = ap.parse_args(argv)
    try:
        if a.deps:
            sys.stdout.write(make_deps(a.book, a.books_dir))
            return 0
        if a.cover_data:
            data = cover_data(books.load_book(a.book, a.books_dir))
            sys.stdout.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            return 0
        md = assemble(a.book, a.out, a.books_dir, a.covers_dir, a.today)
    except (MetadataError, SpecError, FileNotFoundError) as e:
        sys.exit(f"assemble.py: {e}")
    print(f"assembled {md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
