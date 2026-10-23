## Relevant Files

- `.gitignore` - Ignores `build/`, `sources/upstream/`, macOS junk, Python caches.
- `**/.gitkeep` - Keep the skeleton folders in git until they get content.
- `Makefile` - All build and check targets (`check-tools`, `all`, `epub`, `pdf`, `book`, `covers`, `lint`, `lint-fix`, `compare`, `index`, `dpd-check`, `fetch-sources`, `epubcheck`, `test`, `clean`). Per-book text dependencies come from `build/deps/<book>.mk` (written by `assemble.py --deps`).
- `scripts/check-tools.sh` - Checks tool presence and minimum versions, prints install hints.
- `scripts/migrate-legacy.sh` - One-off legacy migration with verification and manifest.
- `tests/test_migrate.sh` - Runs the migration into a temp dir; checks totals, re-run no-op and `--force`. Part of `make test`; skips without the legacy folder.
- `scripts/fetch-sources.sh` - Clones/updates upstream source repos at pinned commits.
- `scripts/chantlib/__init__.py` - Shared package for the Python tools.
- `scripts/chantlib/spec.py` - Reads the fenced rule blocks from `docs/style-spec.md`.
- `scripts/chantlib/parse.py` - Chant-file parser (line kinds, units, rows, member rows).
- `scripts/chantlib/text.py` - Shared normalisation helpers (NFC, ṃ→ṁ, Pāli-letter folding).
- `scripts/chantlib/books.py` - Reads `books/*/metadata.txt` (YAML-subset reader, book options, folder → book), `load_book` (validated `Book` with `Part`s), `book_files`.
- `scripts/lint.py` - Lint and safe auto-fix.
- `scripts/assemble.py` - Builds one pandoc-Markdown file per book, plus `<book>.meta.json` (with `book-id`/`cover-pdf` for the PDF) and a pandoc defaults file `<book>.pandoc.json`; `--deps` prints the book's make dependencies; `--cover-data` prints the cover JSON.
- `scripts/compare.py` - Pāli check against sources.
- `scripts/index.py` - Cross-file index, dupes, stats, rows, overlaps.
- `scripts/align.py` - Rules-based bulk alignment with a change log.
- `scripts/draft.py` - Compact draft format ↔ chant file.
- `scripts/simsapa.py` - Simsapa API client (lookup, check, gloss).
- `scripts/simsapa_fmt.py` - Copied formatter for ad-hoc `curl` queries.
- `tests/test_smoke.py` - Checks that `chantlib` imports, so `make test` runs from the start.
- `tests/` - `unittest` tests: `test_spec.py`, `test_parse.py`, `test_lint.py`, `test_assemble.py`, `test_compare.py`, `test_index.py`, `test_draft.py`, `test_simsapa.py`, `test_migrate.sh`.
- `tests/fixtures/` - Small chant files: `good.md`, `good-vinaya.md`, `good-dn22.md` (from real texts) and `bad-*.md` (one rule broken each); later, recorded Simsapa JSON responses.
- `tests/test_parse.py`, `tests/test_lint.py` - Parser, text helpers, lint checks, tag order, repeats, `--fix`.
- `tests/test_assemble.py` - Assembles fixture books from a temp `books/`/`texts/` tree: div order, TOC span, parts, metadata (incl. PDF keys, cover data), CHANGELOG/originals excluded; loads the 13 real books.
- `tests/test_pdf.py` - PDF pipeline on a fixture book in parts, in a temp typst root: Lua filter output (function calls, word tables, member rows, `toc-en`, contents placement), typst compile with no warnings, standalone cover PNG. Skips without pandoc/typst.
- `texts/**` - Migrated chant files and changelogs (content; created by migration, never edited by this feature).
- `sources/MIGRATION-MANIFEST.tsv` - Written by the migration script.
- `sources/UPSTREAM.txt` - Upstream repos, pinned commits, Chanting Guide locations.
- `sources/reference-pali-supplement.md`, `sources/suttacentral/*.json`, `sources/originals/**` - Reference texts for `compare`.
- `books/<book>/metadata.txt`, `books/<book>/about.md` - Per-book metadata and About text (13 books). `title`/`subtitle` are as displayed (FR-27); `pali-title-first` only says which of them is Pāli. About sub-headings are `{.unnumbered .unlisted}`.
- `templates/epub.css` - EPUB styling (adapted from legacy `style.css`): embedded Crimson/Noto Sans/Noto Sans Math, `instruction`/`gloss` classes, tags in small Noto Sans.
- `templates/pandoc/book.typst` - Pandoc typst template: imports `book.typ`/`cover.typ`, cover (or `cover-pdf` override), blank verso, page numbers from the About page, body.
- `templates/pandoc/chant.lua` - Lua filter: classed divs → typst function calls, unit head → `#unit-head`, tables → `#word-table`, `Code` → tags/plain text, `.toc-en` → `#toc-en`, contents page after About, cover-data path for the template.
- `templates/typst/style.typ` - Fonts (all lists end in Noto Sans Math), sizes, A5 page, running header/footer, heading styles by role (adapted from `pali-exercises`).
- `templates/typst/book.typ` - Typst functions for the unit elements, word table, tags, `toc-en`, contents page, blank page.
- `templates/typst/cover.typ` - Generated cover: `cover-page(data)` for the PDF; standalone with `--input cover-data=…` for the EPUB PNG.
- `fonts/Crimson/`, `fonts/Noto_Sans/`, `fonts/Noto_Sans_Math/` - Fonts with licence files (`Crimson/OFL.txt` and `Noto_Sans_Math/OFL.txt` added from upstream; sources in `docs/legacy-migration.md`).
- `docs/style-spec.md` - Editorial rules with machine-readable blocks.
- `docs/decisions.md` - Dated maintainer decisions.
- `docs/quality-process.md` - Checking routine.
- `docs/legacy-migration.md` - Migration sources, manifest columns, version-conflict evidence, affected-file list, legacy history, tools not migrated.
- `docs/drafting-workflow.md` - Workflow for adding a text.
- `docs/book-build.md` - Book pipeline: metadata keys, About, assembled div format, EPUB build, epubcheck, cover, PDF (Lua filter mapping, layout, font check), dependencies.
- `docs/simsapa-localhost-api-search-endpoints.md` - Existing; Simsapa API reference.
- `.claude/skills/pali-word-analysis/SKILL.md` - Local skill for grammar labels and word tables.
- `README.md` - Existing one-liner; to be extended.
- `CLAUDE.md` - New; agent instructions.

