## Relevant Files

- `.gitignore` - Ignores `build/`, `sources/upstream/`, macOS junk, Python caches.
- `**/.gitkeep` - Keep the skeleton folders in git until they get content.
- `Makefile` - All build and check targets (`check-tools`, `all`, `epub`, `pdf`, `book`, `covers`, `lint`, `lint-fix`, `compare`, `index`, `dpd-check`, `fetch-sources`, `epubcheck`, `test`, `clean`). Per-book text dependencies come from `build/deps/<book>.mk` (written by `assemble.py --deps`).
- `scripts/check-tools.sh` - Checks tool presence and minimum versions, prints install hints.
- `scripts/migrate-legacy.sh` - One-time legacy migration with verification and manifest. Ran once (2026-10-22); kept as a record, not maintained.
- `scripts/fetch-sources.sh` - Clones/updates upstream source repos at pinned commits.
- `scripts/chantlib/__init__.py` - Shared package for the Python tools.
- `scripts/chantlib/spec.py` - Reads the fenced rule blocks from `docs/style-spec.md`.
- `scripts/chantlib/parse.py` - Chant-file parser (line kinds, units, rows, member rows).
- `scripts/chantlib/text.py` - Shared normalisation helpers (NFC, ṃ→ṁ, Pāli-letter folding).
- `scripts/chantlib/books.py` - Reads `books/*/metadata.txt` (YAML-subset reader, book options, `book_for_text` from a file's path), `load_book` (validated `Book` with `Part`s), `book_files` (text folders resolved inside the book folder; `NN*.md`, so `NNa_` texts are included).
- `scripts/lint.py` - Lint and safe auto-fix.
- `scripts/assemble.py` - Builds one pandoc-Markdown file per book, plus `<book>.meta.json` (with `book-id`/`cover-pdf` for the PDF) and a pandoc defaults file `<book>.pandoc.json`; `--deps` prints the book's make dependencies; `--cover-data` prints the cover JSON.
- `scripts/compare.py` - `extract` (normalised Pāli stream of a text or a mapped reference passage) and `diff` (report over `sources/ref-map.tsv`; `diff` and `contain` modes; keys `anchor`, `anchor..end`, `seg..seg`, Chanting Guide `Start..End` headings).
- `scripts/index.py` - Cross-file index (etymology and word-class tag conflicts; `--all-tags`), dupes, stats, rows, overlaps.
- `scripts/align.py` - Rules-based bulk alignment, cell-scoped, whole-cell match by default (substring rules skip cells already aligned), dry run by default, with a change log and `--changelog` Was/Now tables.
- `scripts/draft.py` - Compact draft format ↔ chant file (`I|` by Pāli-line key; `T0|` for a table header without rows); `extract` refuses a file whose layout would not round-trip.
- `scripts/simsapa.py` - Simsapa API client on the exact routes (`/lookup_forms`, exact `/gloss_text`): lookup; check with flags and candidates; gloss as candidate data.
- `scripts/simsapa_fmt.py` - Copied formatter for ad-hoc `curl` queries.
- `tests/test_smoke.py` - Checks that `chantlib` imports, so `make test` runs from the start.
- `tests/` - `unittest` tests: `test_spec.py`, `test_parse.py`, `test_lint.py`, `test_assemble.py`, `test_compare.py`, `test_index.py`, `test_align.py`, `test_draft.py`, `test_simsapa.py`.
- `tests/fixtures/compare/` - BM-style Markdown (Contents, anchors, divs, link line, italic table cells, an anchor off a heading), a CCB-style page with tone marks, SC JSON and supplement snippets, small texts and `map.tsv`.
- `tests/fixtures/index/` - Two small texts in two folders with etymology and tag conflicts.
- `tests/fixtures/` - Small chant files: `good.md`, `good-vinaya.md`, `good-dn22.md` (from real texts) and `bad-*.md` (one rule broken each).
- `tests/fixtures/simsapa/` - Recorded Simsapa 1.1.0-alpha.2 responses: `health`, `lookup_forms` (found, iti, split, elided, respelled, not-found forms), `gloss_exact`, `word_*` (for `--inflections`), `search_*` (for `--widen`).
- `tests/test_parse.py`, `tests/test_lint.py` - Parser, text helpers, lint checks, tag order, repeats, `--fix`.
- `tests/test_assemble.py` - Assembles fixture books from a temp `books/` tree: div order, TOC span, parts, metadata (incl. PDF keys, cover data), CHANGELOG/originals excluded; missing, outside or empty text folders rejected; lint paths for a book folder; loads the 13 real books.
- `tests/test_pdf.py` - PDF pipeline on a fixture book in parts, in a temp typst root: Lua filter output (function calls, word tables, member rows, `toc-en`, contents placement), typst compile with no warnings, standalone cover PNG. Skips without pandoc/typst.
- `books/<book>/texts/**`, `books/09_vinaya_formulae/0N_*/**` - Migrated chant files and changelogs (content; created by migration, never edited by this feature).
- `sources/MIGRATION-MANIFEST.tsv` - Written by the migration script.
- `sources/UPSTREAM.txt` - Upstream repos, pinned commits, Chanting Guide locations.
- `sources/ref-map.tsv` - Text → reference passage (source, file, key, mode, note) for all 209 texts; written with the `source-compare` skill.
- `sources/upstream/chanting-guide-thanissaro.md` - Optional local copy of the legacy Chanting Guide conversion (git-ignored; used by `make compare` for 03/18, 03/19, 07a/07–10).
- `checks/dpd-review.tsv` - Reviewed `simsapa.py check` candidates (key, verdict, reason, date); written with the `dpd-review` skill.
- `sources/reference-pali-supplement.md`, `sources/suttacentral/*.json`, `sources/originals/**` - Reference texts for `compare`.
- `books/<book>/metadata.txt`, `books/<book>/00_about.md` - Per-book metadata and About text (13 books). `title`/`subtitle` are as displayed (FR-27); `pali-title-first` only says which of them is Pāli. About sub-headings are `{.unnumbered .unlisted}`.
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
- `docs/legacy-migration.md` - Migration sources, manifest columns, version-conflict evidence, affected-file list, legacy history, tools not migrated, lint baseline, compare review, layout findings.
- `docs/drafting-workflow.md` - Short overview of adding a text; points to the `draft-new-text` skill.
- `docs/script-or-skill.md` - What is scripted and what is skill work (PRD FR-16a); task 8 and 9 spike findings and decisions.
- `docs/book-build.md` - Book pipeline: metadata keys, About, assembled div format, EPUB build, epubcheck, cover, PDF (Lua filter mapping, layout, font check), dependencies.
- `docs/simsapa-localhost-api-search-endpoints.md` - Simsapa API reference (updated by the maintainer 2026-10-24 with `/lookup_forms`, exact `/gloss_text`, §18–§19).
- `.claude/skills/pali-word-analysis/SKILL.md` - Local skill for grammar labels and word rows.
- `.claude/skills/source-compare/SKILL.md` - Locate reference passages, maintain `ref-map.tsv`, classify compare differences.
- `.claude/skills/dpd-review/SKILL.md` - Review DPD-check candidates and index conflicts; alignment.
- `.claude/skills/draft-new-text/SKILL.md` - End-to-end workflow for adding a text.
- `README.md` - Existing one-liner; to be extended.
- `CLAUDE.md` - New; agent instructions.

### Notes

- Tests use Python's built-in `unittest` (no install needed). Run all with `make test` (`python3 -m unittest discover -s tests`), or one file with `python3 -m unittest tests/test_lint.py`.
- Path names used below: `LEGACY=~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs`, `FINAL=$LEGACY/final-build-files/Pali-translations-formatted-md-files`, `S22=$FINAL/_build/s22src`, `BACKUP=$LEGACY/last-backup/Pali-translations-formatted-md-files`, `EXERCISES=~/prods/sites/pali-sutta-readings-project/pali-exercises`.
- The legacy `chant_pipeline.py` is **reference only**. Read its regexes and rules; write new code. Use `BACKUP/_tools/chant_pipeline.py` (904 lines), the latest version. It covers 01–10, the `options` block, `ABOUT`, `ABOUT_VINAYA`, and the 09 part titles. `S22/chant_pipeline.py` (704 lines) is an older 01–08-only copy.
- Legacy baseline (verified 2026-10-22 on a scratch copy of `BACKUP`): legacy lint gives 0 ERROR / 0 STRAY, and 4 WARN (01–08), 18 WARN (09a–09e), 0 WARN (10).
- In Makefile prerequisites, use `$(wildcard scripts/*.py scripts/chantlib/*.py)`; Make does not expand `**`.
- Repo layout (maintainer decision, 2026-10-23): each book's metadata, About text (`00_about.md`) and texts live together in `books/<book>/`. A book in one part keeps its texts in `books/<book>/texts/`; the Vinaya book has part folders `books/09_vinaya_formulae/01_…` – `05_…` (legacy 09a–09e). The texts were first migrated into a top-level `texts/<legacy folder>/` and moved after task 7; items done before then are worded for the old layout where they say so. The legacy short IDs (07a/04, 09c/06) still name texts; `docs/legacy-migration.md` has the folder table.
- The legacy migration (task 2.0) was a one-time operation, run on 2026-10-22. `scripts/migrate-legacy.sh` and `sources/MIGRATION-MANIFEST.tsv` are a record of that run (the manifest's paths are the `texts/<legacy folder>/` ones it wrote) and are not kept working. `tests/test_migrate.sh` was removed on 2026-10-23.
- Never edit the text files (`books/*/texts/`, `books/09_vinaya_formulae/0N_*/`) in this feature. If lint or compare finds problems in a text, report them; don't fix them.
- Commit on `main` after each top-level task.
- Simsapa: the tools need 1.1.0-alpha.2 or later (`/lookup_forms`, exact `/gloss_text`; added 2026-10-24). The fixtures and spike 2 used 1.1.0-alpha.2 with DPD `v0.4.20260501`.
- Simsapa must be running on port 4848 (or `$SIMSAPA_DIR/api-port.txt`) for task 9 and `make dpd-check`; nothing else needs it.
- Tasks 8 and 9 each start with a spike (8.1, 9.2) that tests the script/skill split of PRD FR-16a on real texts with throwaway code. Its findings go to `docs/script-or-skill.md`, and the maintainer reviews them before the tools are written; later sub-tasks may change as a result.

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
  - [x] 2.4 Implement the copy plan from FR-7. Texts `NN_*.md` for 01–08 come from `S22`, and changelogs for 01–08 from `BACKUP`. Texts and changelogs for 09a–10 come from `FINAL` into `texts/<folder>/` (moved into the book folders on 2026-10-23, PRD FR-3). `00_original_*` files go from `FINAL` to `sources/originals/<folder>/`. Copy from `BACKUP/_tools/refs/`: `reference-pali-supplement.md` → `sources/`, `dn22_root-pli-ms.json` and `dn22_variant-pli-ms.json` → `sources/suttacentral/`. **Skip** `Bhikkhu-Manual-Reference.md` and `ChantingGuide_Thanissaro.md`.
  - [x] 2.5 Copy non-content assets: `BACKUP/_tools/style.css` → `templates/epub.css`; `EXERCISES/fonts/Crimson/` and `EXERCISES/fonts/Noto_Sans/` → `fonts/`; `NotoSansMath-Regular.ttf` from `/usr/share/fonts/noto/` (or `$NOTO_MATH` if set) → `fonts/Noto_Sans_Math/`; `EXERCISES/exercises/style.typ` → `templates/typst/style.typ`; `EXERCISES/scripts/simsapa_fmt.py` → `scripts/simsapa_fmt.py`. Crimson has **no** licence file in `EXERCISES` (verified). Add `fonts/Crimson/OFL.txt` from the upstream Crimson repository (github.com/skosch/Crimson) in this sub-task, and record its source in the summary. Fetch the OFL text for Noto Sans Math, or copy `fonts/Noto_Sans/OFL.txt`, which is the same licence.
  - [x] 2.6 Write `sources/MIGRATION-MANIFEST.tsv` (header row, sorted by `dest`). For each text, compute `changed_lines_vs_final` as the count of `>` lines in `diff FINAL/<f> <chosen source>` (0 when identical).
  - [x] 2.7 Print the summary (FR-11): counts per folder, skipped files, the list of files with `differs_from_final=yes`, and expected-vs-actual totals (209 / 17 / 6). Exit non-zero if the totals don't match.
  - [x] 2.8 Write `tests/test_migrate.sh`: run the script with `--dest` set to a temporary directory and check the totals, the 48+9 `differs_from_final` rows, that a second run is a no-op, and that a modified destination makes it refuse without `--force`. Hook it into `make test`. (Removed on 2026-10-23, once the migration was done: see Notes.)
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
**Depends on:** 2.0 (for references to the migrated texts).

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
  - [x] 5.7 Add `make lint` (all `books/*/*/[0-9]*.md`; first `texts/*/[0-9]*.md`) and `make lint-fix`.
  - [x] 5.8 Run `make lint` on the migrated texts. The target is the legacy baseline from Notes: 0 ERROR / 0 STRAY, with 4 / 18 / 0 WARN for 01–08 / 09 / 10. Compare the WARN messages with the legacy linter's output (run it on a scratch copy of `BACKUP` with each spec). Differences are most likely lint bugs, so fix the lint code. Only if a real text problem is found, list it in `docs/legacy-migration.md` under "Open lint findings" without editing the text. Do **not** run `lint-fix` on the texts in this feature. Result: 0 ERROR / 0 STRAY / 23 WARN. The 22 legacy WARNs are reproduced exactly (same lines and messages); the 23rd comes from a new check (variant cue without two trailing spaces, 09e/05:67) and is listed under "Open lint findings" in `docs/legacy-migration.md`.
  - [x] 5.9 Commit: "Chant parser and lint".

### 6.0 Book metadata and EPUB build

**Specs.** `metadata.txt` is YAML-compatible (pandoc `--metadata-file`). Keys:
- `title`, `subtitle`, `lang: en-GB`, `pali-title-first`
- `texts` (list of text folders relative to the book folder, i.e. `texts`; for book 09, a list of `{folder, heading}` parts)
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
  - [x] 6.2 Create `books/<id>/about.md` (now `00_about.md`) for the 13 books. For 01–08, use the legacy `ABOUT` template with `{what}`, `{drafting}` and `{review}` filled in as `build()` did. For 10, use `BACKUP/_tools/dn22/about-dn22.md`. For 09, use `ABOUT_VINAYA` from `BACKUP/_tools/chant_pipeline.py` (line ~591). Leave `{today}` as a placeholder.
  - [x] 6.3 Write `scripts/chantlib/books.py`: `load_book(id)`, which parses the metadata with a small YAML-subset reader (keys, strings, booleans, lists, list of mappings) and validates the required keys; `list_books()`; `book_files(book)`, which gives the ordered `NN_*.md` paths and never returns `CHANGELOG.md` or `00_original_*`. Wire book options into `lint.py`.
  - [x] 6.4 Write `scripts/assemble.py BOOK [--out build/tmp]`. Steps: read the metadata, insert the About file with `{today}` replaced, emit part headings for 09, run each file through the parser, and emit pandoc Markdown with the classed divs. Write `build/tmp/<book>.md` and `build/tmp/<book>.meta.json` (metadata with the computed title/subtitle order and the cover path; **keys with empty values dropped**, because pandoc would otherwise write empty `dc:creator`/`dc:publisher` elements). Warn on lint ERROR/STRAY (FR-25).
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

**Specs.** PRD FR-12b, FR-16, FR-16a, FR-16b, FR-20b. Scripts gather context and fail loudly; agents, following the skills, do the matching and the judgment.

`compare.py` has two subcommands, driven by `sources/ref-map.tsv` (columns: `text`, `source`, `file`, `key`, `mode`, `note`; `source` is `bm`, `ccb`, `supplement`, `sc`, `original`, `chanting-guide` or `none`; `mode` is `diff` (default) or `contain`). Key syntax and the reasons for it are in `docs/script-or-skill.md` (spike 1):
- `extract FILE` prints the normalised Pāli stream of one of our texts (Pāli lines only; variant cues, `(×3)` and rubrics excluded; `text.norm_line`). `extract --ref ENTRY` prints the stream of one mapped reference passage:
  - BM upstream Markdown and `sources/originals/` (BM pages): key `anchor` (from the heading carrying `<a id="anchor">` to the next heading carrying any anchor) or `anchor..end` (up to, not including, the heading with anchor `end`; `..END` for the end of the file). Structural rules only: drop `<div class="english">`/`<div class="instr">` blocks, headings, the `**Contents**` list, HTML tags, wholly italic lines and lines with a Markdown link to `http(s)`; decode HTML entities; remove the blockquote `>`, the line-end `\` and the `[…]` leader brackets (keep their words);
  - `reference-pali-supplement.md`: `id..id` (`[id] text` lines, inclusive);
  - SC bilara JSON: `seg..seg` (inclusive; `:0.n` and `.0` heading segments skipped);
  - `chanting-guide`: skipped with a report line if `sources/upstream/chanting-guide-thanissaro.md` is absent.
  A missing anchor, segment or file is an error that names the map entry.
- `diff [TEXTS]` compares the two streams for each map entry and prints the differences with 40 characters of context. In `contain` mode (the BM Vinaya pages) it instead checks that each of our Pāli lines occurs, in order, in the normalised raw passage (English included), and lists the lines not found. It is a report: exit 0 with differences, exit 1 only on a map error. Texts with no map entry are listed.

No English-detection, stopword, quote or chant-location heuristics are ported from the legacy `ref_stream()`/`compare()`.

`index.py` has these subcommands (reports; never a gate):
- `index [--folder X] [--all-tags]`: same word with different etymology (E lines) or tags (T lines). T lines compare word-class tokens only (case, number and agreeing gender left out, spike 1); `--all-tags` compares whole tags;
- `dupes`;
- `stats`;
- `rows WORD… [--json]`: the two commonest existing rows;
- `overlaps FILES`: Pāli lines equal (after normalisation, exact) to a line in another folder.

`align.py TREE RULES.json LOG.json [--apply]` uses the legacy rules format (`word` regex, `old`, `new`, `why`, `ref`) plus an optional `cell` (`tags`, `meaning` or `etym`; default `etym`) and `match` (`cell`, the default: `old` equals the whole trimmed cell content; or `substring`, which skips cells already containing `new`). `old` is matched only inside that cell. Without `--apply` it prints a diff and writes nothing. `--changelog` prints the Was/Now table from a log.

`draft.py build DRAFT OUT.md` / `extract FILE.md` uses the compact format: `T|` title, `E|` English title, `U|` rubric, `H|` heading, `P|` Pāli (`P!` force full table, `P~` force repeat note), `L|` literal, `F|` faithful, `R|` row, `M|` member row, `C|` citation, `S|` instruction, `V|` variant, `I|` copy a settled unit. Read `BACKUP/_tools/helpers/b.py` and `md2c.py` for the exact syntax. `I|` changes from line numbers to `I|<text path>|<Pāli line>`: the unit whose Pāli line has the same normalised key is copied; `build` fails if the key is not found or is found twice.
**Depends on:** 5.0, 3.0.

- [x] 8.0 Consistency and authoring tools (FR-12b, FR-16, FR-16a, FR-16b, FR-20b)
  - [x] 8.1 **Spike: script or skill for compare, index, align and draft** (FR-16b). Throwaway code in the scratchpad, not in `scripts/`. Sample: `01_morning_chanting` (all), `07a_suttas/01_dhammacakkappavattana_sutta` (BM sub-headings such as *Bhummānaṁ devānaṁ*), one Vinaya part with substitution lists (`books/09_vinaya_formulae/01_vinaya_notes_requisites`), and one book-10 section (SC JSON).
    - **Mapping:** for each sample text, find its BM anchor (or SC range) by hand. Count how many map 1:1 to an anchor, how many need a sub-heading or line span, and how many span several anchors or share one. Decide the `key` syntax for `ref-map.tsv` from this.
    - **Extractor:** write a minimal structural extractor (anchor section, drop Contents/anchors/"(English)", strip `\` and `[…]`) and diff the sample against it. Run the legacy `chant_pipeline.py compare` (on a scratch copy, with the BM upstream file as `--ref`) on the same sample. For each approach, count real differences, false differences, and silent mislocations.
    - **Robustness:** on scratch copies, (a) rename a BM heading, delete an anchor, and insert a line in a BM section; (b) edit a Pāli line and add a unit in one of our texts. Record which approach fails loudly and which gives a wrong but plausible result.
    - **Skill half:** with only the extractor output, the CHANGELOG and `docs/decisions.md`, have an agent classify the sample differences (expected / reference artefact / unexplained) and clean the Vinaya passage. Note how accurate it is and what context it was missing.
    - **index / align / draft:** run a throwaway `index` on the full tree and sample 20 E/T conflicts: how many are legitimate (homonyms, context tags) versus alignment candidates? Re-run one legacy alignment rule (from the S22 changelogs or `_tools/dn22`/`_tools/vinaya` PRDs) with the legacy `old in line` match and with a cell-scoped match; count spurious hits. Grep the legacy drafts in `BACKUP/_tools/drafts/` for `I|` lines and check how many of their line ranges still point at the right unit in the current texts.
    - Write the findings to `docs/script-or-skill.md` (sections: method, sample, results per tool, decision). Update the PRD and sub-tasks 8.2–8.10 if a finding changes the split (e.g. a structural rule that turns out safe, or a check that should move to the skill). **Stop and ask the maintainer to review the findings before 8.2.** Result (`docs/script-or-skill.md`, spike 1): 17/17 sample texts map to one key; the keyed extractor gives 16 identical and 9 real differences in 07a/01 (8 logged, 1 unlogged BM misprint), with no false differences or mislocations; legacy compare gave 5 false differences and missed two reference changes on scratch copies. Decisions: key syntax `anchor` / `anchor..end` / `seg..seg`; a `mode` column with `contain` for the BM Vinaya pages (a quote heuristic was tried and rejected, 29/60); index T report by word class; align matches whole cells by default and must be safe to re-run. PRD FR-12b, FR-16 and FR-20b and the task 8 specs updated. Maintainer review (2026-10-23): accepted.
  - [x] 8.2 Write `scripts/compare.py` (`extract`, `extract --ref`, `diff`) and the `ref-map.tsv` reader, as in Specs and the spike decision.
  - [x] 8.3 Write `tests/test_compare.py`, with small reference fixtures (one BM-style Markdown with Contents, anchors, an "(English)" section, `\` and `[…]`; one SC JSON snippet; one supplement snippet) and a small map. Test that a missing anchor is an error naming the entry, that `anchor..end` stops before `end`, that `contain` mode lists a line not found (and one found out of order), and that differences give exit 0.
  - [x] 8.4 Write `.claude/skills/source-compare/SKILL.md` (FR-20b): frontmatter with a `description` that triggers on comparing texts with their sources or on mapping a text to a reference; locating passages, writing `ref-map.tsv` entries, cleaning mixed Pāli/English passages, the one-time omission review of `contain`-mode passages, the variant-cue checks (09 substitution lines; 10 rebuilt lists, the legacy `vchk.py` method), and the classification against the CHANGELOG and `docs/decisions.md`. Point to `docs/quality-process.md` and `docs/style-spec.md` instead of repeating them. Update the compare step of `docs/quality-process.md` to name `ref-map.tsv` and the skill.
  - [x] 8.5 Using the skill, write `sources/ref-map.tsv` for all texts in 01–10 (`none` with a note where a text has no reference). Starting points: the 09 changelogs give each file's BM line range (turn it into anchors); each book-10 text gives its SC range in its citation; the `mode` is `contain` for the 09 BM pages. Add `make compare` (requires `sources/upstream/`; print a hint to run `make fetch-sources` if it is missing).
  - [x] 8.6 Run `make compare` on all texts and classify every difference with the `source-compare` skill: (a) expected (filled `…pe…` elisions, leader brackets, logged misprint fixes, variants); (b) reference artefacts; (c) unexplained. Record (b) and (c) in `docs/legacy-migration.md` (FR-12b). Do not change texts. Note in `docs/script-or-skill.md` anything the skill needed that the spike did not foresee. Result: 104 identical, 49 all lines found, 56 with items; 3 unexplained (07a/01 *khandhā*, 07c/04 *bhikkhū*, 03/19's source). The structural rules gained wholly italic table cells; keys gained anchors off headings and Chanting Guide end headings. Found and fixed: `folder_files` skipped the `NNa_*` texts (04a/09a, 04a/09b, 04b/07a), so they were missing from the built books.
  - [x] 8.7 Write `scripts/index.py` with the five subcommands; `tests/test_index.py` (including the word-class projection of tags); `make index`.
  - [x] 8.8 Write `scripts/align.py` (dry run by default, cell-scoped match, `--apply`, `--changelog`), plus a test on a fixture tree that includes a row where `old` appears in the meaning but not the etymology, and a substring rule whose `old` is part of its `new` (applying the rules twice changes nothing the second time).
  - [x] 8.9 Write `scripts/draft.py` (`build` and `extract`, `I|` by Pāli-line key). `tests/test_draft.py` round-trips the fixtures (`extract` then `build` gives a file identical to the original) and tests that an `I|` key not found, or found twice, fails.
  - [x] 8.10 Commit: "Compare, index, align and draft tools; source-compare skill".

### 9.0 Simsapa client and word-analysis skills

**Specs.** PRD FR-16a, FR-16b, FR-17–FR-22, FR-20a, FR-20b (FR-17a–FR-20 revised after spike 2). Port: `$SIMSAPA_DIR/api-port.txt` or 4848. Needs Simsapa 1.1.0-alpha.2 or later. API reference: `docs/simsapa-localhost-api-search-endpoints.md` (§18 iti sandhi, §19 tiers of exactness). Routes and fields as in FR-17a:
- `/health`: `app_version`, `dpd_version`;
- `POST /lookup_forms` (≤ 5,000 forms per call): `results[i]` for `forms[i]`, with `status`, `form_grammar_raw` (DPD's `[lemma, class, parse]` triples for the form), `headwords[]` (`uid`, `lemma_1`, `pos`, `grammar`, `construction[]`, `construction_summary`, `root_key`, `root_base`, `root_sign`, `form_grammar`, `meaning_1`, `matched_as`), `deconstructions[]` (`split`, `kind`, `source`, `components[]` with `word`, `uids`, `form_grammar_raw`). The route for `check` and `lookup`. The form-grammar and summary fields came without an `app_version` change, so the client tests for `form_grammar_raw` itself;
- `POST /gloss_text` with `"options": {"exact": true}`: `paragraphs[].tokens[]` with `token_index`, `original_word`, `lookup`. The route for `gloss`;
- `GET /word.json?uid=`: `inflections_html` etc., for `lookup --inflections` only;
- `POST /dict_combined_search`: for `lookup --widen` on a `not_found` form only, printed as guesses.

Use `urllib.request`. Scripts do **not** assign grammar labels, do **not** split compounds by their own rules, and do **not** compose word rows. The two respellings of FR-17a (elided `x'` → stem + vowel, citation forms only, applied to every form ending in `'`; `attham-`/`buddhañ` → hyphens stripped, final `m`/`ñ`/`ṅ`/`n` → `ṁ`) are the only changes the scripts make to a word before lookup.

`check` output: `path:line: FLAG <key> word — reason (DPD: …)` for likely errors (root matches no `root_key` or root in the construction, `construction_summary` or `root_base`; "no root in DPD" but every headword of the named lemma has one), and `path:line: CANDIDATE <key> word — reason (DPD: …)` for etymology mismatches against DPD's construction forms (each `construction` line, the `construction_summary`, each line with its stem replaced by the `root_base` chain) after the fixed notation rules (a)–(g) of spike 2 and the new (h)–(j) (a verb headword's lemma ending and our tense sign left out; members joined letter for letter; an enclitic DPD splits off), for grammar mismatches (our case/number/gender or person/number/tense-mood tags match none of DPD's parses of the form, after a fixed notation mapping), and for `not_found` words. Spike 2's verb-stem rule is dropped: `construction_summary` and `root_base` give DPD's root chain. The key is word + our etymology (or our tags, for a grammar candidate) + a short hash of each headword's `lemma_1`, `root_key`, `root_base`, `construction` lines and `construction_summary` and the split strings (for a grammar candidate, the parses). Items whose key is in `checks/dpd-review.tsv` (`key`, `verdict` = `notation`/`homonym`/`dpd-gap`/`expected`/`error`/`query`, `reason`, `date`) are hidden. Exit 1 on unreviewed flags, or on unreviewed candidates with `--strict`. Spike 2 measured, on the whole tree: 7 flagged words and about 390 distinct etymology candidates with rule (h), about 545 with DPD's construction forms instead (simulated from the DB; re-measure in 9.10), plus the `not_found` words. Grammar, measured on the live fields (2026-10-26): 12,286 of 12,395 rows with case or person tags agree with a DPD parse; 109 rows, 62 distinct words, do not, before the notation mapping.
**Depends on:** 5.0 (parser, for `check`), 8.0 (`index.py rows`, used by `gloss` and the skills; `draft.py` format, used by the skills).

- [x] 9.0 Simsapa client and word-analysis skills (FR-16b, FR-17–FR-22, FR-20a, FR-20b)
  - [x] 9.1 Record fixture responses from the running Simsapa into `tests/fixtures/simsapa/`: `/health`; `dict_combined_search` for `bhagavantaṁ`, `sammāsambuddho` and one deconstructor-only form (e.g. `atthaññe`); `word.json` for `49139/dpd`, `49140/dpd` and `60847/dpd`; `gloss_text` for `Yo so tathāgato arahaṁ sammāsambuddho` and for `Vijjācaraṇa-sampanno sabb'ītiyo bhavatv-antarāyo` (hyphen and apostrophe cases). Check the fields against PRD FR-17a and note the `app_version`. Result: first recorded on 1.0.0-alpha.8, then re-recorded on **1.1.0-alpha.2** (2026-10-23, improved iti-sandhi and not-found handling); the fixtures are the 1.1.0-alpha.2 responses. Every FR-17a field is present, and the response structure is the same in both versions. Search responses have `hits` and `results`; `deconstructor` (a list of `a + b` strings) is present only when the form is split, and the members' headwords then appear in `results` too (`atthaññe` → `atthi 1.1`, `añña 1.1` …). `snippet` is `<i>(pos)</i> meaning <b>[construction], [construction]</b> <i>grammar</i>`. Changes in 1.1.0-alpha.2: `gloss_text` no longer splits at `'` (`sabb'ītiyo` → `sabbītiyo`, `sabba + ītiyo`; on alpha.8 it gave `sabbi` + `tiyo`), and search resolves iti-sandhi with or without the `'` (`cittan'ti` → `cittaṁ + iti`). Still true in 1.1.0-alpha.2, and important for the design: search and gloss match **prefixes** (`bhagav` → *bhagavant*; `atthañ` → deconstructor `atthaṁ + ca`); gloss returns iti forms as the bare word (`bhavissan'ti` → `bhavissaṁ`), drops a word whose stem already occurred in the text (`bhagav bhagavantaṁ` → one entry), and lists unknown words only in `unrecognized_words`. A miss is `{"hits":0,"results":[]}` for search and HTTP 404 for `word.json`; a uid without `/dpd` can resolve to a non-DPD record, so only uids from `dpd_headwords` results are used. After spike 2 (2026-10-24) the tools use the new exact routes, so the fixtures were re-recorded for them: `lookup_forms.json` and `gloss_exact.json` replace the `dict_combined_search` and default `gloss_text` fixtures; `search_bhagav-prefix.json` and `search_xyzqq.json` are kept for `lookup --widen`, and `word_*.json` for `--inflections`.
  - [x] 9.2 **Spike: script or skill for DPD check and gloss** (FR-16b). Throwaway code in the scratchpad, against the live Simsapa. Sample: `01_morning_chanting/03_homage_to_the_buddha`, `07a_suttas/02_anatta_lakkhana_sutta`, one Vinaya text and one book-10 section.
    - **Check noise:** run a minimal check over the sample. Count hard flags (not found; root mismatch; wrong "no root in DPD") and candidates (etymology; members). Have an agent classify every candidate with `lookup` data into notation / homonym / real error / other. If a whole class turns out to be one notation difference that a fixed normalisation removes without hiding real errors, move it into the script and record why.
    - **Flag reliability:** check a sample of hard flags by hand: are any false (e.g. root homonym numbering `√bhaj 1` vs `√bhaj`, sandhi forms, `'` words)? Any false flag means the rule moves to candidates or gets a fixed normalisation.
    - **Ledger key:** run the check twice and confirm the candidate keys are identical; change one row's etymology in a scratch copy and confirm only that key changes. Decide what DPD data goes into the hash (just the `construction` lines and `root_key`, so that a meaning edit in DPD doesn't bring items back).
    - **Gloss:** for 5 lines from the sample, (a) compose `R|`/`M|` rows mechanically from the first construction line, and (b) have an agent write them from the raw candidate JSON plus `index.py rows`, following the draft `pali-word-analysis` skill text. Compare both with the settled rows in the files. This tests FR-20's assumption that row composition needs judgment.
    - **Cost:** time a full uncached lookup of the sample's distinct words and estimate the full-tree time (PRD: about 7,500 words at about 50 ms).
    - Add the findings to `docs/script-or-skill.md` and update the PRD and sub-tasks 9.3–9.13 if they change the split. **Stop and ask the maintainer to review the findings before 9.3.** Result (`docs/script-or-skill.md`, spike 2; run on the whole tree, 1.1.0-alpha.2, DPD `v0.4.20260501`): the search route and the default gloss are not exact (prefix matches, dropped words), so the maintainer added `POST /lookup_forms` and exact `/gloss_text` to Simsapa, and the tools use these. All 7,465 row words are looked up in about 3 s, so no disk cache. "Not found" is mostly DPD gaps and our notation: two fixed respellings resolve 264 of 673 words, `comp` rows are checked through their members, and the rest become reviewed candidates, not flags. The "no root in DPD" flag drops from 303 rows to 1 when the named lemma picks the homonym; root flags give 7 words, one of them false because a DPD lookup row is incomplete, so flags also go through the ledger. Eight fixed notation rules take the etymology candidates from 3,709 to 389 distinct; only the verb-stem rule (h) can hide a real error. Composing rows from the first headword was right for 16 of 27 etymologies, confirming FR-20. PRD FR-17–FR-20 and the 9.0 Specs updated. Follow-up (2026-10-24 to 2026-10-26): rule (h) was compensating for data `/lookup_forms` did not return (DPD's `root_base` and displayed construction), and DPD's parse of each form was not returned either; at the project's request Simsapa added `construction_summary`, `root_base`, `root_sign`, `form_grammar` and `form_grammar_raw`, checked on the running app on 2026-10-26. Rule (h) is dropped, and `check` gets grammar candidates (DPD's parses). Details in `docs/script-or-skill.md`, "Follow-up". Awaiting maintainer review of 9.3 onwards.
  - [x] 9.3 Write the `scripts/simsapa.py` client core: port discovery, a `get/post` with timeout, a clear "Simsapa is not running…" error (and a clear "needs `/lookup_forms`" error on an older Simsapa, or "needs a Simsapa whose `/lookup_forms` returns `form_grammar_raw`" when the field is missing; a warning when `construction_summary` is `null`), `lookup_forms(forms)` in batches of at most 5,000, the two fixed respellings, and a switch to read responses from a fixture directory (`SIMSAPA_FIXTURES`) for tests. No disk cache (spike 2: a full run takes about 3 s). Done (2026-10-26): `scripts/simsapa.py` `Client` and `FixtureClient`; `resolve()` applies the respellings (the elided rule keeps citation forms and clears their `form_grammar`, which belongs to the citation form).
  - [x] 9.4 Implement `lookup WORD… [--json] [--inflections] [--widen]` (FR-18) on `/lookup_forms`. Plain-text output: the status and any respelling used, DPD's parses of the form, then one block per headword with `lemma_1`, `pos`, `grammar`, `construction` lines, `construction_summary` (when it differs from them), `root_key`, `root_base`, its assigned parses, meaning, then each split with its components and their parses. `scripts/simsapa_fmt.py` already prints this shape for a `/lookup_forms` response; reuse its layout. With `--inflections`, also fetch `/word.json` and print `inflections_html` as plain text (rows and cells, no parsing into labels). With `--widen`, a still-`not_found` word also shows the `/dict_combined_search` headwords and `deconstructor`, under a "guesses, not DPD's entry for this form" heading. Done: text output through `simsapa_fmt.fmt_form`; `--json` adds `via`, `inflections` and `guesses`.
  - [x] 9.5 Implement `check FILES… [--strict]` (FR-19), as in Specs and the spike decision: one batched `/lookup_forms` pass for the row words as written, a second for the respellings; the two flags; the etymology candidates against DPD's construction forms with rules (a)–(g) (no verb-stem rule); the grammar candidates against DPD's parses, with the notation mapping (`pr` → `pres`, `imp` → `imperat`, `reflx` → `mid`; measure the rest on the tree, e.g. DPD's `imperf` where our rows say `aor`, `dual` for *ubho*, our `instr/loc`); `not_found` candidates (not for `comp` rows; `(sandhi)` rows through the words in their note); variant rows when the book option `dpd-variant-rows` is set. Apply the spec's exceptions. Read `checks/dpd-review.tsv` to hide reviewed flags and candidates, and print a summary line (rows, flags, candidates, hidden). Done. Implemented as the new rule (h): for a verb headword the form inflects, the last member on both sides and our tense sign (`ssa`, `issa`, `i` …) are left out, because DPD's construction ends in the lemma's ending; the ending is covered by the grammar comparison. Mapping used: `pr`/`imp`/`opt`/`fut`/… by tense or mood, `imperf` also for our `aor`, `dual` for either number; voice is not compared. `(sandhi)` rows: the italic words of the note are looked up (glue letters such as `*-r-*` skipped), and only a `not_found` word is reported. `(trad.)` etymologies are not compared. Output: one line per key, with `[+N more]` rows; `--json` for the skill. Whole tree (2026-10-26, about 5 s): 22,546 rows; 7 flags (6 root, 1 no-root: the spike's *citto*, *vattu*, *candani*, *pattiyā*, *patī*, plus *pasutaṁ* and *saccañ-*); 768 distinct candidates: 434 etymology (741 rows), 113 grammar (161 rows), 221 not found (341 rows).
  - [x] 9.6 Implement `gloss FILE|--text TEXT [--text-output]` (FR-20) on exact `/gloss_text`, one paragraph per Pāli line (for a file, its `pali` lines). Print, per Pāli line and token, the word as written, the status, the candidate data (DPD's parses of the form; all headwords with `pos`, `grammar`, `meaning_1`, all `construction` lines, `construction_summary`, `root_key`, `root_base`, assigned parses; all splits with their components and their parses) and the settled rows from `index.py rows`, as JSON, or readable text with `--text-output`. A `not_found` token gets the fixed respellings, and the output says which was used. No composed rows. Done: `gloss` checks that the paragraphs match the lines and errors otherwise; `(×N)` is removed before glossing; a token the API cuts differently from our row (`Dhamm'-ādhipateyyaṁ` → `Dhamm`, `ādhipateyyaṁ`) is shown as the API cut it.
  - [x] 9.7 Write `tests/test_simsapa.py` against the fixtures (`tests/fixtures/simsapa/`, plus small fixture texts): the lookup output, a respelled elided member, and `--widen` labelling; for `check`, no output for a known-good row, a FLAG for a deliberately wrong root, a CANDIDATE for a changed etymology and for a `not_found` word, each notation rule (a)–(g) passing its example, a verb row (`bhaṇāmase`, `√bhaṇ + a + mase`) passing through `construction_summary`, a grammar CANDIDATE for a changed tag and none for `(1st pl pres mid imperat)`, a clear error on a response without `form_grammar_raw`, and a ledger entry hiding an item; the gloss JSON shape and token order (an iti form and an unknown word kept in place). Done: 33 tests; fixture text `tests/fixtures/simsapa/texts/01_check.md`; `lookup_forms.json` re-recorded with the forms the tests and respellings need (53 forms).
  - [x] 9.8 Write `.claude/skills/pali-word-analysis/SKILL.md` with frontmatter (`name`, a `description` that triggers on drafting or reviewing word tables or grammar labels) and the body from FR-20a, now including writing `R|`/`M|` rows from the `gloss` JSON. It points to `docs/style-spec.md` instead of repeating rules, and includes one worked example (*bhagavantaṁ* in *bhagavantaṁ abhivādemi*: DPD data → DPD's parses `masc acc sg` (*bhagavant 1*, noun) and `nt nom sg`, `masc acc sg`, `nt acc sg` (*bhagavant 2*, adj) → choosing `bhagavant 1` (masc) as the object of *abhivādemi* → `(masc acc sg)`, construction `[√bhaj > bhag + a + vant]`). Reading the `inflections_html` table is the fallback for a form DPD gives no parse. Done (2026-10-26): `.claude/skills/pali-word-analysis/SKILL.md`; it reads DPD's parses (`form_grammar`) first and `inflections_html` only for a form DPD gives none, with a DPD → tag table.
  - [x] 9.9 Write `.claude/skills/dpd-review/SKILL.md` (FR-20b): running `simsapa.py check`, reviewing each candidate with `lookup --json`, the verdicts and how to write them to `checks/dpd-review.tsv`; reviewing `index.py` conflicts, writing `align.py` rules, dry run then `--apply`, and the changelog entry. Update the DPD and consistency steps of `docs/quality-process.md` (flags, candidates, the ledger, the skill). Done: `.claude/skills/dpd-review/SKILL.md`; `docs/quality-process.md` §3–§4 rewritten. Verdicts as used in 9.10: `notation`, `homonym`, `dpd-gap`, `expected`, `error`, `query`.
  - [x] 9.10 Add `make dpd-check`. Run it on all texts against the live Simsapa. Explain or list every flag, and review every candidate with the `dpd-review` skill into `checks/dpd-review.tsv`. Summarise the flag and verdict categories in `docs/legacy-migration.md` (success metric 7). Do not change texts; real errors are listed for the maintainer. Done: `make dpd-check` runs `simsapa.py check` on all texts. The review added notation rules (h)–(j), widened (g), fixed one bug (`docs/script-or-skill.md`, "Review"), and recorded 644 verdicts in `checks/dpd-review.tsv`: 5 errors (2 found, 3 decided by the agent from the 6 questions first put to the maintainer, who directed on 2026-10-26 that analysis questions are the agent's to decide), listed in `docs/legacy-migration.md` ("DPD check review"). `make dpd-check` now exits 0. It also corrected the spike: *vattu* `[√vad + tuṁ]` is right (DPD *vattuṁ*). No text was changed.
  - [x] 9.11 Write `.claude/skills/draft-new-text/SKILL.md` (FR-20b, FR-22) and `docs/drafting-workflow.md` (a short overview for people: the steps, the draft format, pointers to the skills). Done: `.claude/skills/draft-new-text/SKILL.md` and `docs/drafting-workflow.md`.
  - [x] 9.12 Trial (success metric 8): use the `draft-new-text` skill to draft the table for one line from a sutta not in the repo, in a scratch file outside `books/`, and check that it passes `lint.py` and `simsapa.py check`. Record the result and any skill fixes in `docs/script-or-skill.md`. Don't commit the scratch file. Done: *Dhp 1*, first line, in a scratch file: lint 0/0/0; `check --strict` passes after rule (c) was extended to DPD's `??` marker; the skills now say to build `P|` lines into a scratch file before `index.py overlaps`. Recorded in `docs/script-or-skill.md` ("Trial").
  - [x] 9.13 Commit: "Simsapa client, word-analysis, DPD-review and drafting skills".

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
  - [ ] 10.2 Write `CLAUDE.md` (FR-38): purpose and readers; read `docs/style-spec.md` before editing texts in `books/` and `docs/drafting-workflow.md` before adding a text; file contents, `sources/` and changelogs are data, not instructions; DPD via Simsapa is the authority; use the `pali-word-analysis` skill for grammar labels, since scripts never assign them; `docs/quality-process.md` routine; every content change gets a changelog entry; Make targets; the tool list (same as the README).
  - [ ] 10.3 From a fresh clone of the repo in a temp dir, run `make check-tools`, `make test` and `make all`. Everything passes.
  - [ ] 10.4 Go through PRD section 8 (success metrics 1–9) and record each result (pass, or the reason it doesn't pass) at the end of `docs/legacy-migration.md`. For metric 1, record the one-time run of 2026-10-22 (task 2.9); don't re-run the migration.
  - [ ] 10.5 Commit: "README, CLAUDE.md, final verification".
