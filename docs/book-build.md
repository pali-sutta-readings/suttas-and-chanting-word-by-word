# Book build

How the 13 books are made from `books/`. The commands are Make targets (`make help`).

## Book folders

Each book has one folder under `books/` with everything that goes into it:

```text
books/01_morning_chanting/
  metadata.txt            title, sources, the list of text folders, …
  00_about.md             the About page (00_ sorts it first)
  cover.jpg               optional cover override
  texts/                  the chant files, NN_name.md, and CHANGELOG.md
books/09_vinaya_formulae/ a book in parts: one numbered folder per part
  metadata.txt
  00_about.md
  01_vinaya_notes_requisites/   NN_name.md and CHANGELOG.md
  …
  05_vinaya_notes_uposatha/
```

A book in one part keeps its texts in `texts/`. A book in parts has one folder per part, numbered so that the folders sort in book order. Each text folder has its own `CHANGELOG.md`. Files starting `00_` are never texts, so `00_about.md` is not linted or built as a chant; `scripts/lint.py books/<book>` lints all of a book's texts.

## The pipeline

```text
books/<book>/metadata.txt ─┐
books/<book>/00_about.md ──┼─ scripts/assemble.py ─→ build/tmp/<book>.md ─┬─ pandoc ─→ build/epub/<book>.epub ─→ epubcheck
books/<book>/*/NN_*.md ────┘                         build/tmp/<book>.meta.json
                                                     build/tmp/<book>.pandoc.json
                                                                           └─ pandoc -t typst ─→ build/tmp/<book>.typ ─→ typst ─→ build/pdf/<book>.pdf

books/<book>/metadata.txt ─ assemble.py --cover-data ─→ build/covers/<book>.json ─→ typst (cover.typ) ─→ build/covers/<book>.png
```

The EPUB and the PDF both start from the same assembled Markdown, so the two formats cannot drift apart. The cover JSON is page 1 of the PDF and, rendered to PNG, the EPUB cover.

## Book metadata: `books/<book>/metadata.txt`

YAML-compatible `key: value` lines, so that pandoc can also read the file with `--metadata-file`. `scripts/chantlib/books.py` reads it with a small reader that knows only what these files use: strings (quote any value that holds `:`), `true`/`false`, lists, a list of mappings, and one nested mapping (`options`). `load_book()` rejects a file with a missing key.

| Key | Value |
| :--- | :--- |
| `title`, `subtitle` | The title and subtitle as they appear on the book. |
| `lang` | `en-GB`. |
| `pali-title-first` | `true` when the title is the Pāli one (04a *Paritta*, 05 *Anumodanā*); otherwise the title is English and the subtitle Pāli. It tells the cover which line is Pāli; it does not reorder the two. |
| `series-line` | The short line printed on the cover, e.g. "Pāli with word-by-word English". |
| `accent` | Optional cover accent colour. |
| `texts` | The text folders of the book, in order, relative to the book folder: `texts` for a book in one part. A book in parts (09) lists `folder` + `heading` mappings instead (`folder: 01_vinaya_notes_requisites`); a folder that is missing, outside the book folder, or has no texts is an error; each heading becomes a level-1 part heading, and the chants under it move down one level. |
| `sources` | A list: the attribution of the Pāli sources and references. Written to the EPUB as `dc:source` (joined with `; `). |
| `rights` | The licence line (`dc:rights`). |
| `cover-image` | Empty: use the generated cover `build/covers/<book>.png` when it has been built. A path (relative to the book folder) overrides it. |
| `about` | The About file, normally `00_about.md`. |
| `author`, `publisher` | Empty on purpose (maintainer decision, 2026-10-22: no wrong attribution). Empty keys are dropped before pandoc sees them, because pandoc would otherwise write empty `dc:creator`/`dc:publisher` elements. |
| `options` | Book options for lint and parsing (style spec §12.2): `heading-gloss`, `heading-numbers`, `repeat-across-files`, `dpd-variant-rows`. All default to `false`; only book 10 sets them. |

