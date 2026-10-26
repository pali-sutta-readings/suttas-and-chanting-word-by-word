# Quality process

The checking routine for any change to a text in `books/`, from a one-row fix to a new text. It is the routine the legacy project ran after every session, which brought all 209 texts to 0 ERROR and 0 STRAY. The rules being checked are in `docs/style-spec.md`. How to draft a new text is in `docs/drafting-workflow.md`.

Run the steps in order, on the files you changed (or the whole book, for a large change). A step that finds a fault means: fix the file, then run the routine again from step 1.

## 1. Lint: 0 ERROR, 0 STRAY

```sh
make lint                                  # all texts
python3 scripts/lint.py books/07a_suttas/texts/05_dhaj_agga_sutta.md
python3 scripts/lint.py --fix FILES        # safe fixes only, then lint again
```

- ERROR and STRAY must reach zero. Both fail the check (exit code 1).
- Each remaining WARN is explained: in the changelog entry, or in the report to the maintainer. Some are expected by rule, e.g. the repeat WARN on an identical line with different grammar (style spec §8), compound members written apart by BM in the Vinaya files (§12.1), long instruction lines (§12.1).
- `--fix` makes only safe, mechanical fixes (style spec §5, synonym tags; `---` lines; NFC; ṃ → ṁ). Log them as one "safe fixes applied" line per file.
- The baseline for the migrated texts is 0 ERROR / 0 STRAY, with 4 WARN in 01–08, 18 in 09a–09e and 0 in 10.

## 2. Pāli check against the source

```sh
make fetch-sources     # once, and after a re-pin of sources/UPSTREAM.txt
make compare
```

`compare` checks each file's Pāli lines, normalised, against the text's source: the *Bhikkhu Manual* (upstream Markdown), the *Chanting Guide* (if a local copy is present), `sources/reference-pali-supplement.md`, SuttaCentral's JSON for book 10, or the Vinaya originals in `sources/originals/`. Which passage belongs to which text is recorded in `sources/ref-map.tsv` (an anchor, an anchor range or a segment range), written and kept with the `source-compare` skill (`.claude/skills/source-compare/`); the script never guesses it, and stops with a map error if an anchor or segment is gone. For the Vinaya pages, where English and Pāli are mixed, `compare` checks that each Pāli line of ours occurs, in order, in the passage (`contain` mode); the skill reads those passages once for formulae missing from our text. Classify every reported item with the skill. Every difference must be one of:

- a filled elision (*…pe…*, “…”), written out from the text's own wording and logged;
- a logged misprint fix, or a logged restoration decided by the maintainer;
- removed leader brackets, `(×3)`, rubrics (stripped before the comparison);
- for books 09 and 10, a variant list (checked separately, style spec §12).

Anything else is a fault in the file: fix it. Variant cues are not seen by `compare`; check them by hand against the source's substitution lines (09), or by rebuilding the lists (10, style spec §12.2). The originals are never edited: `git diff --stat -- sources/originals` must be empty.

## 3. DPD check of every row

```sh
make dpd-check                                 # all texts; Simsapa must be running
python3 scripts/simsapa.py check FILES         # --strict: fail on unreviewed candidates too
```

DPD, through the Simsapa app's localhost API, is the authority for roots, constructions and compound members, and lists the possible parses of each form. `simsapa.py check` looks every row up exactly (`/lookup_forms`) and reports two levels:

- **Flags**, likely errors: a root that matches no root of the form's DPD headwords; "no root in DPD" where DPD's headwords of that lemma have one.
- **Candidates**, for review: an etymology that matches none of DPD's construction forms or splits (after fixed notation rules); tags that match none of DPD's parses of the form; a form DPD does not have.

Review every new flag and candidate with the `dpd-review` skill (`.claude/skills/dpd-review/`), which records a verdict for each in `checks/dpd-review.tsv` (`notation`, `homonym`, `dpd-gap`, `expected`, `error`, `query`). Reviewed items are hidden on later runs; a change to the row or to DPD's data brings an item back. `make dpd-check` fails while a flag is unreviewed. Fix each `error` (with the maintainer's agreement for migrated texts), and put each `query` (a doubt about the Pāli text) to the maintainer. Questions about the analysis are decided by the agent, following the `pali-word-analysis` skill (§7, "Decide, don't defer"), and the decision is written in the verdict's reason. A fix made to follow DPD is logged with "DPD" as the reference.

Variant rows of book 10 are checked like any other row (`dpd-variant-rows`).

## 4. Review of grammar labels

`simsapa.py check` compares tags with DPD's parses of the form, but a tag that matches a parse can still be the wrong one for the line (*bhagavantaṁ* is masc acc sg as a noun and nt nom sg as an adjective). Review the tags of every new or changed row with the `pali-word-analysis` skill (`.claude/skills/pali-word-analysis/SKILL.md`): the label must fit the word as it stands in the line (agreement, mood, sandhi), use only the allowed tokens in the canonical order, and be one of DPD's parses of the form, or explain in its note why not. Scripts never assign grammar labels.

## 5. Independent spot check: 10 units

A separate agent, one that did not draft or edit the files, checks 10 units chosen at random from the changed files (variants count as units). For each unit it checks the rows against DPD and the style spec, and the Literal and Faithful lines against the Pāli. Confirmed errors are fixed and logged; the result is reported as a score (e.g. "spot check 9/10, one tag fixed"). If several errors are found, look for the same error elsewhere in the changed files.

Give the agent only the file paths, the style spec and the skill, not the drafting notes, so that the check is independent.

## 6. Consistency across files

```sh
make index                                     # whole tree
python3 scripts/index.py index --folder 07a_suttas
python3 scripts/index.py rows WORD             # settled rows for a word
python3 scripts/index.py overlaps FILES        # lines equal to a settled line elsewhere
```

`index` lists words whose rows differ between files, in etymology or in tags. Align a row with the others only where its grammar and meaning in its own line are the same; different grammar in context (nom/acc by construction, a different lemma) is kept. Log every alignment, in each folder whose files change. A Pāli line identical to a settled line in another file is copied, not re-analysed (style spec §4, §12).

## 7. Changelog entry

Every change to a text gets an entry in its folder's `CHANGELOG.md` (style spec §11), newest at the top: a dated heading, then per file a table:

```text
| Line | Was | Now | Why | Reference |
```

"Was" and "Now" give the old and new text of the row or line; "Why" the reason in a few words; "Reference" the authority (`DPD <headword>`, a spec section, the source, or the maintainer's decision). Note the results of steps 1–6 in the entry's opening paragraph: lint result and explained WARNs, compare result, DPD flags explained, spot-check score.

## 8. Build

```sh
make book BOOK=07a_suttas
```

The build warns (and does not fail) if lint finds errors in the book's files. Every EPUB is validated with `epubcheck`. Look at the changed pages in the PDF.

## Queries to the maintainer

When a rule seems wrong for a text, or the Pāli text is uncertain (a possible misprint, an expansion of an elision, a mistranslation in the source), keep the file as it is and ask the maintainer. Questions about the analysis of a text (which reading, sign or label; how full an etymology) are not queries: the agent decides them by the `pali-word-analysis` skill and records the reason. Record the answer in `docs/decisions.md` and apply it with a changelog entry that cites it.
