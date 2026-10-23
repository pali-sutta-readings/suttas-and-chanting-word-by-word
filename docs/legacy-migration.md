# Legacy migration

The texts in this repo were made in an earlier, agent-driven project ("the legacy project"). Its working folder was deleted; what remains are two snapshots copied over from a Mac. This document records where each migrated file came from, why one version was chosen where the snapshots disagree, what the legacy project was, and which of its tools were not carried over.

The copy was a **one-time operation**. `scripts/migrate-legacy.sh` ran once, on 2026-10-22 (commit `9a2cbb9`), and wrote `sources/MIGRATION-MANIFEST.tsv`. Both are kept as a record of that run and are not maintained. The content and the folder layout have changed since (see "Where the texts are now" below), so the script is not expected to work on this repo again, and nothing tests it.

## The snapshots

| Name | Path |
| :--- | :--- |
| `LEGACY` | `~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs` |
| `FINAL` | `$LEGACY/final-build-files/Pali-translations-formatted-md-files` |
| `S22` | `$FINAL/_build/s22src` (the source the legacy 01–08 books were built from) |
| `BACKUP` | `$LEGACY/last-backup/Pali-translations-formatted-md-files` (Time Machine snapshot; a clean git repo, 49 commits) |
| `EXERCISES` | `~/prods/sites/pali-sutta-readings-project/pali-exercises` (typst style, fonts, `simsapa_fmt.py`) |

## What was copied from where

| What | From | To |
| :--- | :--- | :--- |
| 01–08 texts (`NN_*.md`, 130 files) | `S22/<folder>/` | `texts/<folder>/` |
| 01–08 `CHANGELOG.md` (11 files) | `BACKUP/<folder>/` | `texts/<folder>/` |
| 09a–09e and 10 texts (79 files) and changelogs (6 files) | `FINAL/<folder>/` | `texts/<folder>/` |
| `00_original_*` (6 files) | `FINAL/<folder>/` | `sources/originals/<folder>/` |
| `reference-pali-supplement.md` | `BACKUP/_tools/refs/` | `sources/` |
| `dn22_root-pli-ms.json`, `dn22_variant-pli-ms.json` | `BACKUP/_tools/refs/` | `sources/suttacentral/` |
| `style.css` | `BACKUP/_tools/` | `templates/epub.css` |
| Crimson, Noto Sans | `EXERCISES/fonts/` | `fonts/` |
| `NotoSansMath-Regular.ttf` | `/usr/share/fonts/noto/` (Arch `noto-fonts`; `$NOTO_MATH` overrides) | `fonts/Noto_Sans_Math/` |
| `style.typ` | `EXERCISES/exercises/` | `templates/typst/` |
| `simsapa_fmt.py` | `EXERCISES/scripts/` | `scripts/` |

The "To" column is where the run put each file. The texts went into a top-level `texts/` folder, one subfolder per legacy folder, with the legacy names.

### Where the texts are now

On 2026-10-23 (maintainer decision) the texts moved into their book folders under `books/`, so that a book's metadata, About text and texts live in one place. File names were kept and the files were moved, not edited:

