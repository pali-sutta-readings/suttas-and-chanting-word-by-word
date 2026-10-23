# PRD: Repository Setup, Legacy Migration and Book Build System

## 1. Introduction / Overview

This repository keeps Pāli suttas and chants, each line followed by a literal and a natural English rendering and a word-by-word analysis table. The texts were produced in an earlier, agent-driven project ("the legacy project"). That project's working folder was deleted. What remains is in two snapshots copied over from a Mac:

| Name used in this PRD | Path |
| :--- | :--- |
| `LEGACY` | `~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs` |
| `FINAL` | `$LEGACY/final-build-files/Pali-translations-formatted-md-files` |
| `S22` | `$FINAL/_build/s22src` (the source snapshot the legacy 01–08 books were built from) |
| `BACKUP` | `$LEGACY/last-backup/Pali-translations-formatted-md-files` (Time Machine snapshot; a clean git repo, 49 commits) |
| `EXERCISES` | `~/prods/sites/pali-sutta-readings-project/pali-exercises` (typst styles and fonts to reuse) |

This feature does the following:

1. Designs a clean folder structure for this repo.
2. Writes a **migration shell script** that copies the right legacy files into it, choosing the correct version of each file.
3. Defines a **build system**, driven by Makefile targets and Python scripts. It builds an EPUB (pandoc) and an A5 PDF (typst) per book. Book details come from per-book metadata `.txt` files.
4. Replaces the legacy local-DPD-database checks with the **Simsapa localhost API**.
5. Re-documents the legacy project's key editorial decisions in `docs/`, and writes `README.md` and `CLAUDE.md`.

The goal is a repo where anyone, human or agent, can clone it, install the listed tools, run `make`, and get correct, attributed books. They can also edit or add texts by following written rules.

## 2. Goals

1. All 226 content files (209 chant/section files and 17 changelogs, plus 6 `00_original_*` source files) are migrated, each from its correct source version, with a manifest that records where each file came from.
2. `make all` builds 13 books, each as an EPUB and an A5 PDF, with no manual steps.
3. Every book's title, subtitle, language, sources/attribution, cover and About text come from that book's files under `books/`, not from Python code.
4. Word-analysis checks and lookups use the Simsapa API; no local `dpd.db` is needed.
5. The editorial rules (the style spec and decisions from the legacy PRDs and guides) are written in `docs/`, and `CLAUDE.md` tells an agent to read them.
6. `README.md` and `CLAUDE.md` list every required tool, how to check for it, and how to install it.

## 3. User Stories

- **As the maintainer (a bhikkhu)**, I want to run one migration script and get all finished texts into the new repo, so that I don't have to sort the legacy folders by hand.
- **As the maintainer**, I want to know which legacy files had conflicting versions and why one was chosen, so that I can review those files later if needed.
- **As the maintainer**, I want to run `make` and get EPUBs and PDFs with correct titles, sources and licence, so that I can share them right away.
- **As the maintainer**, I want to change a book's title, About text or cover by editing a text file, without touching code.
- **As an agent editing texts**, I want `CLAUDE.md` to point me to the style rules and to the Simsapa workflow, so that my edits follow the same conventions as the existing files.
- **As an agent adding a new sutta**, I want a documented drafting workflow (a compact draft format, DPD lookups via Simsapa, lint, compare, index), so that new texts reach the same standard as the legacy ones.
- **As a new contributor**, I want `make check-tools` to tell me which tools are missing and how to install them.

## 4. Functional Requirements

### 4.1 Folder structure

FR-1. The repo must use this layout (names may be refined during implementation, but the separation of concerns must stay):

```text
README.md                 overview, tool install, build usage
CLAUDE.md                 agent instructions; points to docs/
Makefile                  all build and check targets
.gitignore                build/, sources/upstream/, .DS_Store, ._*, __pycache__/
books/                    one folder per book (13 books), holding its content
  01_morning_chanting/
    metadata.txt          title, subtitle, lang, sources, cover, text folders, etc.
    00_about.md           the "About This Book" front matter (00_ sorts it first)
    cover.jpg             optional override; normally the cover is generated (FR-33a)
    texts/                the chant files: NN_name.md + CHANGELOG.md
  …
  09_vinaya_formulae/     a book in parts: one numbered folder per part
    01_vinaya_notes_requisites/   (legacy 09a) NN_name.md + CHANGELOG.md
    …
    05_vinaya_notes_uposatha/     (legacy 09e)
  10_mahasatipatthanasutta/
    texts/
sources/                  reference texts used for checks (never built into books)
  UPSTREAM.txt            upstream repo URLs + pinned commits (FR-12a)
  upstream/               git-ignored clones made by `make fetch-sources`
    bhikkhu-manual/       → manuscript/markdown/ (BM's own Markdown)
    community-chanting-book/ → chapters/english/markdown-vol1, -vol2, -satipatthana
    chanting-guide-thanissaro.md  optional local copy, not committed (FR-12a)
  reference-pali-supplement.md
  suttacentral/dn22_root-pli-ms.json, dn22_variant-pli-ms.json
  originals/09a…09e, 10/  the 00_original_* files, unchanged
  MIGRATION-MANIFEST.tsv  written by the migration script
templates/
  epub.css                adapted from legacy style.css
  typst/                  style.typ, book.typ, cover.typ (adapted from EXERCISES)
  pandoc/                 Lua filter(s), typst template
fonts/                    Crimson, Noto Sans, Noto Sans Math (fallback for ↳, see FR-32)
scripts/                  Python tools (see 4.4), migrate-legacy.sh, fetch-sources.sh
docs/                     style spec, decisions, workflows, Simsapa API doc
tasks/                    PRDs and task lists
.claude/skills/pali-word-analysis/SKILL.md   local skill for grammar labels (FR-20a)
build/                    output (git-ignored)
```

FR-2. The `00_original_*` files must **not** remain among the texts in `books/`. They move to `sources/originals/<folder>/`, so that no build or lint glob can match them. (The legacy project had to guard against this by hand.)

