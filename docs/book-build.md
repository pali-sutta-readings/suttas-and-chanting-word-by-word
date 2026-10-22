# Book build

How the 13 books are made from `texts/` and `books/`. The commands are Make targets (`make help`).

## The pipeline

```text
books/<book>/metadata.txt ─┐
books/<book>/about.md ─────┼─ scripts/assemble.py ─→ build/tmp/<book>.md ─┬─ pandoc ─→ build/epub/<book>.epub ─→ epubcheck
texts/<folder>/NN_*.md ────┘                         build/tmp/<book>.meta.yaml
                                                     build/tmp/<book>.pandoc.yaml
```

The EPUB and the PDF both start from the same assembled Markdown, so the two formats cannot drift apart.

## Book metadata: `books/<book>/metadata.txt`

YAML-compatible `key: value` lines, so that pandoc can also read the file with `--metadata-file`. `scripts/chantlib/books.py` reads it with a small reader that knows only what these files use: strings (quote any value that holds `:`), `true`/`false`, lists, a list of mappings, and one nested mapping (`options`). `load_book()` rejects a file with a missing key.

| Key | Value |
| :--- | :--- |
| `title`, `subtitle` | The title and subtitle as they appear on the book. |
| `lang` | `en-GB`. |
| `pali-title-first` | `true` when the title is the Pāli one (04a *Paritta*, 05 *Anumodanā*); otherwise the title is English and the subtitle Pāli. It tells the cover which line is Pāli; it does not reorder the two. |
| `series-line` | The short line printed on the cover, e.g. "Pāli with word-by-word English". |
| `accent` | Optional cover accent colour. |
| `texts` | The `texts/` folders of the book, in order. A book in parts (09) lists `folder` + `heading` mappings instead; each heading becomes a level-1 part heading, and the chants under it move down one level. |
| `sources` | A list: the attribution of the Pāli sources and references. Written to the EPUB as `dc:source` (joined with `; `). |
| `rights` | The licence line (`dc:rights`). |
| `cover-image` | Empty: use the generated cover `build/covers/<book>.png` when it has been built. A path (relative to the book folder) overrides it. |
| `about` | The About file, normally `about.md`. |
| `author`, `publisher` | Empty on purpose (maintainer decision, 2026-10-22: no wrong attribution). Empty keys are dropped before pandoc sees them, because pandoc would otherwise write empty `dc:creator`/`dc:publisher` elements. |
| `options` | Book options for lint and parsing (style spec §12.2): `heading-gloss`, `heading-numbers`, `repeat-across-files`, `dpd-variant-rows`. All default to `false`; only book 10 sets them. |

## About text: `books/<book>/about.md`

Plain Markdown, placed before the texts. `{today}` is replaced with the build date (`$BUILD_DATE` if set, else today). The level-2 headings are `{.unnumbered .unlisted}`, so that they stay out of the table of contents. Keep the AI-disclosure paragraphs.

## Assembly: `scripts/assemble.py BOOK`

For each folder in `texts`, the files `NN_*.md` are taken in name order. `CHANGELOG.md` and `00_original_*` are never included. Each file is parsed with `chantlib.parse`, and each line kind is written as:

| Line kind | Output |
| :--- | :--- |
| `title` | `# Pāli title [— English title]{.toc-en}`; the span shows in the table of contents and is hidden in the heading by CSS |
| `subtitle` | `::: subtitle` |
| `heading`, `gloss` (book 10) | the heading as it is; `::: gloss` |
| `pali` | opens `::: unit`, then `::: {.pali lang="pi"}` with the bold markers removed |
| `literal`, `faithful` | `::: literal`, `::: faithful` |
| table rows | the Markdown table as it is |
| `repeat`, `rubric`, `variant` | `::: repeat`, `::: rubric`, `::: variant` |
| `citation` | closes the unit, then `::: citation` |
| `instruction` (Vinaya) | closes the unit, then `::: instruction` with the `> ` removed |

A unit closes at the next Pāli line, heading, title, citation or instruction line. A lint ERROR or STRAY in the book's files prints a warning; the book is still built.

`<book>.meta.yaml` is the metadata pandoc gets (written as JSON, which is valid YAML): a typed title (`main` and `subtitle`, so that both reach the EPUB package), `lang`, `rights`, `source`, and `cover-image`. `<book>.pandoc.yaml` is a pandoc defaults file with the input, the metadata file, the table of contents, and the TOC depth and split level: 1, or 2 for a book in parts.

## EPUB

```sh
pandoc --defaults build/tmp/<book>.pandoc.yaml --css templates/epub.css \
  --epub-embed-font=… -o build/epub/<book>.epub
epubcheck build/epub/<book>.epub
```

- `templates/epub.css` styles the classed divs. Body text is Crimson; the tag groups are small Noto Sans. The backticked words and tags are `code` in HTML, and the CSS keeps them out of monospace.
- Embedded fonts (`EPUB_FONTS` in the Makefile): Crimson Roman, Italic, Bold and Bold Italic; Noto Sans Regular; Noto Sans Math. Noto Sans Math is there only for `↳` (U+21B3), which the other fonts lack. It comes straight after the main font in the table-cell font stacks, so it is used only for glyphs the main font does not have.
- `epubcheck` runs on every EPUB right after pandoc writes it. A fatal or an error fails the build and deletes the EPUB, so Make does not treat it as up to date. Warnings are printed and do not fail. `make epubcheck` checks all built EPUBs again.

## Dependencies

A book is rebuilt when its texts, metadata, About text, the stylesheet, the fonts, the scripts or `docs/style-spec.md` change. The list of a book's text files comes from its metadata. `assemble.py --deps BOOK` writes it to `build/deps/<book>.mk`, which the Makefile includes. The deps file is remade when a text folder changes, but it is replaced only if the file list has changed. So an editor's lock or backup file in a folder does not rebuild the book, but a new or removed text does.