| Legacy folder (short ID) | Folder in this repo |
| :--- | :--- |
| `01_morning_chanting` … `08_patimokkha_chants` (01 … 08) | `books/<same name>/texts/` |
| `09a_vinaya_notes_requisites` (09a) | `books/09_vinaya_formulae/01_vinaya_notes_requisites/` |
| `09b_vinaya_notes_rains_and_kathina` (09b) | `books/09_vinaya_formulae/02_vinaya_notes_rains_and_kathina/` |
| `09c_vinaya_notes_other_procedures` (09c) | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/` |
| `09d_vinaya_notes_offences` (09d) | `books/09_vinaya_formulae/04_vinaya_notes_offences/` |
| `09e_vinaya_notes_uposatha` (09e) | `books/09_vinaya_formulae/05_vinaya_notes_uposatha/` |
| `10_Mahasatipatthanasutta` (10) | `books/10_mahasatipatthanasutta/texts/` |

The changelogs and docs cite texts by the legacy short ID (07a/04, 09c/06); this table resolves them, and changelog line numbers still hold. The manifest's `dest` column keeps the paths of the migration run (`texts/<legacy folder>/…`); this table maps them to the current folders. `sources/originals/` keeps the legacy folder names, because those files are sources and are never built.

Later edits are not in the manifest either: `templates/epub.css` and `templates/typst/style.typ` have been adapted since, so their hashes no longer match.

Two licence files were added by hand, because neither source folder has them:

- `fonts/Crimson/OFL.txt` is `LICENSE.txt` from the Crimson repository, <https://github.com/skosch/Crimson>, commit `685b5a2478a7213a806e9bbf1e36f6a9e7f5c7ef`.
- `fonts/Noto_Sans_Math/OFL.txt` is `OFL.txt` from <https://github.com/notofonts/math>, commit `6764bbdf67f2f94b26e2705c7c6e124efa2816f3`. (Arch's `/usr/share/licenses/noto-fonts/LICENSE` is the Apache licence of the packaging, not the font licence.)

Both are the SIL Open Font License 1.1, which allows embedding the fonts in the books.

Not copied: macOS junk (`._*`, `.DS_Store`, `__pycache__/`, `*.pyc`); the legacy `_build/` outputs; `_dpd/` (the 2.3 GB DPD SQLite database, replaced by Simsapa); the scratch folders `_s0dn22/`, `_s2tmp/`, `_s3tmp/`, `_s8tmp/`, `_to_delete/`; `_tools/drafts/`; the legacy `.git/`; the legacy specs, PRDs, guides, checkpoints and scripts (their content is re-documented in `docs/`). Of `_tools/refs/`:

- `Bhikkhu-Manual-Reference.md` is not copied. It was converted to Markdown from the HTML of the *Bhikkhu Manual* EPUB. BM's own Markdown is now available upstream (<https://github.com/bhikkhu-manual/bhikkhu-manual>, `manuscript/markdown/`), fetched by `make fetch-sources`, and `compare` reads that instead.
- `ChantingGuide_Thanissaro.md` is not committed (maintainer decision, 2026-10-22). `sources/UPSTREAM.txt` records where the *Chanting Guide* can be found.

### The manifest

`sources/MIGRATION-MANIFEST.tsv` has one row per copied file, sorted by destination. It records the run of 2026-10-22 and is not updated when files move or change:

| Column | Meaning |
| :--- | :--- |
| `dest` | path in this repo |
| `snapshot` | `S22`, `FINAL`, `BACKUP`, `EXERCISES`, or `SYSTEM` (the Noto Sans Math font) |
| `source` | path relative to that snapshot's root (absolute for `SYSTEM`) |
| `sha256` | SHA-256 of the file |
| `differs_from_final` | `yes` / `no` for texts, changelogs and originals; `n/a` for files that have no copy in `FINAL` |
| `changed_lines_vs_final` | the number of `>` lines in `diff FINAL/<file> <chosen source>` (0 when identical) |

### The run

The script was run as `scripts/migrate-legacy.sh` with the default `LEGACY` path. It verified the snapshots before copying anything (below) and would have stopped if a check failed. It refused to overwrite a destination file that differed from its source unless given `--force`. During development it was tested with a script that ran it into a temporary folder; that test was removed once the migration was done.

The run, on 2026-10-22, reported:

- S22 vs BACKUP (01–08 texts): 130/130 identical.
- FINAL vs BACKUP (07c, 08, 09a–09e, 10; every file, including changelogs and originals): 105/105 identical.
- 209 texts, 17 changelogs and 6 originals; 250 manifest rows; 383 macOS junk files skipped.
- 57 files where `FINAL` differs from the chosen source: 48 texts and 9 changelogs (listed below).

## Version conflict: S22 and BACKUP over FINAL

### Finding

The maintainer's first instruction was that `FINAL` supersedes `BACKUP`. But for folders 01–07b, `FINAL`'s files are *older* than both `BACKUP` and `S22`.

### Evidence

1. `BACKUP` is a git repository whose working tree is clean (no uncommitted changes). Its HEAD is commit `94cb57e` ("S8 (DN 22): final unit …", 2026-10-13), the last commit of the whole project.
2. Every `CHANGELOG.md` in `BACKUP` for 01–08 starts with **"2026-10-11 — session S22 (final: whole-tree index alignment)"**. In `FINAL`, the 01–07b changelogs stop at S19c, S20 or S18b (2026-10-05). Only 07c and 08 in `FINAL` contain S22.
3. The S22 entry says: "etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them." The differing lines are exactly those edits, e.g. `[√bhaj + a + vant]` → `[√bhaj > bhag + a + vant]`, `(masc nom sg)` → `(adj masc nom sg)` for *anuttaro*.
4. `S22` (`FINAL/_build/s22src/`, the zip that the legacy 01–08 EPUBs and PDFs were built from) is byte-identical to `BACKUP` for all 130 texts in 01–08.
5. For 07c, 08, 09a–09e and 10, `FINAL` and `BACKUP` are identical.
6. Simsapa's DPD (checked 2026-10-22) gives *bhagavant* the construction `√bhaj > bhag + a + vant`. This is the S22 form, not the older `√bhaj + a + vant` in `FINAL`.

### Decision

Maintainer, 2026-10-22: use the `S22` text files for 01–08 and the `BACKUP` changelogs, and record the difference here. A separate review of the affected files is not needed now; they stay listed below.

### Files where FINAL differs from the chosen version

48 texts and 9 changelogs, taken from the manifest (`differs_from_final = yes`). The number is `changed_lines_vs_final`. For texts, all changes are S22 alignment edits. For changelogs, the count is larger because the `FINAL` copies also lack the entries between their last session (S18b–S20) and S22.

| Folder | File (changed lines) |
| :--- | :--- |
| 01_morning_chanting | 01_dedication_of_offerings (11), 02_preliminary_homage (2), 03_homage_to_the_buddha (4), 04_homage_to_the_dhamma (5), 05_homage_to_the_sangha (9), 06_salutation_to_the_triple_gem (5), 07_closing_homage (5), CHANGELOG (62) |
| 02_evening_chanting | 01_dedication_of_offerings (11), 02_preliminary_homage (2), 03_recollection_of_the_buddha (4), 04_supreme_praise_of_the_buddha (2), 05_recollection_of_the_dhamma (5), 06_supreme_praise_of_the_dhamma (2), 07_recollection_of_the_sangha (9), 08_supreme_praise_of_the_sangha (2), 09_closing_homage (5), CHANGELOG (71) |
| 03_reflections | 01_reflection_on_the_four_requisites (1), 02_five_subjects_for_frequent_recollection (2), 03_ten_subjects_for_frequent_recollection (2), 05_recollection_after_using_the_requisites (1), 07_mettapharana (2), 12_the_teaching_on_striving_according_to_dhamma (5), 18_dhamma_garav_adi_gatha (1), 19_the_teaching_on_the_noble_eightfold_path (4), CHANGELOG (54) |
| 04a_parittas | 03_pubba_bhaga_nama_kara_patha (1), 08_mangala_sutta (4), 11_khandha_paritta (1), 13_buddha_dhamma_sangha_guna (13), CHANGELOG (34) |
| 04b_verses_on_the_dhamma | 06_dhamma_garav_adi_gatha (1), CHANGELOG (10) |
| 05_anumodanas | 09_maha_mangala_cakka_vala (1), CHANGELOG (10) |
| 06_funeral_chants | 01_dhamma_sangani_matika (2), 08_patthana_matika_patha (1), 10_pamsukula (1), CHANGELOG (22) |
| 07a_suttas | 01_dhammacakkappavattana_sutta (7), 02_anatta_lakkhana_sutta (4), 03_aditta_pariyaya_sutta (4), 05_dhaj_agga_sutta (17), 06_girimananda_sutta (6), 07_maha_samaya_sutta (20), 08_bhikkhu_aparihaniya_dhamma (14), 09_gotami_sutta (8), 10_saraniya_dhamma_sutta (6), 11_nakulapitusutta (20), 12_itivuttaka_49_ditthigatasutta (3), CHANGELOG (95) |
| 07b_anagatabhaya_suttas | 03_tatiyaanagatabhayasutta (5), 04_catutthaanagatabhayasutta (5), 05_saddhammappatirupakasutta (4), 06_kimilasutta (4), CHANGELOG (29) |

To list them again from the manifest:

```sh
awk -F'\t' '$5 == "yes" {print $1, $6}' sources/MIGRATION-MANIFEST.tsv
```

### Reproducing the comparison

With the snapshot paths set as above (bash):

```sh
LEGACY=~/prods/sites/pali-sutta-readings-project/suttas-and-chanting-word-by-word_docs
FINAL=$LEGACY/final-build-files/Pali-translations-formatted-md-files
S22=$FINAL/_build/s22src
BACKUP=$LEGACY/last-backup/Pali-translations-formatted-md-files