FR-3. Legacy file names must be kept unchanged, and each legacy folder maps to exactly one text folder, so that every changelog line reference and every cross-reference (e.g. "07a/04") can still be resolved. A book in one part keeps its texts in `books/<book>/texts/`. The Vinaya book is in parts: legacy `09a_*` … `09e_*` become `books/09_vinaya_formulae/01_*` … `05_*` (the number keeps the order; the rest of the name is kept). This layout replaced a first top-level `texts/<legacy folder>/` layout (maintainer decision, 2026-10-23: a book's metadata, About text and texts live in one place). `docs/legacy-migration.md` gives the folder table.

### 4.2 Migration script

**Status (2026-10-23).** The migration is a one-time operation. It ran once, on 2026-10-22 (commit `9a2cbb9`), and met FR-4 to FR-11. The script and `sources/MIGRATION-MANIFEST.tsv` are kept as a record of that run and are not maintained. Content and layout have changed since (FR-3), so the script is not expected to work on the repo again, and no test runs it. FR-10's re-run safety applied while the migration was being developed.

FR-4. Provide `scripts/migrate-legacy.sh` (bash), runnable as `scripts/migrate-legacy.sh [LEGACY_DIR]`, defaulting to the `LEGACY` path above.

FR-5. The script must copy files byte for byte. It must not change any content.

FR-6. The script must skip macOS junk: `._*` files, `.DS_Store`, `__pycache__/`, `*.pyc`.

FR-7. The script must choose each file's source by this table. **Do not use file timestamps**: they are unreliable after the copy between computers.

| What | Copy from | Copy to | Why (see 4.3) |
| :--- | :--- | :--- | :--- |
| `01_*` … `08_*` text files (`NN_*.md`) | `S22/<folder>/` | `texts/<folder>/` (now `books/<folder>/texts/`, FR-3) | S22 holds the final S22 pass |
| `01_*` … `08_*` `CHANGELOG.md` | `BACKUP/<folder>/` | `texts/<folder>/` (now `books/<folder>/texts/`) | S22 has no changelogs; FINAL's 01–07b changelogs lack the S22 entry |
| `09a_*` … `09e_*`, `10_*` text files and changelogs | `FINAL/<folder>/` | `texts/<folder>/` (now `books/09_vinaya_formulae/0N_<name>/` and `books/10_mahasatipatthanasutta/texts/`, FR-3) | Not in S22; FINAL = BACKUP |
| `00_original_*` (09a–09e `.md`, 10 `.txt`) | `FINAL/<folder>/` | `sources/originals/<folder>/` | FR-2 |
| `_tools/refs/*` except `Bhikkhu-Manual-Reference.md` and `ChantingGuide_Thanissaro.md` | `BACKUP/_tools/refs/` | `sources/` (renamed as in FR-1) | needed by `compare` |
| `_tools/style.css` | `BACKUP/_tools/` | `templates/epub.css` | start point for EPUB styling |
| Fonts `Crimson/`, `Noto_Sans/` | `EXERCISES/fonts/` | `fonts/` | FR-32 |
| `NotoSansMath-Regular.ttf` (+ its `OFL.txt`) | the system Noto install (`/usr/share/fonts/noto/` on Arch, package `noto-fonts`), or the notofonts GitHub release if not installed | `fonts/Noto_Sans_Math/` | FR-32: fallback for `↳` |
| `style.typ` | `EXERCISES/exercises/style.typ` | `templates/typst/style.typ` | adapted later |
| `simsapa_fmt.py` | `EXERCISES/scripts/simsapa_fmt.py` | `scripts/simsapa_fmt.py` | FR-21 |

FR-8. The script must **verify** before copying:
   - each `01–08` text in `S22` is byte-identical to the same file in `BACKUP` (expected: 130 of 130). If not, stop and list the mismatches.
   - each `07c`, `08`, `09a–09e`, `10` file in `FINAL` is byte-identical to `BACKUP` (expected: all). If not, stop and list the mismatches.

FR-9. The script must write `sources/MIGRATION-MANIFEST.tsv` with one row per copied file: destination path, source snapshot (`S22`/`FINAL`/`BACKUP`/`EXERCISES`), source path, SHA-256, and a `differs_from_final` flag (yes/no) plus the count of changed lines versus the FINAL copy.

FR-10. The script must be safe to re-run. It must not overwrite a destination file that differs from its source unless `--force` is passed. It prints what it would overwrite and exits non-zero.

FR-11. The script must print a summary: files copied per folder, files skipped, and the list of files where FINAL differed from the chosen source.

FR-12. The script must not copy: legacy `_build/` outputs (EPUB/PDF/zip), `_dpd/` (2.3 GB SQLite), `_s0dn22/`, `_s2tmp/`, `_s3tmp/`, `_s8tmp/`, `_to_delete/`, `_tools/drafts/`, the legacy `.git/`, or verbatim copies of the legacy spec, PRDs, guides, checkpoints and scripts. Their content is re-documented in `docs/` (4.6). The implementer reads them in place from `LEGACY`. `_tools/refs/Bhikkhu-Manual-Reference.md` is also not copied: it was converted back to Markdown from the BM EPUB's HTML, and BM's own Markdown is now available upstream (FR-12a). `_tools/refs/ChantingGuide_Thanissaro.md` is not committed either (maintainer decision, 2026-10-22); its locations are recorded instead (FR-12a).

FR-12a. **Upstream sources.** `sources/UPSTREAM.txt` records the source repositories, and `scripts/fetch-sources.sh` (`make fetch-sources`) clones or updates them into `sources/upstream/` (git-ignored) at the commit pinned in `UPSTREAM.txt`. The script can also update the pin on request (`--update`).

| Source | Repository | Use | Licence |
| :--- | :--- | :--- | :--- |
| Bhikkhu Manual (BM), Reference Edition, Amaravati Publications 2020 | https://github.com/bhikkhu-manual/bhikkhu-manual | Markdown in `manuscript/markdown/` (`chants/*.md`: morning, evening, reflections, parittas, anumodana, funeral, suttas, patimokkha; `vinaya/`). This is the reference for `compare` on 01–09, replacing the legacy EPUB-to-Markdown conversion. | CC BY-NC-ND 4.0 |
| Community Chanting Book (Amaravati Publications, 2021) | https://github.com/profound-labs/community-chanting-book | English edition, Markdown in `chapters/english/markdown-vol1/`, `markdown-vol2/`, `markdown-satipatthana/` (LaTeX sources beside them). Recorded for later use as needed; not used by any check yet. | CC BY-NC-ND 4.0 |
| *A Chanting Guide* (Ṭhānissaro Bhikkhu; Dhammayut Order in the USA) | Web: https://www.dhammatalks.org/books/ChantingGuide/ · EPUB: https://www.dhammatalks.org/Archive/Writings/Ebooks/ChantingGuide210709.epub · index: https://www.dhammatalks.org/ebook_index.html · legacy Markdown conversion: `$BACKUP/_tools/refs/ChantingGuide_Thanissaro.md` | Recorded for later use as needed. It is a different book from the Community Chanting Book. The legacy project used it as the source for chants not in BM. `fetch-sources.sh` does not download it. | CC BY-NC 4.0 |

Only the two git repos are cloned. The Chanting Guide is recorded in `UPSTREAM.txt` as locations only. When `compare.py` meets a chant whose source is the Chanting Guide and finds no local copy at `sources/upstream/chanting-guide-thanissaro.md`, it skips that chant and lists it in its report rather than failing.

FR-12b. `compare.py` must read BM's upstream Markdown and strip its markup before normalising. The chant files (e.g. `chants/morning-chanting.md`) hold several chants per file: a `**Contents**` list of links, then `## Title<a id="…"></a>` sections, with Pāli and "(English)" sections alternating, lines ending in `\`, and leader words in `[…]`. The reader drops the contents list, the anchors and the "(English)" sections, and removes the line-end `\` and the leader brackets. The first run on 01–09 must be reviewed: any difference that comes from the old EPUB conversion rather than from the texts is noted in `docs/legacy-migration.md`. Text files are not changed.

### 4.3 Version conflict record (evidence for FR-7)

FR-13. `docs/legacy-migration.md` must record the following evidence and the list of affected files, so that they can be reviewed later.

**Finding.** The user's instruction was that `FINAL` supersedes `BACKUP`. But for folders 01–07b, `FINAL`'s files are *older* than both `BACKUP` and `S22`.

**Evidence.**

1. `BACKUP` is a git repository whose working tree is clean (no uncommitted changes). Its HEAD is commit `94cb57e` ("S8 (DN 22): final unit …", 2026-10-13), the last commit of the whole project.
2. Every `CHANGELOG.md` in `BACKUP` for 01–08 starts with **"2026-10-11 — session S22 (final: whole-tree index alignment)"**. In `FINAL`, the 01–07b changelogs stop at S19c, S20 or S18b (2026-10-05). Only 07c and 08 in `FINAL` contain S22.
3. The S22 entry says: "etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them." The differing lines are exactly those edits, e.g. `[√bhaj + a + vant]` → `[√bhaj > bhag + a + vant]`, `(masc nom sg)` → `(adj masc nom sg)` for *anuttaro*.
4. `S22` (`FINAL/_build/s22src/`, the zip that the legacy 01–08 EPUBs and PDFs were built from) is byte-identical to `BACKUP` for all 130 texts in 01–08.
5. For 07c, 08, 09a–09e and 10, `FINAL` and `BACKUP` are identical.
6. Simsapa's DPD (checked 2026-10-22) gives *bhagavant* the construction `√bhaj > bhag + a + vant`. This is the S22 form, not the older `√bhaj + a + vant` in `FINAL`.

**Decision (maintainer, 2026-10-22).** Use the `S22` text files for 01–08 and the `BACKUP` changelogs, and record the difference here.

**Files where `FINAL` differs from the chosen version** (48 texts + 9 changelogs). The number is the count of changed lines; all are S22 alignment edits.

| Folder | File (changed lines) |
| :--- | :--- |
| 01_morning_chanting | 01_dedication_of_offerings (11), 02_preliminary_homage (2), 03_homage_to_the_buddha (4), 04_homage_to_the_dhamma (5), 05_homage_to_the_sangha (9), 06_salutation_to_the_triple_gem (5), 07_closing_homage (5), CHANGELOG |
| 02_evening_chanting | 01_dedication_of_offerings (11), 02_preliminary_homage (2), 03_recollection_of_the_buddha (4), 04_supreme_praise_of_the_buddha (2), 05_recollection_of_the_dhamma (5), 06_supreme_praise_of_the_dhamma (2), 07_recollection_of_the_sangha (9), 08_supreme_praise_of_the_sangha (2), 09_closing_homage (5), CHANGELOG |
| 03_reflections | 01_reflection_on_the_four_requisites (1), 02_five_subjects_for_frequent_recollection (2), 03_ten_subjects_for_frequent_recollection (2), 05_recollection_after_using_the_requisites (1), 07_mettapharana (2), 12_the_teaching_on_striving_according_to_dhamma (5), 18_dhamma_garav_adi_gatha (1), 19_the_teaching_on_the_noble_eightfold_path (4), CHANGELOG |
| 04a_parittas | 03_pubba_bhaga_nama_kara_patha (1), 08_mangala_sutta (4), 11_khandha_paritta (1), 13_buddha_dhamma_sangha_guna (13), CHANGELOG |
| 04b_verses_on_the_dhamma | 06_dhamma_garav_adi_gatha (1), CHANGELOG |
| 05_anumodanas | 09_maha_mangala_cakka_vala (1), CHANGELOG |
| 06_funeral_chants | 01_dhamma_sangani_matika (2), 08_patthana_matika_patha (1), 10_pamsukula (1), CHANGELOG |
| 07a_suttas | 01_dhammacakkappavattana_sutta (7), 02_anatta_lakkhana_sutta (4), 03_aditta_pariyaya_sutta (4), 05_dhaj_agga_sutta (17), 06_girimananda_sutta (6), 07_maha_samaya_sutta (20), 08_bhikkhu_aparihaniya_dhamma (14), 09_gotami_sutta (8), 10_saraniya_dhamma_sutta (6), 11_nakulapitusutta (20), 12_itivuttaka_49_ditthigatasutta (3), CHANGELOG |
| 07b_anagatabhaya_suttas | 03_tatiyaanagatabhayasutta (5), 04_catutthaanagatabhayasutta (5), 05_saddhammappatirupakasutta (4), 06_kimilasutta (4), CHANGELOG |

FR-14. The doc must give the commands to reproduce the comparison (e.g. `diff $FINAL/<f> $S22/<f>`), and the line-level "Was / Now" tables in each folder's S22 changelog entry must be named as the review list.

### 4.4 Tooling (Python scripts + Makefile)

FR-15. All tools are Python 3 scripts in `scripts/`, called by Makefile targets. They should use only the standard library (the HTTP calls to Simsapa use `urllib`), so that no Python package install is needed. If a dependency becomes necessary, it is managed with `uv` and `pyproject.toml`.

FR-16. The new scripts must be **newly written** for this repo. The legacy `chant_pipeline.py` and helpers are reference material for the logic, not code to copy. Each legacy tool gets this treatment:

| Legacy tool | What it did | Treatment |
| :--- | :--- | :--- |
| `chant_pipeline.py lint [--fix]` | Checks file layout, allowed tags, tag order, word coverage of the Pāli line, compound member rows, rubrics, stray English, NFC, niggahīta ṁ, repeat notes; safe auto-fixes | **Rewrite** as `scripts/lint.py`. Keep the mechanism of reading the rule lists (`tags`, `rubrics`, `english-stopwords`, `repeat-note`, and per-book `options`) from fenced blocks in `docs/style-spec.md`, so rules and checks never drift. |
| `chant_pipeline.py compare --ref` + `nc.py` | Compares the Pāli lines with the source text (BM, Chanting Guide, SC JSON, or Vinaya originals) after normalisation | **Rewrite** as `scripts/compare.py`; reference files from `sources/`. |
| `chant_pipeline.py index` + `xidx.py` | Cross-file index: same word with different etymology or tags | **Rewrite** as `scripts/index.py` (one tool, optional folder filter). |
| `chant_pipeline.py dupes`, `stats` | Repeated lines; counts of units and rows | **Rewrite** as subcommands of `index.py` or a small `stats.py`. |
| `chant_pipeline.py build` / `preprocess` | Turned each file into pandoc Markdown with classed divs; EPUB via pandoc; PDF via WeasyPrint; titles and About text hard-coded | **Rewrite** as `scripts/assemble.py` (see 4.5). WeasyPrint is dropped. Titles and About move to `books/`. |
| `chant_pipeline.py dpd`, `q.py`, `ec.py` | Looked up words in the local `dpd.db`; flagged rows whose root/construction/tags differ from DPD | **Replace** with `scripts/simsapa.py` using the Simsapa API (4.4.1). |
| `b.py` + `md2c.py` | Compact one-line-per-item draft format (`T\|`, `E\|`, `H\|`, `P\|`, `L\|`, `F\|`, `U\|`, `S\|`, `V\|`, `P~`, `P!`, `I\|` …) → chant file, and back | **Rewrite** as `scripts/draft.py build|extract`; format documented in `docs/drafting-workflow.md`. |
| `wr.py` | Shows the most common existing rows for a word | **Rewrite** as `scripts/index.py rows <word>`. |
| `ov.py` | Lists Pāli lines that equal an already-settled line elsewhere (to copy, not re-analyse) | **Rewrite** as `scripts/index.py overlaps <files>`. |
| `align.py` | Bulk replace in table rows by a rules JSON, with a log for the changelog | **Rewrite** as `scripts/align.py` (same rules format, documented). |
| `vchk.py`, `vchk19.py` | One-off DN 22 checks that rebuild variant lists and compare with SC JSON | **Document the method only** (`docs/style-spec.md` variant section). |
| `split.py`, `split_originals.py`, `estimate.py`, `_s0dn22/patch_pipeline.py` | One-off splitting/sizing for the DN 22 and Vinaya sub-projects | **Not migrated**; one paragraph in `docs/legacy-migration.md`. |
| `cp`, `gitc` | Wrappers for a sandbox that could not delete files | **Dropped.** |

#### 4.4.1 Simsapa API

FR-17. `scripts/simsapa.py` must read the port from `$SIMSAPA_DIR/api-port.txt` if set, else use `4848`. It must fail with a clear message ("Simsapa is not running; start the app …") when `/health` does not answer.

FR-17a. **Confirmed API format** (Simsapa 1.1.0-alpha.1, port 4848, checked 2026-10-22). The scripts rely on these fields:

| Route | Fields used |
| :--- | :--- |
| `GET /health` | `app_version`, `counts.dpd_headwords` (88 864), `fulltext.state` |
| `POST /dict_combined_search` `{"query_text": <form>}` | `results[]`: `uid` (e.g. `49140/dpd`), `title` (= DPD `lemma_1`, e.g. `bhagavant 2`), `table_name` (`dpd_headwords`; skip `bold_definitions` rows), `snippet` (HTML: `(pos)` meaning `[construction]`); top-level `deconstructor` when the form is split |
| `GET /word.json?uid=<uid>` | array of one record: `lemma_1`, `pos`, `grammar` (e.g. `adj, from bhaga`), `construction` (may hold several lines, e.g. `√bhaj > bhag + a + vant` and `bhaga + vant`), `root_key` (`√bhaj 1`), `root_sign`, `stem`, `pattern`, `meaning_1`/`meaning_2`, `meaning_lit`, `inflections` (comma list of all forms), `inflections_html` (declension or conjugation table) |
| `POST /gloss_text` `{"text": …}` | `paragraphs[].words_data[]`: `original_word`, `stem`, `direct_uids`, `results[]` (`uid`, `word`, `summary` HTML with pos, meaning, construction), `deconstructions[]` (`words_joined`, `components[].word`, `components[].result_uids`); `paragraphs[].unrecognized_words` |

Findings that shape the design:
- **Niggahīta:** Simsapa's DPD writes **ṁ** (e.g. `bhagavantaṁ` in `inflections`), the same as our files. Unlike the legacy local `dpd.db`, no ṃ→ṁ conversion is needed. The scripts still fold ṃ to ṁ to be safe.
- **Grammar labels are not automated.** Case, number, gender, person, tense, voice, mood and participle labels for a word *as it stands in the line* are not worked out by scripts (maintainer decision, 2026-10-22): this is unreliable to automate. Scripts fetch and present the DPD data (headwords, `pos`, `grammar`, `construction`, `root_key`, meanings, the raw `inflections` list and `inflections_html` table). An LLM then assigns the labels by following a local skill file (FR-20a).
- **Sandhi apostrophes:** `/gloss_text` splits words at `'`: *sabb'ītiyo* came back as *sabbi* + *tiyo*, which is wrong. Hyphens are handled (*vijjācaraṇa-sampanno* → *vijjācaraṇasampanna*). So the scripts take words from our own rows, not from Simsapa's tokens. Before calling `/gloss_text` on a raw line, they join apostrophe words (drop the `'`), and they look up a row word with `'` removed.
- **Volume:** the migrated texts have about 7,500 distinct row words. One dictionary search takes about 50 ms on this machine, so a full check costs minutes, not seconds. `simsapa.py` keeps a disk cache in `build/cache/simsapa/`, keyed by the Simsapa `app_version` from `/health`. It uses the search `snippet` (pos, meaning and construction) first, and fetches `/word.json` only when the root or full construction is needed.
- **Compounds come from DPD as Simsapa returns them.** Dictionary search returns compounds as DPD knows them: a compound headword with its `construction` (e.g. *sammāsambuddha* → `sammā + sambuddha`), or the `deconstructor` split for forms DPD has no headword for. The scripts pass these on unchanged and never split compounds by their own rules.

FR-18. `simsapa.py lookup <word>…` must print, for each word, the DPD headwords (`lemma_1`, `pos`, `grammar`, `construction`, `root_key`, meanings) and any `deconstructor` split, using `POST /dict_combined_search` and `GET /word.json?uid=` (replaces `q.py`). `--json` prints the same data as JSON for the skill (FR-20a). `--inflections` adds the plain-text `inflections_html` table.

FR-19. `simsapa.py check <files>…` must report only what can be checked mechanically (replaces `dpd` and `ec.py`):
   - the row word (or its sandhi-free form) is found in DPD, either as an inflection of some headword or through the deconstructor; words that are not found are listed;
   - the row's √root matches the `root_key` of at least one candidate headword;
   - the row's etymology matches at least one line of a candidate's `construction` (after normalising spaces and `>` notation);
   - a `comp` row's member rows match the members in DPD's `construction` or the deconstructor split.

   Rows tagged `(trad.)` or "no root in DPD", indeclinables, pronouns and the *antara-* rule follow the spec's exceptions. **Grammar tags are not checked by this script**; they are reviewed with the skill (FR-20a).

FR-20. `simsapa.py gloss <file|text>` must call `POST /gloss_text` on a Pāli line or file. For each word it prints a draft row in the compact draft format: the word, an **empty tag slot**, the candidate meanings (`meaning_1` of each direct result), etymology from `construction`, and member rows from DPD's `construction` or `deconstructions[]`. Words with several candidate headwords list all of them for the drafter to choose. This is raw material for the skill, not a finished table.

FR-20a. **Local skill for word analysis.** Provide `.claude/skills/pali-word-analysis/SKILL.md`, a Claude Code skill that an agent loads when drafting or reviewing word tables. It must:
   - tell the agent to get DPD data first (`simsapa.py gloss` for a new line, `simsapa.py lookup --json [--inflections]` for single words) and never to label a word without it;
   - explain how to read the DPD data: `pos` and `grammar`, `construction` (several lines = several analyses), `root_key`, and the `inflections_html` table (rows = case or person; columns = gender and number; cells = stem + ending) to find which cells match the surface form;
   - have the agent choose the reading that fits the line's syntax (agreement, verb mood, sandhi), and write the tags in the spec's canonical order using only allowed tokens (`docs/style-spec.md` §Tags);
   - say how to handle ambiguity (`dat/gen`), the "read as a wish" notes, compounds and member rows (from DPD only), `(trad.)`, and "no root in DPD";
   - require reuse of settled rows first (`index.py rows <word>`) so the same word is analysed the same way across files;
   - end with the checks to run (`make lint`, `simsapa.py check`) and the changelog entry.

   The skill points to `docs/style-spec.md` for the rules rather than repeating them.

FR-21. `scripts/simsapa_fmt.py` (copied from `EXERCISES`) is kept for ad-hoc agent queries with `curl`, as recommended in `docs/simsapa-localhost-api-search-endpoints.md`.

FR-22. `docs/drafting-workflow.md` must describe the full workflow for adding a new text: get the Pāli from a source (Simsapa sutta routes, BM upstream Markdown, the Community Chanting Book, or the Chanting Guide) → `simsapa.py gloss` → assign grammar labels and finish the rows with the `pali-word-analysis` skill (FR-20a) → `draft.py build` → `make lint` → `make compare` → `simsapa.py check` → `index.py overlaps` / `rows` for consistency → changelog entry → build.

#### 4.4.2 Makefile targets

FR-23. The Makefile must provide at least:

| Target | Does |
| :--- | :--- |
| `make check-tools` | Checks that pandoc, typst, python3, make, curl, git and epubcheck are installed (and their minimum versions), and whether Simsapa answers. Prints install hints for anything missing. |
| `make all` | `epub` + `pdf` for all books |
| `make epub` / `make pdf` | All books in one format |
| `make book BOOK=01_morning_chanting` | One book, both formats |
| `make lint` / `make lint-fix` | `scripts/lint.py` on all texts |
| `make compare` | Pāli check against `sources/` |
| `make index` | Cross-file consistency report |
| `make dpd-check` | `simsapa.py check` on all texts (needs Simsapa running) |
| `make fetch-sources` | Clones/updates `sources/upstream/` at the pinned commits (FR-12a) |
| `make covers` | Renders all covers (PDF page and EPUB PNG) |
| `make epubcheck` | Validates every EPUB in `build/epub/` with `epubcheck` (FR-30a) |
| `make clean` | Removes `build/` |

FR-24. Outputs go to `build/epub/<book>.epub` and `build/pdf/<book>.pdf`. Makefile dependencies must cause a book to rebuild when its texts, metadata, about, templates or fonts change.

FR-25. A build must print a warning (not fail) when lint finds errors in that book's files, as the legacy build did.

### 4.5 Book assembly, EPUB and PDF

FR-26. Each book's `metadata.txt` must contain (YAML-compatible `key: value` lines, so that pandoc can read it with `--metadata-file`):
   - `title`, `subtitle`, `lang` (`en-GB`)
   - `pali-title-first` (true for 04a and 05, following the legacy rule; otherwise the English title comes first and the Pāli title is the subtitle)
   - `texts`: the ordered list of text folders in the book, relative to the book folder (`texts`, except `09_vinaya_formulae`, which lists its five part folders `01_…` – `05_…` with BM's English part headings)
   - `sources`: attribution of the Pāli sources (Bhikkhu Manual, Reference Edition, Amaravati Publications 2020, CC BY-NC-ND 4.0; Chanting Guide, Dhammayut Order in the USA, 4th ed. 2017, CC BY-NC 4.0; SuttaCentral Mahāsaṅgīti edition, CC0; Digital Pāḷi Dictionary as reference)
   - `rights`: "English renderings CC BY-NC 4.0; Pāli text under the licences of its sources. Free distribution only." (legacy wording)
   - `cover-image`: empty by default, which means the generated cover (FR-33a) is used; a path here overrides it
   - `about`: path to the book's About file, `00_about.md`
   - `author`, `publisher`: present but **empty** (maintainer decision, 2026-10-22: avoid wrong attribution; to be filled in when needed). Pandoc writes an empty key as an empty `<dc:creator/>` / `<dc:publisher/>` (verified with pandoc 3.8.3). So `assemble.py` drops keys with empty values from the metadata it passes to pandoc (FR-30).

FR-27. Initial metadata values must come from the legacy material:

| Book | Title | Subtitle |
| :--- | :--- | :--- |
| 01 | Morning Chanting | Pubbaṇha-vandanā |
| 02 | Evening Chanting | Sāyaṇha-vandanā |
| 03 | Reflections | Paccavekkhaṇa-pāṭha |
| 04a | Paritta | Protective Chants |
| 04b | Verses on the Dhamma | Dhamma-gāthā |
| 05 | Anumodanā | Blessings and Rejoicing in Merit |
| 06 | Funeral Chants | Matakicca-pāṭha |
| 07a | Suttas | Sutta-pāṭha |
| 07b | Discourses on Future Dangers | Anāgatabhaya-sutta |
| 07c | Conditions of Non-decline for Bhikkhus | Bhikkhu-aparihāniya-dhamma |
| 08 | Pāṭimokkha Chants | Pāṭimokkha-pāṭha |
| 09 | Vinaya Formulae | Vinaya-pāṭha |
| 10 | The Great Discourse on the Establishments of Mindfulness | Mahāsatipaṭṭhānasutta |

FR-28. Each `00_about.md` must be created from the legacy About text: the `ABOUT` template plus the `DRAFTING` and `REVIEW` paragraphs in `chant_pipeline.py` for 01–08, the DN 22 About (`_tools/dn22/about-dn22.md`) for 10, and the Vinaya equivalent for 09. Placeholders (`{what}`, `{drafting}`, `{review}`) are filled in, so that each file is plain Markdown. The build date (`{today}`) is inserted at build time. The AI-disclosure wording must be kept.

FR-29. `scripts/assemble.py <book>` must read the book's metadata, concatenate its texts (`NN_*.md` in name order, never `CHANGELOG.md`), and write one pandoc-Markdown file to `build/tmp/<book>.md`. Each element is wrapped in a classed fenced div, as in the legacy `preprocess()`: `pali` (with `lang="pi"`), `literal`, `faithful`, `unit`, `repeat`, `citation`, `rubric`, `subtitle`, and for 09/10 `instruction`, `variant`, `gloss`. The English title is added to the table-of-contents entry (`.toc-en` span), as before.

FR-30. EPUB: `pandoc build/tmp/<book>.md --metadata-file build/tmp/<book>.meta.json -o build/epub/<book>.epub` (the `meta.json` is written by `assemble.py` from `metadata.txt`, with the title order applied and empty keys dropped) with `--toc --toc-depth=1 --split-level=1`, `templates/epub.css`, the embedded fonts, and `--epub-cover-image` set to the generated cover PNG (or the override).

FR-30a. **EPUB validation.** Every generated EPUB must be validated with `epubcheck`. The EPUB build rule runs `epubcheck` on each file right after pandoc writes it; any fatal or error fails the rule and removes the invalid EPUB, so that Make does not treat it as up to date. Warnings are printed but do not fail the build. `make epubcheck` re-validates all built EPUBs.

FR-31. PDF: pandoc converts the same assembled Markdown to typst (`-t typst`) with a template in `templates/pandoc/`, plus a Lua filter that maps the classed divs to typst functions defined in `templates/typst/`. Then `typst compile --font-path fonts/ --ignore-system-fonts` writes the PDF. Pandoc's own typst output was checked: it drops div classes (each div becomes a plain `#block[…]`), turns `lang="pi"` into `#set text(lang: "pi")`, wraps tables in `#figure(align(center)[#table(…)])` with a `table.header`, and writes the backticked word and tag cells as typst raw text, which prints in a monospace font. So the Lua filter must (a) map classes to functions, (b) unwrap tables from `figure` into the word-table function, and (c) turn `Code` inlines into styled text (word: bold serif; tags: small sans). The legacy EPUB CSS handled (c) with `code { font-family: inherit; … }`; keep that in `epub.css`.

FR-32. PDF layout (typst):
   - A5 paper.
   - Body font Crimson; table/label font Noto Sans (both from `EXERCISES`).
   - Order per unit: bold Pāli line → Literal → Faithful → word table, as in the legacy books.
   - Improvements: a unit's Pāli line and renderings must not be separated from the start of its table at a page break; tables that do break repeat their header row; running headers show the book and chant title; page numbers; a contents page with Pāli and English titles; the About page before the texts.
   - The `↳` member-row marker must render. Neither Crimson, Noto Sans nor the Libertinus text fonts contain `↳` (U+21B3; checked with `fc-query`). **Noto Sans Math** (`NotoSansMath-Regular.ttf`, which has it) is the fallback (maintainer decision, 2026-10-22). In typst, every font list that may set a member row ends with `"Noto Sans Math"`, e.g. `("Noto Sans", "Noto Sans Math")`, so only glyphs missing from the main font fall through. In the EPUB, Noto Sans Math is embedded and listed last in the CSS `font-family` for table cells. Noto Sans Math has only a regular weight, so a `↳` in a bold cell will be synthetically emboldened or appear regular; this is acceptable.

FR-33. `templates/typst/style.typ` is adapted from `EXERCISES/exercises/style.typ`: keep its structure for fonts, sizes, page and headings; drop the exercise-specific parts (language strings, answer keys).

FR-33a. **Generated covers.** `templates/typst/cover.typ` makes a simple, typographic cover for each book from its `metadata.txt`: title, subtitle (Pāli or English, following `pali-title-first`), a short series line (e.g. "Pāli with word-by-word English"), and a plain rule or ornament. No images are needed. All covers share one design and differ only in text (an optional per-book accent colour in `metadata.txt` is allowed). Fonts are Crimson and Noto Sans.
   - PDF: the cover is page 1 of the A5 PDF, followed by a blank verso.
   - EPUB: `typst compile --format png --ppi 300` renders the same cover to `build/covers/<book>.png` (A5 proportions, at least 1400 px wide), which is passed to pandoc.
   - The cover is a Makefile dependency of both formats, so editing the metadata rebuilds it.

### 4.6 Documentation

FR-34. `docs/style-spec.md` must re-state, in this repo's own words, the rules from the legacy `style-spec.md` (main, DN 22 and Vinaya variants), organised as:
   1. File layout (title, English title, Pāli `###` headings only, Literal/Faithful with two trailing spaces, citation placement, no `---`).
   2. The Pāli line: source priority (BM → Chanting Guide → SuttaCentral; DN 22 = SuttaCentral only; Vinaya = BM only), ṁ niggahīta, ASCII `'`, leader brackets removed, `(×3)`, slash alternatives, `…pe…` written out, nothing else in the line.
   3. Literal and Faithful lines: word order, square brackets for added words, mood must be rendered, the "read as a wish" rules, British spelling, consistent key terms, **never copy BM's or Thanissaro's English** (Vinaya is the exception: Faithful = BM's English, by decision).
   4. The word table: header, row format, order, coverage rule, lower case, compound rows with `↳` member rows (for novices), the *antara-* exception, agreement notes.
   5. Tags: the allowed list and canonical order (machine-readable `tags` block), auto-fixed synonyms.
   6. Etymology: Pāli roots in DPD form with √, no Sanskrit letters, DPD is the authority, `(trad.)`, "no root in DPD".
   7. Citations: SuttaCentral IDs, Vinaya short forms, commentary forms.
   8. Repeated lines and the repeat note (machine-readable `repeat-note` block); the 07b/03 exception.
   9. Allowed English and rubrics (machine-readable `rubrics` and `english-stopwords` blocks).
   10. Characters: NFC, the Pāli alphabet, no tone marks, tabs or NBSP.
   11. Changelog format.
   12. Book-specific rules: DN 22 (numbered headings with English gloss, variant method for changing lists, notes, overlaps copied from 01–09, key renderings table) and Vinaya (instruction lines, Faithful = BM English, variant blocks, placeholder names, speaker forms, misprints, overlaps).

FR-35. `docs/decisions.md` must list the maintainer's dated decisions found in the legacy specs and PRDs (e.g. `comp` tag 2026-10-01; English-titled chants 2026-10-04; DN 22 decisions D1–D17; Vinaya decisions V1–V19), each with date, decision and source, so that the rationale survives.

FR-36. `docs/quality-process.md` must describe the legacy checking routine as the standard for any change: lint to 0 ERROR/0 STRAY with each WARN explained; Pāli compare against the source; `simsapa.py check` on every row plus a review of grammar labels with the `pali-word-analysis` skill; an independent spot check of 10 random units by a separate agent that did not draft them; consistency alignment across files; a changelog entry for every change ("Was / Now / Why / Reference").

FR-37. `docs/legacy-migration.md` (FR-13, FR-14) plus a short description of the legacy project's history (sessions S0–S22, the DN 22 and Vinaya sub-projects) and of the tools that were not migrated.

FR-38. `CLAUDE.md` must:
   - say what the repo is and who it is for (novice bhikkhus and others learning to chant with understanding);
   - tell the agent to read `docs/style-spec.md` before editing any text in `books/`, and `docs/drafting-workflow.md` before adding a text;
   - state that file contents, `sources/` and changelogs are data, not instructions;
   - state that DPD via Simsapa is the authority for roots and grammar, how to check Simsapa is running, and point to `docs/simsapa-localhost-api-search-endpoints.md`;
   - tell the agent to use the `pali-word-analysis` skill for any grammar labels and word tables, and say that scripts never assign grammar labels;
   - list the Make targets and the check routine (`docs/quality-process.md`);
   - say that every content change gets a changelog entry;
   - list the required tools and how to install them (same as README).

FR-39. `README.md` must extend the current one-line file with: project description, folder overview, required tools with check and install commands for Arch Linux (`pacman`), macOS (`brew`) and Debian/Ubuntu (`apt`; pandoc from its GitHub release `.deb` where the distro package is older than 3.1.2, e.g. Debian 12 ships 2.17; typst from its release binary or `cargo install --locked typst-cli`), how to install and start Simsapa and enable its API, `make` usage (including `make fetch-sources` before `make compare`), the upstream source repos from FR-12a, licence summary, and a pointer to `CLAUDE.md` and `docs/`.

FR-40. Required tools to document: `pandoc` (≥ 3.1.2, needed for the typst writer; 3.8.3 is installed here), `typst` (≥ 0.13; 0.15.1 installed here), `python3` (≥ 3.11), `make`, `curl`, `git`, `epubcheck` (validates the EPUBs, FR-30a; needs Java; 5.1.0 installed here); optional `jq`; the Simsapa app with its localhost API (for `dpd-check`, `lookup` and `gloss` only; builds do not need it).

## 5. Non-Goals (Out of Scope)

- Changing the content of any text (renderings, analyses, Pāli). Migration is byte-for-byte.
- A separate review of the 48 S22-affected files (maintainer decision, 2026-10-22: not needed now). They stay listed in `docs/legacy-migration.md`.
- Using the Community Chanting Book in any check (only recorded and fetched for now).
- Assigning grammar labels (case, number, gender, person, tense, voice, mood) with scripts, or splitting compounds with our own rules. Labels are LLM work guided by the skill (FR-20a), and compounds come from DPD via Simsapa.
- Committing the Ṭhānissaro *Chanting Guide* (only its locations are recorded).
- Keeping the legacy git history (decision: start fresh with one import commit).
- Migrating legacy built EPUBs/PDFs, drafts (`_tools/drafts/*.c`), scratch folders, or the local `dpd.db`.
- WeasyPrint or LaTeX PDF builds.
- A4 PDFs (A5 only).
- Running the Simsapa AI "word selection" WebSocket (`/word_selection_ws`); only the synchronous `/gloss_text` is used.
- A website or HTML output.
- Adding new suttas (the workflow is documented, but no new texts are drafted in this feature).

## 6. Design Considerations

- Book look: follow the legacy books (`FINAL/_build/*.pdf`, `*.epub`) for content order and hierarchy. Those files can be opened for visual comparison from the legacy folder; they are not copied.
- The legacy `style.css` (64 lines) gives the class names and the EPUB look to start from. It hides the English part of the title in headings while keeping it in the table of contents (`.toc-en`).
- Word tables in A5 are narrow: the Word column should size to its content and the Analysis column should wrap. Use Noto Sans at a smaller size for tags.
- Pāli lines are bold. Literal and Faithful labels are bold, followed by plain text.

## 7. Technical Considerations

- **One parser, two outputs.** `assemble.py` parses each text once and emits pandoc Markdown with classed divs. EPUB and PDF both start from that file, so the two formats cannot drift apart.
- **One spec is enough.** The legacy main, Vinaya and DN 22 specs have identical `tags`, `english-stopwords` and `repeat-note` blocks. The Vinaya `rubrics` block is also identical, and DN 22's is empty, which is harmless because DN 22 files have no rubrics. So one `docs/style-spec.md` serves all books. Book 10's behaviour comes from its `options` (from the DN 22 spec's `options` block).
- **Spec-driven checks.** `lint.py` reads its rule lists from fenced code blocks in `docs/style-spec.md`, as the legacy script did. Per-book behaviour (DN 22 heading numbers and glosses, cross-file repeats, variants) comes from an `options` block, or from the book's `metadata.txt`.
- **Parsing rules** (from the legacy parser): title `# …`; English title `*…*` on the next line; `### ` Pāli heading; `**Pāli**` line; `**Literal:**`/`**Faithful:**`; table rows `| **`word`** | `(tags)` meaning; **[etym]** |`; member rows starting `| ↳ `; the repeat note in italics; citation `*SC-ID*`; rubrics `*(…)*`; Vinaya instruction lines `> …`; `**Variant:** …` cues.
- **Simsapa.** The API is bound to `127.0.0.1`. The port is in `<SIMSAPA_DIR>/api-port.txt` (default 4848). Use the `uid` from search results rather than building uids. `/word.json?uid=` is the safe route for uids containing `/`. A miss is HTTP 404. Fulltext sutta search ignores diacritics, so check hits by fetching the text.
- **DPD notation.** Simsapa's DPD uses ṁ like our files (FR-17a). DPD marks *antara-* words as compounds; the spec overrides this. A DPD `construction` may list several analyses (one per line), and a row matches if it agrees with any of them.
- **Fonts.** Crimson, Noto Sans and Noto Sans Math are all SIL OFL (Noto Sans includes `OFL.txt`; confirm Crimson's and Noto Sans Math's licence files are copied with them). Embedding them in the EPUB is allowed.
- **Shell.** The user's interactive shell is fish, but the migration script is bash with `#!/usr/bin/env bash` and `set -euo pipefail`.
- **Typst version drift.** Pin the minimum typst version in `check-tools`. The template should avoid features newer than that version.

## 8. Success Metrics

1. `scripts/migrate-legacy.sh` runs cleanly on a fresh checkout (met by the one-time run of 2026-10-22; not expected to hold after later changes). Its manifest lists 209 texts + 17 changelogs in `texts/` and the 6 `00_original_*` files in `sources/originals/`. Its verification step reports 130/130 identical (S22 vs BACKUP) and all-identical for 07c–10.
2. `make all` builds 13 EPUBs and 13 PDFs, each with its generated cover, without errors on this machine.
3. `make lint` on the migrated texts reports the same result as the legacy final state. Running the legacy linter on a scratch copy of `BACKUP` (2026-10-22) gave 0 ERROR and 0 STRAY, with 4 WARN for 01–08 (main spec), 18 WARN for 09a–09e (Vinaya spec) and 0 WARN for 10 (DN 22 spec). The new lint should reproduce these counts, or explain any difference.
4. `epubcheck` reports 0 fatals and 0 errors on every EPUB (FR-30a); any remaining warnings are listed.
5. Each EPUB's metadata (title, subtitle, language, rights, sources) matches its `metadata.txt`.
6. Spot comparison of three PDFs (01, 07a, 10) against the legacy PDFs shows the same content in the same order, with no missing glyphs (`↳`, √, ṁ, ṭ, ḷ).
7. `make dpd-check` runs against Simsapa on all migrated texts. Every flag it raises (word not found, root or construction mismatch, compound members) is either explained or listed for review.
8. Using the skill, an agent drafts the table for one line of a sutta not in the repo, and the result passes `make lint` and `simsapa.py check`.
9. A fresh agent session, given only `CLAUDE.md`, finds the style spec and runs the check routine without further instructions.

## 9. Open Questions

None at present. All earlier questions were answered by the maintainer on 2026-10-22 and are recorded in the requirements above.