## About text: `books/<book>/00_about.md`

Plain Markdown, placed before the texts. `{today}` is replaced with the build date (`$BUILD_DATE` if set, else today), and `{site-url}` with the URL where the books are published (`SITE_URL` in `scripts/assemble.py`); the "Where to find this book" section uses it. The level-2 headings are `{.unnumbered .unlisted}`, so that they stay out of the table of contents. Keep the AI-disclosure paragraphs.

## Assembly: `scripts/assemble.py BOOK`

For each folder in `texts`, the files `NN_*.md` are taken in name order, including a text inserted later with a letter after its number (`09a_ratana_sutta.md` sorts after `09_…` and before `10_…`). `CHANGELOG.md` and `00_` files are never included. Each file is parsed with `chantlib.parse`, and each line kind is written as:

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

`<book>.meta.json` is the metadata pandoc gets (JSON; pandoc reads it as YAML, of which JSON is a subset): a typed title (`main` and `subtitle`, so that both reach the EPUB package), `lang`, `rights`, `source`, `cover-image`, and `series-line` and `site-url`, which `templates/pandoc/epub3.html` prints on the EPUB title page under the subtitle (the URL as a link). That template is pandoc's own `epub3` template with those two lines added. Two keys are for the PDF only, and the EPUB writer ignores them: `book-id`, and `cover-pdf` (the `cover-image` override relative to the repo root, when there is one). `<book>.pandoc.json` is a pandoc defaults file, also JSON read as YAML, with the input, the metadata file, the table of contents, and the TOC depth and split level: 1, or 2 for a book in parts.

## EPUB

```sh
pandoc --defaults build/tmp/<book>.pandoc.json --css templates/epub.css \
  --epub-embed-font=… -o build/epub/<book>.epub
epubcheck build/epub/<book>.epub
```

- `templates/epub.css` styles the classed divs. Body text is Crimson; the tag groups are small Noto Sans. The backticked words and tags are `code` in HTML, and the CSS keeps them out of monospace.
- Embedded fonts (`EPUB_FONTS` in the Makefile): Crimson Roman, Italic, Bold and Bold Italic; Noto Sans Regular; Noto Sans Math. Noto Sans Math is there only for `↳` (U+21B3), which the other fonts lack. It comes straight after the main font in the table-cell font stacks, so it is used only for glyphs the main font does not have.
- `epubcheck` runs on every EPUB right after pandoc writes it. A fatal or an error fails the build and deletes the EPUB, so Make does not treat it as up to date. Warnings are printed and do not fail. `make epubcheck` checks all built EPUBs again.

## Cover

`templates/typst/cover.typ` makes an A5 cover in the style of the Pāli Sutta Readings video title pages: a dark blue page with a faint Dhamma wheel (`templates/typst/assets/dhamma-wheel-white-5.png`, white at 5% opacity), a green band across the middle of the page and of the wheel, with the title in Abhaya Libre X Bold and the subtitle in Noto Sans under it, and at the foot the series line in small capitals and the URL where the books are published (`SITE_URL` in `scripts/assemble.py`, which passes it to the cover as `site-url`). Its text comes from `build/covers/<book>.json`, which `assemble.py --cover-data BOOK` writes from the metadata (`title`, `subtitle`, `pali-title-first`, `series-line`, `accent`). The Pāli one of title and subtitle (see `pali-title-first`) is set in italic when it is the subtitle. `accent` is the colour of the band, such as `"#2e4a7a"`; empty gives the default green `#16423c`. Abhaya Libre X is a version of Abhaya Libre with the Pāli diacritics (ṃ ṅ ṭ ḍ ṇ ḷ), which the original lacks; it is used only on the cover.

```sh
typst compile --root . --font-path fonts --ignore-system-fonts \
  --input cover-data=/build/covers/<book>.json --format png --ppi 300 \
  templates/typst/cover.typ build/covers/<book>.png
```