### Notes

- Tests use Python's built-in `unittest` (no install needed). Run all with `make test` (`python3 -m unittest discover -s tests`), or one file with `python3 -m unittest tests/test_lint.py`.
- Path names used below: `LEGACY=~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs`, `FINAL=$LEGACY/final-build-files/Pali-translations-formatted-md-files`, `S22=$FINAL/_build/s22src`, `BACKUP=$LEGACY/last-backup/Pali-translations-formatted-md-files`, `EXERCISES=~/prods/sites/pali-sutta-readings-project/pali-exercises`.
- The legacy `chant_pipeline.py` is **reference only**. Read its regexes and rules; write new code. Use `BACKUP/_tools/chant_pipeline.py` (904 lines), the latest version. It covers 01–10, the `options` block, `ABOUT`, `ABOUT_VINAYA`, and the 09 part titles. `S22/chant_pipeline.py` (704 lines) is an older 01–08-only copy.
- Legacy baseline (verified 2026-10-22 on a scratch copy of `BACKUP`): legacy lint gives 0 ERROR / 0 STRAY, and 4 WARN (01–08), 18 WARN (09a–09e), 0 WARN (10).
- In Makefile prerequisites, use `$(wildcard scripts/*.py scripts/chantlib/*.py)`; Make does not expand `**`.
- Never edit files under `texts/` in this feature. If lint or compare finds problems in a text, report them; don't fix them.
- Commit on `main` after each top-level task.
- Simsapa answering on 2026-10-22 during task 1 reported `app_version` 1.0.0-alpha.8, not the 1.1.0-alpha.1 noted in PRD FR-17a; re-check the response fields when recording fixtures in task 9.
- Simsapa must be running on port 4848 (or `$SIMSAPA_DIR/api-port.txt`) for task 9 and `make dpd-check`; nothing else needs it.

## Instructions for Completing Tasks

**IMPORTANT:** As you complete each task, you must check it off in this markdown file by changing `- [ ]` to `- [x]`. This helps track progress and ensures you don't skip any steps.

Example:
- `- [ ] 1.1 Read file` → `- [x] 1.1 Read file` (after completing)

Update the file after completing each sub-task, not just after completing an entire parent task.

## Tasks

### 1.0 Repo skeleton and tool check

**Specs.** Layout as in PRD FR-1. Minimum versions (FR-40): pandoc ≥ 3.1.2, typst ≥ 0.13, python3 ≥ 3.11, make, curl, git, epubcheck (required, because every EPUB is validated, PRD FR-30a); optional jq. Simsapa is reported as "available / not running", never as an error. Python tools use the standard library only.
**Depends on:** nothing.