# One file: what S22 changed relative to FINAL.
diff $FINAL/01_morning_chanting/01_dedication_of_offerings.md \
     $S22/01_morning_chanting/01_dedication_of_offerings.md

# All 01–08 texts: S22 vs BACKUP (expect no output), then S22 vs FINAL.
for f in $S22/0*/[0-9]*.md; do cmp -s $f $BACKUP/${f#$S22/} || echo "differs: ${f#$S22/}"; done
for f in $S22/0*/[0-9]*.md; do cmp -s $f $FINAL/${f#$S22/} || echo "${f#$S22/} $(diff $FINAL/${f#$S22/} $f | grep -c '^>')"; done

# The S22 entry in a changelog, and the last session FINAL knows about.
grep -m1 '^## ' $BACKUP/01_morning_chanting/CHANGELOG.md
grep -m1 '^## ' $FINAL/01_morning_chanting/CHANGELOG.md

# BACKUP's last commit.
git -C $BACKUP log -1 --format='%h %ad %s' --date=short
```

### Review list

The line-level record of every S22 change is the **"2026-10-11 — session S22 (final: whole-tree index alignment)"** entry at the top of each 01–08 changelog (`books/<book>/texts/CHANGELOG.md`). Under one `###` heading per file, its "Line / Was / Now / Why / Reference" table gives each changed row (e.g. *bhagavā* `√bhaj + a + vant` → `√bhaj > bhag + a + vant`, "DPD construction of bhagavant"). If the 48 files are ever reviewed, that table is the list to work through; line numbers refer to the files as migrated, and later edits to a file may shift them.

## History of the legacy project

The legacy project ran from 2026-10-01 to 2026-10-13, in numbered agent sessions guided by a style spec, a PRD and a checkpoint file, with the maintainer (a bhikkhu) answering numbered queries between sessions. Each session drafted or redrafted a set of files, ran lint, a Pāli comparison with the source, a DPD check of every row and an independent 10-unit spot check, then aligned rows across files with the cross-file index ("step 9") and logged every change in the folder's changelog.

**Main chant books, 01–08 (sessions S1–S22).** Session dates and scopes, from the changelogs:

| Session | Date | Scope |
| :--- | :--- | :--- |
| S1 | 2026-10-01 | 01 Morning Chanting; second pass for compound member rows |
| S2 | 2026-10-04 | 02 Evening Chanting |
| S3–S4 | 2026-10-04 | 03 Reflections (01–11, 12–21); queries 13–22 |
| S5–S7 | 2026-10-04 | 04a Parittas (01–10, 11–26, 27); queries 23–25 |
| S8 | 2026-10-04 | 04b Verses on the Dhamma; queries 33–37 |
| S9a–S9b | 2026-10-04 | 05 Anumodanā |
| S10–S11 | 2026-10-04 | 06 Funeral Chants |
| S12–S18b | 2026-10-04/05 | 07a Suttas, one or a few suttas per session |
| S19a–S19c | 2026-10-05 | 07b Anāgatabhaya suttas, redrafted from AN 5.77–5.80, SN 16.13, AN 7.59 |
| S20 | 2026-10-05 | 07c, redrafted from DN 16:1.6–1.12 |
| S21 | 2026-10-11 | 08 Pāṭimokkha chants, redrafted from BM 8.1–8.5; queries 58–60 |
| S22 | 2026-10-11 | final whole-tree index alignment (301 rows in 11 folders); About text |

Maintainer queries were numbered 1–60 across these sessions (e.g. query 56: an identical line with different grammar keeps a full table; query 57: *antara-* words stay single rows). They are collected in `docs/decisions.md`.

**Vinaya sub-project, 09a–09e (sessions S0–S5, 2026-10-12).** Word-by-word versions of the Vinaya formulae in the *Bhikkhu Manual*. S0 split BM's five Vinaya sections into 60 raw per-procedure files (originals kept as `00_original_*`) and extended the spec with instruction lines and variant blocks; S1 drafted the 09a pilot; S2–S4 drafted 09b, 09c, 09d and 09e; S5 ran the whole-tree index and built the combined *Vinaya Formulae* book. Maintainer decisions V1–V19.

**DN 22 sub-project, 10 (sessions S0–S8, 2026-10-12/13).** The *Mahāsatipaṭṭhānasutta* from SuttaCentral's Mahāsaṅgīti edition, as a study text for novices. S0 split the SC text into 19 section files, checked it against SC's bilara root JSON, and added spec `options` (heading numbers and glosses, cross-file repeats, DPD on variant rows); S1 was the pilot (01–02); S2–S7 drafted 03–19, using the variant method for lists that change and copying units already settled in 01–09; S8 ran the final index and built the book. Maintainer decisions D1–D17.

The legacy git history (`BACKUP/.git`) starts at "Baseline before S19a" (2026-10-05); sessions S1–S18b are known only from the changelogs. This repo starts with a fresh history (one import commit).

## Legacy tools that were not migrated

The legacy pipeline (`_tools/chant_pipeline.py` and `_tools/helpers/`) is reference material only; this repo's tools in `scripts/` are new code. These legacy tools have no counterpart:

- **`split.py`, `split_originals.py`, `estimate.py`, `_s0dn22/patch_pipeline.py`**: one-off scripts from the S0 sessions of the DN 22 and Vinaya sub-projects. They split the source texts into per-section or per-procedure raw files, estimated session sizes, and patched the pipeline. Their work is done and is recorded in the changelogs.
- **`vchk.py`, `vchk19.py`**: one-off DN 22 checks that rebuilt each variant's full Pāli list and compared it with the SC JSON. The method is described in `docs/style-spec.md` (variant section); the scripts are not kept.
- **`cp`, `gitc`**: wrappers for the legacy agent sandbox, which could not delete files or run git normally. Not needed.
- **`chant_pipeline.py dpd`, `q.py`, `ec.py`** and the local `dpd.db`: replaced by `scripts/simsapa.py`, which uses the Simsapa app's localhost API.
- **WeasyPrint PDF build**: replaced by typst.

## Lint baseline

`make lint` on the migrated texts (2026-10-22) gives **0 ERROR, 0 STRAY, 23 WARN** over 209 files.

The legacy linter (`BACKUP/_tools/chant_pipeline.py lint`, run on a scratch copy of `BACKUP` with each of its three specs) gives 0 ERROR, 0 STRAY and 22 WARN: 4 for 01–08, 18 for 09a–09e and 0 for 10. `scripts/lint.py` reports the same 22 WARNs, on the same lines, with the same messages. Each was left on purpose and is explained in the folder's changelog:

| File:line | WARN | Why it is kept |
| :--- | :--- | :--- |
| 06/01:55 | compound `vipāka` needs member rows | stem form of one member of the canonical compound *nevavipākanavipākadhammadhammā*, written apart; S11 note in `books/06_funeral_chants/texts/CHANGELOG.md` |
| 07a/02:913, 1236 | repeat of lines 792, 1112 written out in full | *Aniccā bhante* and *ajjhattā vā bahiddhā vā …* for *saṅkhārā* (masc pl) repeat the lines for *vedanā* (fem sg), so they keep their own tables (style spec §8, query 56) |
| 07b/03:818 | repeat of line 750 written out in full | *okkamane pubbaṅgamā …*: masc nom pl, then fem nom sg agreeing with *janatā* (query 56) |
| 09c/10:245–311 (5), 09c/11:245–367 (8) | compound `veramaṇī` needs member rows | first member of *veramaṇī-sikkhāpadaṁ*, which BM writes apart (style spec §12.1, "written apart") |
| 09c/11:537, 538 | compounds `uposatha`, `sīla` need member rows | members of *uposatha-sīla-vasena*, written apart by BM |
| 09e/02:42 | compound `pārisuddhi` needs member rows | written apart by BM; compound with *uposathaṁ* |
| 09d/01:223 | BM-style citation *Vin.IV.122* | kept by decision V15 |
| 09e/01:22 | BM-style citation *Vin.I.120-129* | kept by decision V16 |

`scripts/lint.py` also has checks the legacy linter did not have: canonical tag order (style spec §5), the two trailing spaces after Literal, Faithful and Variant lines (§1, §12.1), letters outside the Pāli alphabet in Pāli lines and row words (§10), and non-breaking spaces (§10). The book 10 options (§12.2) come from `books/10_mahasatipatthanasutta/metadata.txt` instead of a separate spec.

### Open lint findings

The new checks found one problem. It is listed here; the text is not changed in this migration.

| File:line | WARN | Note |
| :--- | :--- | :--- |
| `books/09_vinaya_formulae/05_vinaya_notes_uposatha/05_sick_parisuddhi.md:67` | variant line does not end with two spaces | The cue *Āyasmā bhante uttaro bhikkhu* → *Uttaro bhante bhikkhu* (decision V18) lacks the two trailing spaces that §12.1 asks for. A blank line follows it, so the built book is not affected. The fix is to add the two spaces and log it in the changelog. |