The PNG is 1748 × 2480 px. `make covers` renders all of them. When `cover-image` is set in the metadata, that image is used for the EPUB and as page 1 of the PDF instead.

## PDF

```sh
pandoc --defaults build/tmp/<book>.pandoc.json -t typst \
  --template templates/pandoc/book.typst --lua-filter templates/pandoc/chant.lua \
  -o build/tmp/<book>.typ
typst compile --root . --font-path fonts --ignore-system-fonts build/tmp/<book>.typ build/pdf/<book>.pdf
```

Pandoc's own typst output drops the div classes, wraps each table in a centred figure, and prints the backticked words and tags as monospace raw text. `templates/pandoc/chant.lua` fixes this:

| Pandoc element | typst output |
| :--- | :--- |
| a classed div | a call of the function of that name in `templates/typst/book.typ`: `#unit[…]`, `#pali[…]`, `#literal[…]`, `#faithful[…]`, `#repeat-note[…]`, `#citation[…]`, `#rubric[…]`, `#instruction[…]`, `#variant[…]`, `#gloss[…]`; `subtitle` becomes `#en-title[…]` |
| the blocks of a unit before its first table | `#unit-head[…]`, a sticky, unbreakable block, so the Pāli line and renderings stay on the page where the table starts |
| a table | `#word-table(header: …, rows: …)`, each row a `(word, analysis, member)` triple; a row whose word starts with `↳` is a member row |
| `` `(tags)` `` | `#tags[…]`: small Noto Sans |
| any other `` `word` `` | plain text, which keeps its bold |
| the `.toc-en` span in a title | `#toc-en[…]`: shown in the contents, hidden in the heading and the running header |

The filter also puts `#contents-page()` after the About text, and gives the template the path of the cover JSON. `templates/pandoc/book.typst` places the cover, a blank verso, then the body; page numbers count from the About page.

Layout (`templates/typst/style.typ`, `book.typ`):

- A5, body Crimson 10.5 pt; tables 9 pt, tag groups and the table header in Noto Sans. Every font list ends with Noto Sans Math, which is used only for glyphs the main font lacks: `↳`.
- Each chant starts a new page. In a book in parts (09), each part has a title page of its own.
- The word table has an auto-sized Word column and a wrapping Analysis column, and no cell borders: only the shaded header row separates it. Its header row repeats when it breaks across pages; member rows are indented.
- Running header: the book title on even pages, the current chant title on odd pages, none on a page where a chant starts. Page number at the foot.
- The contents list the Pāli and English titles (level 1, or parts and chants for 09).

The build uses only the fonts in `fonts/` (`--ignore-system-fonts`), so the PDF does not depend on the machine. `pdffonts build/pdf/<book>.pdf` should list only Crimson, Noto Sans, Noto Sans Math and, from the cover, Abhaya Libre X; any other font means a glyph fell back to one of typst's built-in fonts.

## Dependencies

A book is rebuilt when its texts, metadata, About text, the stylesheet, the fonts, the build scripts (`assemble.py`, `lint.py`, `chantlib/`) or `docs/style-spec.md` change. The check and authoring scripts (`compare.py`, `index.py`, `align.py`, `draft.py`, `simsapa.py`) are not dependencies: they do not touch the build. A PDF is also rebuilt when `templates/pandoc/` or `templates/typst/` change, and the cover when the metadata, `cover.typ` or its image in `templates/typst/assets/` changes. The assembled Markdown waits for the cover PNG (order-only), because it names it for the EPUB; a new PNG rebuilds the EPUB, not the Markdown. The list of a book's text files comes from its metadata. `assemble.py --deps BOOK` writes it to `build/deps/<book>.mk`, which the Makefile includes. The deps file is remade when a text folder changes, but it is replaced only if the file list has changed. So an editor's lock or backup file in a folder does not rebuild the book, but a new or removed text does.