- [x] 1.0 Repo skeleton and tool check (FR-1, FR-15, FR-23, FR-40)
  - [x] 1.1 Create the directories `texts/`, `books/`, `sources/`, `templates/epub/`, `templates/pandoc/`, `templates/typst/`, `fonts/`, `scripts/chantlib/`, `tests/fixtures/`, `docs/`, `.claude/skills/pali-word-analysis/` (add a `.gitkeep` where a folder would otherwise be empty in git). `templates/epub/` was not created: the PRD (FR-1) and task 2.5 put the stylesheet at `templates/epub.css`, so the folder would stay empty.
  - [x] 1.2 Write `.gitignore`: `build/`, `sources/upstream/`, `.DS_Store`, `._*`, `__pycache__/`, `*.pyc`.
  - [x] 1.3 Write `scripts/check-tools.sh`: for each tool, check that it is on `PATH`, parse its version, compare with the minimum, and print `OK`, `TOO OLD` or `MISSING` with an install hint:
    - Arch: `pacman -S pandoc-cli typst python make curl git`, epubcheck from the AUR (`yay -S epubcheck`) or its GitHub release jar;
    - macOS: `brew install pandoc typst python make epubcheck`;
    - Debian/Ubuntu: `apt install python3 make curl git epubcheck`, pandoc from its GitHub release `.deb` (Debian 12's 2.17 is too old), typst from its GitHub release or `cargo install --locked typst-cli`. Probe Simsapa with `curl -s --max-time 2 localhost:$PORT/health`. Exit non-zero only if a required tool is missing or too old.
  - [x] 1.4 Write the `Makefile` skeleton: `.PHONY` targets, `PYTHON ?= python3`, `BOOKS := $(notdir $(wildcard books/*))`, `check-tools`, `test` (`$(PYTHON) -m unittest discover -s tests`), `clean`; placeholder targets for the rest that print "not implemented yet".
  - [x] 1.5 Create `scripts/chantlib/__init__.py`, plus a trivial `tests/test_smoke.py` that imports `chantlib`, so `make test` runs.
  - [x] 1.6 Run `make check-tools` and `make test`; both pass on this machine.
  - [x] 1.7 Commit: "Repo skeleton, Makefile, tool check".

### 2.0 Legacy migration

**Specs.** PRD 4.2 and 4.3. Copy byte for byte. Do not trust timestamps. Expected counts: 130 texts for 01–08 from `S22` (identical to `BACKUP`), 79 texts for 09a–10 from `FINAL`, 17 changelogs (01–08 from `BACKUP`, 09a–10 from `FINAL`), 6 originals to `sources/originals/`. Manifest columns: `dest`, `snapshot`, `source`, `sha256`, `differs_from_final`, `changed_lines_vs_final`. Expected: 48 texts + 9 changelogs with `differs_from_final=yes`.
**Depends on:** 1.0.

- [x] 2.0 Legacy migration (FR-2–FR-14)
  - [x] 2.1 Write `scripts/migrate-legacy.sh` (bash, `set -euo pipefail`) with argument parsing: positional `LEGACY_DIR` (default as in Notes), `--dest DIR` (default: the repo root, found from the script's own path; used by the test), `--force`, `--dry-run`, `--help`. Resolve `FINAL`, `S22`, `BACKUP`, `EXERCISES`; fail clearly if any is missing.
  - [x] 2.2 Implement a `copy_file src dest snapshot` function that skips `._*`, `.DS_Store`, `__pycache__`, `*.pyc`. If `dest` exists and differs from `src`, refuse without `--force` (collect such files and exit non-zero at the end). Otherwise copy with `cp -p`, compute SHA-256 and the FINAL-comparison fields, and append a manifest row.
  - [x] 2.3 Implement the verification step (FR-8), run before any copy: every `S22/0[1-8]*/[0-9]*.md` must be `cmp`-identical to `BACKUP/<same>` (expect 130/130); every file in `FINAL/{07c,08,09*,10}_*/` must be identical to `BACKUP/<same>`. On a mismatch, list it and exit non-zero.
  - [x] 2.4 Implement the copy plan from FR-7. Texts `NN_*.md` for 01–08 come from `S22`, and changelogs for 01–08 from `BACKUP`. Texts and changelogs for 09a–10 come from `FINAL` into `texts/<folder>/`. `00_original_*` files go from `FINAL` to `sources/originals/<folder>/`. Copy from `BACKUP/_tools/refs/`: `reference-pali-supplement.md` → `sources/`, `dn22_root-pli-ms.json` and `dn22_variant-pli-ms.json` → `sources/suttacentral/`. **Skip** `Bhikkhu-Manual-Reference.md` and `ChantingGuide_Thanissaro.md`.
  - [x] 2.5 Copy non-content assets: `BACKUP/_tools/style.css` → `templates/epub.css`; `EXERCISES/fonts/Crimson/` and `EXERCISES/fonts/Noto_Sans/` → `fonts/`; `NotoSansMath-Regular.ttf` from `/usr/share/fonts/noto/` (or `$NOTO_MATH` if set) → `fonts/Noto_Sans_Math/`; `EXERCISES/exercises/style.typ` → `templates/typst/style.typ`; `EXERCISES/scripts/simsapa_fmt.py` → `scripts/simsapa_fmt.py`. Crimson has **no** licence file in `EXERCISES` (verified). Add `fonts/Crimson/OFL.txt` from the upstream Crimson repository (github.com/skosch/Crimson) in this sub-task, and record its source in the summary. Fetch the OFL text for Noto Sans Math, or copy `fonts/Noto_Sans/OFL.txt`, which is the same licence.
  - [x] 2.6 Write `sources/MIGRATION-MANIFEST.tsv` (header row, sorted by `dest`). For each text, compute `changed_lines_vs_final` as the count of `>` lines in `diff FINAL/<f> <chosen source>` (0 when identical).
  - [x] 2.7 Print the summary (FR-11): counts per folder, skipped files, the list of files with `differs_from_final=yes`, and expected-vs-actual totals (209 / 17 / 6). Exit non-zero if the totals don't match.
  - [x] 2.8 Write `tests/test_migrate.sh`: run the script with `--dest` set to a temporary directory and check the totals, the 48+9 `differs_from_final` rows, that a second run is a no-op, and that a modified destination makes it refuse without `--force`. Hook it into `make test`.
  - [x] 2.9 Run the script for real in the repo. Check the summary against the expected numbers.
  - [x] 2.10 Write `docs/legacy-migration.md` (FR-13, FR-14, FR-37):
    - the finding and its 6 evidence points (copy from PRD 4.3);
    - the affected-file table, generated from the manifest;
    - the reproduce commands;
    - a pointer to the S22 "Was / Now" changelog tables as the review list;
    - a short history of the legacy project (sessions S0–S22; the DN 22 and Vinaya sub-projects with their sessions S0–S8);
    - the tools that were not migrated, and why;
    - a note that the reference BM text was an EPUB→Markdown conversion, now replaced by upstream.
  - [x] 2.11 Commit: "Import legacy texts (S22 versions for 01–08) with migration manifest".

### 3.0 Upstream sources

**Specs.** PRD FR-12a. Two git repos: `https://github.com/bhikkhu-manual/bhikkhu-manual` (branch `master`, use `manuscript/markdown/`), `https://github.com/profound-labs/community-chanting-book` (branch `main`, use `chapters/english/markdown-*`). The Chanting Guide is recorded only: `https://www.dhammatalks.org/books/ChantingGuide/`, EPUB `https://www.dhammatalks.org/Archive/Writings/Ebooks/ChantingGuide210709.epub`, index `https://www.dhammatalks.org/ebook_index.html`, legacy copy `$BACKUP/_tools/refs/ChantingGuide_Thanissaro.md`. Optional local copy path: `sources/upstream/chanting-guide-thanissaro.md`.
**Depends on:** 1.0.

- [x] 3.0 Upstream sources (FR-12a)
  - [x] 3.1 Write `sources/UPSTREAM.txt` in a simple `key: value` block format, one block per source: `name`, `url`, `branch`, `commit` (git repos), `paths` (folders used), `licence`, `use`. Give the Chanting Guide block `type: location-only` and the URLs above.
  - [x] 3.2 Write `scripts/fetch-sources.sh`. For each git block: if `sources/upstream/<name>` is missing, `git clone --filter=blob:none`; then `git fetch` and `git checkout <commit>`. `--update` instead checks out the branch head and rewrites the `commit:` line in `UPSTREAM.txt`. Skip `location-only` blocks, printing their URLs.
  - [x] 3.3 Run `scripts/fetch-sources.sh --update` once to pin the current commits, then run it again without `--update` to confirm it is a no-op.
  - [x] 3.4 Add `make fetch-sources`.
  - [x] 3.5 Commit: "Record upstream sources; add fetch-sources".

### 4.0 Editorial docs

**Specs.** PRD FR-34–FR-36. Sources to read in place: `BACKUP/_tools/style-spec.md` (main), `BACKUP/_tools/dn22/style-spec.md` (§10 and `options` block), `BACKUP/_tools/vinaya/style-spec.md` (§10), `BACKUP/_tools/dn22/prd-dn22.md`, `BACKUP/_tools/vinaya/prd-vinaya.md`, both `checkpoint.md` and `operators-guide.md`, and the changelogs. The machine-readable fenced blocks must keep their info strings and contents exactly: ```` ```tags ````, ```` ```rubrics ````, ```` ```english-stopwords ````, ```` ```repeat-note ````. Book options (heading-gloss, heading-numbers, repeat-across-files, dpd-variant-rows) move to `books/<book>/metadata.txt` (task 6), not into the spec.
**Depends on:** 2.0 (for references to files in `texts/`).

- [x] 4.0 Editorial docs (FR-34–FR-36)
  - [x] 4.1 Write `docs/style-spec.md` with the 12 sections listed in FR-34. Re-state the rules in plain words, and keep every example and every dated exception. Where the main, DN 22 and Vinaya specs differ, put the general rule in the main section and the differences in §12 (book-specific rules).
  - [x] 4.2 Copy the four machine-readable blocks verbatim from `BACKUP/_tools/style-spec.md` into the right sections. Add a note at the top that `scripts/lint.py` reads them and that they must only be edited here.
  - [x] 4.3 Remove legacy-environment content that no longer applies (`_tools/cp`, `gitc`, the Mac folder, cloud builds, WeasyPrint, Gentium). Replace references to the local `dpd.db` with "DPD via Simsapa".
  - [x] 4.4 Write `docs/decisions.md`: a table (date, ID, decision, source file) of every maintainer decision found in the specs, PRDs, checkpoints and changelogs. This includes queries 1–60 where they are recorded, D1–D17 and V1–V19.
  - [x] 4.5 Write `docs/quality-process.md` (FR-36):
    - lint to 0 ERROR / 0 STRAY, with each WARN explained;
    - `compare`;
    - `simsapa.py check`;
    - grammar-label review with the skill;
    - an independent 10-unit spot check by a separate agent;
    - `index` consistency;
    - a changelog entry ("Was / Now / Why / Reference").
  - [x] 4.6 Write `scripts/chantlib/spec.py`: `load_spec(path)` returns a dict of block name → list of lines (or text for `repeat-note`). Add `tests/test_spec.py`, which loads `docs/style-spec.md` and checks that the tag list has 47 tokens (the legacy count; adjust if the count in the file differs) and that the other three blocks are present and non-empty.
  - [x] 4.7 Commit: "Editorial docs: style spec, decisions, quality process".

### 5.0 Shared parser and lint

**Specs.** The parser classifies each line into one of these kinds:
- `title` (`# …`), `subtitle` (`*…*` directly after the title)
- `heading` (`### …`; for 10 also a numbered heading followed by `gloss` `*…*`)
- `pali` (`**…**`), `literal` (`**Literal:** …`), `faithful` (`**Faithful:** …`)
- `thead`, `tsep`, `row` (`| **`w`** | … |`), `member` (`| ↳ **`w`** | … |`), `badrow`
- `repeat` (italic repeat note), `citation` (`*SC-ID*`), `rubric` (`*(…)*`)
- `instruction` (`> …`, Vinaya), `variant` (`**Variant:** … *old* → *new* …`)
- `blank`, `other` (stray)

It groups the lines into units: a Pāli line, its renderings, and its table or repeat note, plus any variants. Each row is split into word, tags (one or more groups), note, meaning and etymology. Port the regexes from the legacy `parse()`, `lint_file()`, `tag_problems()` and `coverage_problem()`.

Lint severities are ERROR, STRAY and WARN, as in the legacy script. Output: `path:line: SEVERITY message`, and the exit code is 1 if any ERROR or STRAY. Safe fixes (`--fix`): remove `---` lines, apply the synonym map (`cmpd/compound/in cmpd/in compound→comp`, `inst/ins→instr`, `ppp→pp`, `ppr→prp`, `indcl→ind`), NFC, `ṃ→ṁ` in Pāli.
**Depends on:** 2.0 (texts), 4.0 (spec blocks).

- [x] 5.0 Shared parser and lint (FR-16, success metric 3)
  - [x] 5.1 Write `scripts/chantlib/text.py`: `nfc()`, `fold_niggahita()` (ṃ→ṁ), `pali_letters_only()` (lower case, keep Pāli letters and spaces, drop punctuation and `'`), `norm_line()` for comparisons.
  - [x] 5.2 Write `scripts/chantlib/parse.py`: `classify(lines)`, then `parse_file(path)` returning a `ChantFile` with `title`, `subtitle`, `units[]` (each with `pali`, `literal`, `faithful`, `rows[]`, `members` per row, `repeat`, `variants[]`, `citation`, line numbers) and `stray[]`. Add `split_row()` and `split_tags()`.
  - [x] 5.3 Add `tests/fixtures/good.md`, `good-vinaya.md` and `good-dn22.md` (small hand-made examples copied from real texts), and `bad-*.md` cases (unknown tag, wrong tag order, missing coverage, `comp` row without members, English stray line, ṃ, `---`, missing two trailing spaces). Write `tests/test_parse.py`.
  - [x] 5.4 Write `scripts/lint.py`: CLI `lint.py [--fix] [--book BOOK] PATHS…`. Load the spec via `chantlib.spec`, and book options via `chantlib.books` (a stub returning defaults until task 6). Implement the checks: layout, allowed tags and canonical order, coverage, `comp` members, repeat note and repeats (within a file, or across files when the book option is set), rubrics, English stopwords in Pāli/headings, characters (NFC, ṁ, alphabet, no tabs/NBSP/tone marks), Vinaya instruction-line length (> 45 words → WARN), and variant cue checks.
  - [x] 5.5 Implement `--fix` for the safe fixes only. Write in place, and print one "safe fixes applied" line per changed file.
  - [x] 5.6 Write `tests/test_lint.py`: each bad fixture gives the expected severity; good fixtures are clean; `--fix` on a temp copy gives the expected text.
  - [x] 5.7 Add `make lint` (all `texts/*/[0-9]*.md`) and `make lint-fix`.
  - [x] 5.8 Run `make lint` on the migrated texts. The target is the legacy baseline from Notes: 0 ERROR / 0 STRAY, with 4 / 18 / 0 WARN for 01–08 / 09 / 10. Compare the WARN messages with the legacy linter's output (run it on a scratch copy of `BACKUP` with each spec). Differences are most likely lint bugs, so fix the lint code. Only if a real text problem is found, list it in `docs/legacy-migration.md` under "Open lint findings" without editing the text. Do **not** run `lint-fix` on `texts/` in this feature. Result: 0 ERROR / 0 STRAY / 23 WARN. The 22 legacy WARNs are reproduced exactly (same lines and messages); the 23rd comes from a new check (variant cue without two trailing spaces, 09e/05:67) and is listed under "Open lint findings" in `docs/legacy-migration.md`.
  - [x] 5.9 Commit: "Chant parser and lint".

### 6.0 Book metadata and EPUB build

**Specs.** `metadata.txt` is YAML-compatible (pandoc `--metadata-file`). Keys:
- `title`, `subtitle`, `lang: en-GB`, `pali-title-first`
- `texts` (list of folders; for book 09, a list of `{folder, heading}` parts)
- `sources`, `rights`
- `cover-image` (empty = generated), `about`
- `author: ""`, `publisher: ""`
- `series-line`, optional `accent`
- optional `options` (`heading-gloss`, `heading-numbers`, `repeat-across-files`, `dpd-variant-rows`; for book 10)

Titles are in PRD FR-27. Book IDs: `01_morning_chanting`, `02_evening_chanting`, `03_reflections`, `04a_parittas`, `04b_verses_on_the_dhamma`, `05_anumodanas`, `06_funeral_chants`, `07a_suttas`, `07b_anagatabhaya_suttas`, `07c_bhikkhuaparihaniyadhamma`, `08_patimokkha_chants`, `09_vinaya_formulae`, `10_mahasatipatthanasutta`.

The assembled Markdown follows legacy `preprocess()`, with these divs: `unit`, `pali` (`lang="pi"`), `literal`, `faithful`, `repeat`, `citation`, `rubric`, `subtitle`, `instruction`, `variant`, `gloss`. The TOC entry gets `[— English]{.toc-en}`; the About file gets `{.unnumbered}`. Fonts are embedded with `--epub-embed-font`. `↳` falls back to Noto Sans Math via CSS `font-family`.
**Depends on:** 5.0 (parser), 2.0 (fonts, css).

- [x] 6.0 Book metadata and EPUB build (FR-26–FR-30, FR-32 EPUB part)
  - [x] 6.1 Create `books/<id>/metadata.txt` for the 13 books (book 10's file already exists with `texts` and `options`; extend it), with the FR-27 titles, `pali-title-first: true` for 04a and 05, the `sources` and `rights` text from FR-26, and empty `author`/`publisher`. For 09, list the five parts with their headings from `BACKUP/_tools/chant_pipeline.py` `BOOKS`: Requisites, Rains and Kaṭhina, Other Procedures, Offences, Uposatha. For 10, add `options` from the legacy DN 22 spec's `options` block.
  - [x] 6.2 Create `books/<id>/about.md` for the 13 books. For 01–08, use the legacy `ABOUT` template with `{what}`, `{drafting}` and `{review}` filled in as `build()` did. For 10, use `BACKUP/_tools/dn22/about-dn22.md`. For 09, use `ABOUT_VINAYA` from `BACKUP/_tools/chant_pipeline.py` (line ~591). Leave `{today}` as a placeholder.
  - [x] 6.3 Write `scripts/chantlib/books.py`: `load_book(id)`, which parses the metadata with a small YAML-subset reader (keys, strings, booleans, lists, list of mappings) and validates the required keys; `list_books()`; `book_files(book)`, which gives the ordered `NN_*.md` paths and never returns `CHANGELOG.md` or `00_original_*`. Wire book options into `lint.py`.
  - [x] 6.4 Write `scripts/assemble.py BOOK [--out build/tmp]`. Steps: read the metadata, insert `about.md` with `{today}` replaced, emit part headings for 09, run each file through the parser, and emit pandoc Markdown with the classed divs. Write `build/tmp/<book>.md` and `build/tmp/<book>.meta.json` (metadata with the computed title/subtitle order and the cover path; **keys with empty values dropped**, because pandoc would otherwise write empty `dc:creator`/`dc:publisher` elements). Warn on lint ERROR/STRAY (FR-25).
  - [x] 6.5 Adapt `templates/epub.css`: `@font-face` for Crimson and Noto Sans; Noto Sans Math listed last in the table-cell font stack; the legacy class styles; `.toc-en` hidden in headings; keep the legacy `code { font-family: inherit; font-size: 1em; background: none; }`, so the backticked words and tags are not shown in monospace.
  - [x] 6.6 Add Makefile rules: `build/epub/%.epub` depends on `books/%/*`, the book's texts, `templates/epub.css`, `fonts/**`, `scripts/**` and the cover PNG (until task 7, build without a cover if the PNG is missing). It runs `assemble.py` and then `pandoc -f markdown+fenced_divs --metadata-file build/tmp/<book>.meta.json --toc --toc-depth=1 --split-level=1 --css templates/epub.css --epub-embed-font=… [--epub-cover-image=…] -o $@`, then `epubcheck $@`; on a fatal or error, delete `$@` and fail (PRD FR-30a). Add `make epub`, `make book BOOK=…` (EPUB part) and `make epubcheck` (re-validates every `build/epub/*.epub`). The local `epubcheck` wrapper passes only its first argument, so the rules call it with the file alone (no `-q`).
  - [x] 6.7 Write `tests/test_assemble.py`: assemble a fixture book (a test `books/` folder passed by env var or argument), and check the div order, the TOC span and that `CHANGELOG.md` is excluded.
  - [x] 6.8 Run `make epub`; all 13 EPUBs build. Unzip one and check the OPF metadata (title, language, rights, empty creator/publisher). Run `make epubcheck`: 0 fatals and 0 errors on all 13; list any warnings. Open one in an e-reader and ask the maintainer to check `↳`, tables and the TOC. Result: 13/13 built; epubcheck 0 fatals / 0 errors / 0 warnings on all 13. OPF: typed main title + subtitle, `en-GB`, `dc:rights`, `dc:source`, no `dc:creator`/`dc:publisher`. Book 10 opened in calibre's `ebook-viewer` for the maintainer's check.
  - [x] 6.9 Commit: "Book metadata and EPUB build".

### 7.0 Typst PDF build and generated covers

**Specs.** Pandoc `-t typst --template templates/pandoc/book.typst --lua-filter templates/pandoc/chant.lua`. The Lua filter turns each classed Div into raw typst `#unit[…]`, `#pali[…]`, `#literal[…]`, `#faithful[…]`, `#repeat-note[…]`, `#citation[…]`, `#rubric[…]`, `#instruction[…]`, `#variant[…]`, `#gloss[…]`. Tables become `#word-table(...)` with `table.header(...)`, so the header repeats across pages. Member rows (cell starting `↳`) get an indent style.

Page: A5. Body Crimson; tables and labels Noto Sans; fallback lists end in `"Noto Sans Math"`. The Pāli line and renderings are kept with the start of the table (`block(sticky: true)` or `breakable: false` on the heading part). Running header: book title / current chant title. Page numbers. Contents: Pāli title — English title.

The cover reads `sys.inputs` (`title`, `subtitle`, `series`, `accent`). The PDF is the cover page + blank verso + About + contents + texts. EPUB cover: `typst compile --format png --ppi 300 cover.typ build/covers/<book>.png`. Build with `typst compile --font-path fonts/ --ignore-system-fonts`, so the result does not depend on system fonts.
**Depends on:** 6.0.

- [x] 7.0 Typst PDF build and generated covers (FR-31–FR-33a)
  - [x] 7.1 Adapt `templates/typst/style.typ`: keep the fonts, sizes, page and heading structure; set paper `"a5"` and suitable margins; fonts Crimson (body), Noto Sans (tables), with Noto Sans Math as the last fallback; remove the language-strings, answer-key and disclaimer parts.
  - [x] 7.2 Write `templates/typst/book.typ`: the functions listed in Specs, the word-table function (two columns: auto-sized Word, wrapping Analysis; smaller Noto Sans for tags; member-row indent), the running header from the current level-1 heading, the TOC, and the About page as unnumbered.
  - [x] 7.3 Write `templates/pandoc/book.typst` (based on `pandoc -D typst`): import `style.typ` and `book.typ`, place the cover, a blank verso, the About, the contents and `$body$`; set the document title and language from metadata.
  - [x] 7.4 Write `templates/pandoc/chant.lua`. Pandoc's plain typst output (verified) turns every div into an unclassed `#block[…]`, wraps tables in `#figure(align(center)[#table(…)], kind: table)`, and writes `` `word` ``/`` `(tags)` `` as monospace raw text. The filter must:
    - map the Div classes to raw typst calls;
    - turn each Table into a `#word-table(...)` call (no figure);
    - turn `Code` inlines into styled content (word cells: bold Crimson; tag groups: small Noto Sans);
    - keep `lang="pi"` (typst accepts `lang: "pi"`, verified). Test it on one assembled book with `pandoc … -t typst -o build/tmp/<book>.typ` and inspect the output.
  - [x] 7.5 Write `templates/typst/cover.typ`: a simple typographic A5 cover (title, subtitle, series line, rule or ornament, optional accent colour), taking its inputs from `sys.inputs`.
  - [x] 7.6 Add Makefile rules: `build/covers/%.png` (cover PNG from metadata via `--input`), `build/pdf/%.pdf` (assemble → pandoc → `typst compile --font-path fonts --ignore-system-fonts --root .`), `make covers`, `make pdf`, `make all`, and the PDF part of `make book`. Make the EPUB rule depend on the cover PNG.
  - [x] 7.7 Run `make all`; all 13 EPUBs and 13 PDFs build. Check for typst "unknown font" or missing-glyph warnings (there must be none for `↳`, √, ṁ, ṭ, ḷ). Result: 13 + 13 built, no typst warnings, epubcheck 0/0/0 on all 13; a second `make all` does nothing. `pdffonts` lists only Crimson, Noto Sans and Noto Sans Math in every PDF (no fallback to typst's built-in fonts). A charset check found every character of the assembled books in Crimson or Noto Sans Math; only `↳` and the cover's `◆` come from Noto Sans Math.
  - [x] 7.8 Visually compare the 01, 07a and 10 PDFs with `$FINAL/_build/*.pdf`: same content in the same order, nothing split badly at page breaks, headers repeat. Open them for the maintainer to check by hand (launch the viewer only). Result: Literal, Faithful, `↳`, √ and repeat-note counts are identical in the old and new text of all three (01: 112/112/191/349/0; 07a: 1028/1028/1495/3276/203; 10: 567/567/1016/1882/227), and the Literal lines come in the same order. The only difference is 4 opening quotes in 07a (source `'This …`), which typst sets as ‘ and the legacy PDF as ’. The new PDFs have about half the legacy page count (auto-width Word column, A5 margins and type sizes). Opened for the maintainer.
  - [x] 7.9 Commit: "Typst PDF build and generated covers".

### 8.0 Consistency and authoring tools

**Specs.** `compare.py FILES --ref SOURCE` takes the Pāli lines of each file (variant cues excluded, `(×3)` and rubrics stripped), normalises them with `text.norm_line`, and diffs them against the reference stream. Reference readers:
- BM upstream Markdown (`sources/upstream/bhikkhu-manual/manuscript/markdown/chants/*.md` and `vinaya/`), with markup stripped: headings, emphasis, footnotes, include directives, HTML, leader brackets;
- `reference-pali-supplement.md` (segment lines `[id] text`);
- SC bilara JSON;
- Vinaya `sources/originals/…`;
- the optional Chanting Guide copy, skipped with a report line if absent.

Map each folder or file to its reference source by a small table in `compare.py`; the legacy `compare` arguments show which source each folder used.

`index.py` has these subcommands:
- `index [--folder X]`: same word with different etymology (E lines) or tags (T lines);
- `dupes`;
- `stats`;
- `rows WORD…`: the two commonest existing rows;
- `overlaps FILES`: Pāli lines equal to a line in another folder.

`align.py TREE RULES.json LOG.json` uses the legacy rules format (`word` regex, `old`, `new`, `why`, `ref`).

`draft.py build DRAFT OUT.md` / `extract FILE.md` uses the compact format: `T|` title, `E|` English title, `U|` rubric, `H|` heading, `P|` Pāli (`P!` force full table, `P~` force repeat note), `L|` literal, `F|` faithful, `R|` row, `M|` member row, `C|` citation, `S|` instruction, `V|` variant, `I|` copy a settled unit. Read `BACKUP/_tools/helpers/b.py` and `md2c.py` for the exact syntax.
**Depends on:** 5.0, 3.0.

- [ ] 8.0 Consistency and authoring tools (FR-12b, FR-16)
  - [ ] 8.1 Write `scripts/compare.py`, with the reference readers and the folder→source table. BM upstream chant files hold several chants each: drop the `**Contents**` link list, `<a id>` anchors and the "(English)" sections; remove line-end `\` and `[…]` leader brackets. The report shows, per file, the differences with context (40 characters). Exit 1 if there are differences.
  - [ ] 8.2 Write `tests/test_compare.py`, with small reference fixtures (one BM-style Markdown, one SC JSON snippet).
  - [ ] 8.3 Add `make compare` (requires `sources/upstream/`; print a hint to run `make fetch-sources` if it is missing).
  - [ ] 8.4 Run `make compare` on 01–09 and 10. Sort the differences into: (a) expected (filled `…pe…` elisions, leader brackets, logged misprint fixes, variants); (b) artefacts of the old EPUB→Markdown reference; (c) unexplained. Record (b) and (c) in `docs/legacy-migration.md` (FR-12b). Do not change texts.
  - [ ] 8.5 Write `scripts/index.py` with the five subcommands; `tests/test_index.py`; `make index`.
  - [ ] 8.6 Write `scripts/align.py`, plus a test on a fixture tree.
  - [ ] 8.7 Write `scripts/draft.py` (`build` and `extract`). `tests/test_draft.py` round-trips the fixtures: `extract` then `build` gives a file identical to the original.
  - [ ] 8.8 Commit: "Compare, index, align and draft tools".

### 9.0 Simsapa client and word-analysis skill

**Specs.** PRD FR-17–FR-22 and FR-20a. Port: `$SIMSAPA_DIR/api-port.txt` or 4848. Routes and fields as in FR-17a:
- `/health`;
- `POST /dict_combined_search`: `results[].uid/title/table_name/snippet`, `deconstructor`; skip `bold_definitions`;
- `GET /word.json?uid=`: `lemma_1`, `pos`, `grammar`, `construction`, `root_key`, `stem`, `pattern`, `meaning_1/2`, `meaning_lit`, `inflections`, `inflections_html`;
- `POST /gloss_text`: `words_data[]` with `original_word`, `stem`, `direct_uids`, `results[]`, `deconstructions[]`.

Use `urllib.request`. Scripts do **not** assign grammar labels and do **not** split compounds by their own rules.
**Depends on:** 5.0 (parser, for `check`), 8.0 (`index.py rows`, used by the skill; `draft.py` format, used by `gloss`).

- [ ] 9.0 Simsapa client and word-analysis skill (FR-17–FR-22, FR-20a)
  - [ ] 9.1 Record fixture responses from the running Simsapa into `tests/fixtures/simsapa/`: `/health`; `dict_combined_search` for `bhagavantaṁ`, `sammāsambuddho` and one deconstructor-only form (e.g. `atthaññe`); `word.json` for `49139/dpd`, `49140/dpd` and `60847/dpd`; `gloss_text` for `Yo so tathāgato arahaṁ sammāsambuddho` and for `Vijjācaraṇa-sampanno sabb'ītiyo bhavatv-antarāyo` (hyphen and apostrophe cases).
  - [ ] 9.2 Write the `scripts/simsapa.py` client core: port discovery, a `get/post` with timeout, a clear "Simsapa is not running…" error, and a switch to read responses from a fixture directory (`SIMSAPA_FIXTURES`) for tests.
  - [ ] 9.3 Implement `lookup WORD… [--json] [--inflections]` (FR-18). Plain-text output: one block per headword with `lemma_1`, `pos`, `grammar`, `construction` lines, `root_key`, meaning, then the deconstructor split. With `--inflections`, also print `inflections_html` as plain text (rows and cells, no parsing into labels).
  - [ ] 9.4 Implement `check FILES…` (FR-19): for each row, check that the word is found (the form appears in some headword's `inflections`, or a deconstructor split exists), the root, the etymology against the `construction` lines, and `comp` members against DPD `construction` or the deconstructor. Apply the spec's exceptions. Output `path:line: FLAG word — reason (DPD: …)`. Cache lookups on disk in `build/cache/simsapa/`, keyed by Simsapa `app_version` (about 7,500 distinct row words at about 50 ms per search). Use the search `snippet` first (pos, meaning, construction) and call `/word.json` only when `root_key` or the full `construction` is needed. Look up row words with `'` removed.
  - [ ] 9.5 Implement `gloss FILE|--text TEXT` (FR-20). First join apostrophe words (`sabb'ītiyo` → `sabbītiyo`), because `/gloss_text` splits at `'` (verified: *sabbi* + *tiyo*), and map results back to the original spelling. Then: print draft rows in `draft.py` format with an empty tag slot `()`, all candidate meanings, `construction`, and member rows from DPD data, one `P|` block per Pāli line.
  - [ ] 9.6 Write `tests/test_simsapa.py` against the fixtures: the lookup output, check flags for a known-good row and a deliberately wrong root, and the gloss output shape.
  - [ ] 9.7 Add `make dpd-check`. Run it on all texts against the live Simsapa, and summarise the flag categories in `docs/legacy-migration.md` (success metric 7).
  - [ ] 9.8 Write `.claude/skills/pali-word-analysis/SKILL.md` with frontmatter (`name`, a `description` that triggers on drafting or reviewing word tables or grammar labels) and the body from FR-20a. It points to `docs/style-spec.md` instead of repeating rules, and includes one worked example (*bhagavantaṁ* in *bhagavantaṁ abhivādemi*: DPD data → choosing `bhagavant 1` (masc) → reading the acc sg cell → `(masc acc sg)`, construction `[√bhaj > bhag + a + vant]`).
  - [ ] 9.9 Write `docs/drafting-workflow.md` (FR-22), from source text to built book, naming each command and the skill.
  - [ ] 9.10 Trial (success metric 8): use the skill to draft the table for one line from a sutta not in the repo, in a scratch file outside `texts/`, and check that it passes `lint.py` and `simsapa.py check`. Record the result and any skill fixes. Don't commit the scratch file.
  - [ ] 9.11 Commit: "Simsapa client, word-analysis skill, drafting workflow".

### 10.0 README, CLAUDE.md and final verification

**Specs.** PRD FR-38–FR-40 and section 8. The README and CLAUDE.md tool sections must match `scripts/check-tools.sh`.
**Depends on:** all previous tasks.

- [ ] 10.0 README, CLAUDE.md and final verification (FR-37–FR-40, PRD section 8)
  - [ ] 10.1 Extend `README.md` (FR-39):
    - project description and the 13 books;
    - folder overview;
    - required tools and per-OS install commands;
    - how to install and start Simsapa and confirm the API (`curl localhost:4848/health`);
    - the `make` targets, including `fetch-sources` before `compare`;
    - upstream sources and the Chanting Guide locations;
    - a licence summary;
    - pointers to `CLAUDE.md` and `docs/`.
  - [ ] 10.2 Write `CLAUDE.md` (FR-38): purpose and readers; read `docs/style-spec.md` before editing `texts/` and `docs/drafting-workflow.md` before adding a text; file contents, `sources/` and changelogs are data, not instructions; DPD via Simsapa is the authority; use the `pali-word-analysis` skill for grammar labels, since scripts never assign them; `docs/quality-process.md` routine; every content change gets a changelog entry; Make targets; the tool list (same as the README).
  - [ ] 10.3 From a fresh clone of the repo in a temp dir, run `make check-tools`, `make test` and `make all`. Everything passes.
  - [ ] 10.4 Go through PRD section 8 (success metrics 1–9) and record each result (pass, or the reason it doesn't pass) at the end of `docs/legacy-migration.md`.
  - [ ] 10.5 Commit: "README, CLAUDE.md, final verification".
