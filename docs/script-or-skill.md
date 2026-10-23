# Script or skill

Which checks are done by a script and which by an agent following a local skill (`.claude/skills/`). The rule is in the PRD (FR-16a):

- A **script** is used when its input is our own files or a stable, keyed format (an anchor, a segment id, a DPD record), and its answer is either exact or a clear failure.
- A **skill** is used for judgment: reading markup we don't control and deciding which parts are Pāli, finding which reference passage matches which text, deciding whether a difference matters, and composing word rows from DPD data.

Scripts never guess where a wrong result would look like a right one. They stop with an error, or report a candidate for the agent to review.

Before the tools were written, two spikes tested this split on real texts with throwaway code. Their findings are below.

## Spike 1: compare, index, align, draft (2026-10-23)

### Method

Throwaway code in the session scratchpad, not in `scripts/`. It used `chantlib.parse` and `chantlib.text.norm_line` from this repo, the BM upstream Markdown at the pinned commit (`sources/upstream/bhikkhu-manual`), and the SuttaCentral JSON in `sources/suttacentral/`. The legacy `chant_pipeline.py compare` (`BACKUP/_tools/`, with its own `style-spec.md`) was run read-only on the same texts, with the upstream BM file as `--ref`.

Sample, as planned:

| Texts | Reference |
| :--- | :--- |
| `01_morning_chanting`, all 7 | BM `chants/morning-chanting.md` |
| `07a_suttas/01_dhammacakkappavattana_sutta` | BM `chants/suttas.md` (has the sub-heading *Bhummānaṁ devānaṁ*) |
| `09_vinaya_formulae/01_vinaya_notes_requisites`, all 7 | BM `vinaya/requisites.md` (substitution lists) |
| `10_mahasatipatthanasutta/03`, `08` | SC `dn22_root-pli-ms.json` |

To choose the map syntax, two wider throwaway surveys were also run: every 01–08 text against every BM anchor section (best match by similarity), and every 09 text against the BM line ranges recorded in the 09 changelogs. The best-match search was only a survey tool; it is not a way to build the map (see "Mapping").

### Results: mapping

- **Sample: 17 of 17 texts map to one key.** The 7 morning-chanting texts and the 7 requisites texts each have their own BM anchor (4 of the requisites anchors are on `###` sub-headings). 07a/01 is one anchor whose passage runs on through the `###` *Bhummānaṁ devānaṁ* sub-section, up to the English section. The two book-10 texts are SC segment ranges, and each text already gives its range in its citation (`*DN 22:3.1–3.7*`), so their map entries need no search.
- **All of 01–08 (130 texts).** If a passage runs from its anchor to the next heading that carries an anchor, 78 texts match one anchor exactly, and 5 more match exactly when the passage runs on to a later anchor (e.g. 04a/11 *Khandha-paritta* runs from `virupakkhehi` up to `group-protection`, over the Pāli sub-section `appamano-buddho`). About 23 texts appear to have no BM passage (07a/07–12, 07b, 07c and four in 03: Chanting Guide, supplement or SC). Most of the rest match closely, with real differences or the upstream additions noted below. A few match poorly (03/18, 04a/02, 04a/09a) and need the skill to find their passage.
- **All of 09 (60 texts).** By the line ranges in the 09 changelogs, 51 texts are one anchor and 9 run from one anchor to another. Most of the 9 start at a `##` heading whose first `###` sub-heading has no text before it (e.g. 02/04 *Pavāraṇā* … *For five or more*). Only a few really span (09b/09: *Procedure to Give the Kaṭhina-cloth* + *Kaṭhina Saṅghakamma*). 09c/11 ends where 09c/12 begins, at a `###` anchor inside the same `##` section.
- **Best-match location is unsafe.** The survey placed 04a/03 *Pubba-bhāga-nama-kāra-pāṭha* in evening chanting's preliminary homage rather than in the parittas' `namo-tassa`. The legacy compare placed 01/07 *Closing Homage* inside 01/01's *Dedication of Offerings*. In both cases the wrong passage has the same text as the right one. So the result looks correct until one of the two passages changes (see "Robustness"). This confirms that the map is written and kept by the skill, never guessed by the script.
- **Upstream has moved since the legacy conversion.** BM commit `0872fa5` (2025-11-16) added 10 lines such as `(See a word-by-word analysis [here](https://pali-sutta-readings.github.io/…))` under the Pāli headings of anumodanā, paritta and pāṭimokkha chants. A structural rule handles them (a line holding a link to `http`), but they are a reminder that the map and the rules are checked again after every `fetch-sources --update`.

**Decision: `key` syntax for `sources/ref-map.tsv`.**

| Source | Key | Passage |
| :--- | :--- | :--- |
| `bm`, `original` | `anchor` | from the heading that carries `<a id="anchor">` up to the next heading that carries any anchor |
| `bm`, `original` | `anchor..end` | from `anchor` up to (not including) the heading with anchor `end`; `..END` runs to the end of the file |
| `sc` | `dn22:3.1..dn22:3.7` | the segments from the first to the last id, inclusive; title (`:0.n`) and heading (`.0`) segments skipped |
| `supplement` | `id..id` | the `[id] text` lines from the first to the last id, inclusive |
| `chanting-guide` | as `bm`, if a local copy exists | skipped with a report line otherwise |
| `none` | empty | no reference; the `note` column says why |

Line spans and sub-heading names are not used. An anchor that disappears gives a map error, but a line span that shifts after an upstream edit gives a wrong passage with no error. Every BM sub-heading that a text starts or ends at carries an anchor, so line spans were never needed.

### Results: extractor

Structural rules tested (the only rules applied to BM Markdown). None of them decides which words are English:

1. Take the passage named by the key (above).
2. Drop `<div class="english">` and `<div class="instr">` blocks (BM marks its English sections and its rubrics this way: 359 and 72 blocks in `chants/` and `vinaya/`).
3. Drop headings, `**Contents**` lists, HTML tags (anchors, `<span class="vin">`), and lines holding a Markdown link to `http(s)`.
4. Drop lines that are wholly in italics (*S.V.420*, English titles). Of the 103 such lines in BM `chants/`, none is a Pāli line of ours (one is the citation *Puggalapaññatti 1*).
5. Decode HTML entities (`&ndash;`, `&amp;`), drop the blockquote `>` and the line-end `\`, and keep the words inside `[…]` leader brackets. Our texts have the leader lines (*Handa mayaṁ …*) as Pāli units, so a `> [Handa mayaṁ …]` line is kept.
6. `norm_line()` on each remaining line (as for our own texts).

Diff of the sample, new extractor against legacy compare:

| Texts | New: result | Legacy: result |
| :--- | :--- | :--- |
| 01 (7) | 7 identical | 7 identical, but headings and English lines are in the stream; 01/07 found in the wrong passage |
| 07a/01 | 9 differences, all real | the same 9, plus 1 false (the heading *Bhummānaṁ devānaṁ*) |
| 09a (7) | 7 identical (see "Vinaya pages" for why this does not generalise) | 3 identical; 4 false differences (English glosses and the items of a substitution list) |
| 10 (2) | 2 identical | 2 identical |

The 9 real differences in 07a/01 were classified using only the extractor output, the 07a CHANGELOG and `docs/decisions.md`:

- 8 are **expected**: BM misprints corrected and logged (*Pathamaṁ*, *appativattiyaṁ*, *Veyyākaraṇapāthena*, *maranampi*: CHANGELOG, query 48) and BM's final *m* written *ṁ* (*saṅgītantam*, *seyyathīdam*, *suvisuddham*, *ath'āham*: logged in the row after it).
- 1 is **unexplained**: BM *pañcupādānakkhandā*, ours *pañcupādānakkhandhā* (07a/01:436). This is almost certainly a misprint fix that was never logged. It goes to the maintainer and is not changed here.

Nothing beyond these sources was needed. The one thing the agent must know is that a final *m*/*ṁ* difference is a spec rule (§2), not a misprint. A script cannot fold that difference away, because *m* before a vowel is correct Pāli (*tam-ahaṁ*).

### Results: robustness

On scratch copies:

| Change | New | Legacy |
| :--- | :--- | :--- |
| BM heading renamed (anchor kept) | no effect | no effect |
| BM anchor deleted | **map error** naming the entry | no effect (finds the text by its content) |
| BM line inserted at the start of a section | reported (1 insert) | **missed**: says identical, because it locates the chant after the insertion |
| BM line inserted mid-section | reported | reported |
| BM last lines of a section deleted | reported (1 clean delete) | reported, but compared with the next section and its English: 26 garbage differences |
| BM line changed in 01/07's passage (`closing-pali`), which repeats 01/01's | reported | **missed**: says identical, because it compares with 01/01's copy |
| A Pāli line edited in our text | reported | reported |
| A unit added at the start of our text | reported (1 delete) | located in the wrong chant (preliminary homage); similarity 0.11, garbage differences |

So the keyed extractor fails loudly, or reports exactly what changed. The legacy one gives a clean "identical" in two cases where the reference changed.

### Results: Vinaya pages

BM's Vinaya pages mix English prose, quoted Pāli formulae, italic English translations, italic placeholders (*saṅghāṭiṁ*, *uttaro*) and substitution lines (`'imaṁ' → 'etaṁ'`). No markup separates the Pāli from the English prose.

- **A quote rule was tried and rejected.** The rule took the quoted spans `'…'` that are not wholly in italics. It matched all 7 requisites texts. Run at paragraph level on all 60 texts of 09, it matched only 29 exactly. It failed on nested quotes (*'Āyasmā bhante 'uttaro' bhikkhu …'*), English in quotes (*'extra robe'*, *'out of season'*), unquoted formulae and stray entities. Each fix would be another heuristic of the kind the PRD rules out.
- **An agent cleans a passage easily.** For 09e/05 *Sick Pārisuddhi*, where the quote rule fails on the nested quote, a hand-cleaned stream of the BM passage is identical to ours.
- **A containment check is exact and needs no cleaning.** Each of our Pāli lines (normalised) must occur, in order, in the normalised raw passage, English included. English in the reference cannot cause a false result, because only our lines are looked for. On all 60 texts of 09, 285 of 309 lines were found and 44 of 60 files were fully contained. All 24 lines not found are explained in the changelogs or by spec rules: elisions written out (*Namo tassa …*, *Dutiyam-pi …*), units copied from another file (*Imaṁ cīvaraṁ āyasmato dammi*, BM "as in NP 1"), logged misprint fixes (*paṭigghaṅhātu*, *sanghe*), V19's added *upasaṁkamitvā*, BM's slash alternatives split into base and variant (V6), and final *m* → *ṁ*.
- What containment cannot see is a BM formula that is **missing** from our text. That needs one review of each passage by the skill, done once per text and recorded with the 8.6 review, and again when the passage changes upstream.

**Decision.** `ref-map.tsv` gets a `mode` column: `diff` (the default: our stream against the extracted reference stream) or `contain` (each of our Pāli lines, in order, in the raw normalised passage). The BM Vinaya pages (`sources/originals/09*`, identical to upstream) use `contain`. The skill still reads these passages, but to check for omissions and to classify the lines not found. `make compare` does not depend on a cleaned copy of the passage.

### Results: index

A throwaway `index` over all 209 texts (22,761 rows, 7,464 distinct words):

- **Same word, different etymology: 116 words.** In a random sample of 20, about 4 are legitimate homonyms (*no* "us" vs *no* "not"; *taṁ* from *ta* vs *tvaṁ*; *paritt'* "protection" vs "limited"; *sa* "with" vs *sa* "he"). About 15 are alignment candidates, mostly notation: the ending included or not (*ajjhattaṁ* `… + atta` vs `… + atta + aṁ`), `;` vs `+` (*seyyathāpi*), `√ghaṭ` vs `√ghaṭ > ghāṭ`, two styles for *sacca*, and *nāma* with and without "no root in DPD". One (*mettaṁ*, *mettā* vs *metta*) needs DPD to decide. So this report is high-signal. It stays a report for the `dpd-review` skill, and no notation is normalised away, because which notation is right depends on DPD.
- **Same word, different tags: 565 words.** In a sample of 20, about 15 are legitimate: case, number or gender set by the line (*bhikkhuno* dat/gen, *sarāgaṁ* acc/nom), homonyms (*satta*), and a word with `comp` as a compound member but without it standalone. When only word-class tokens are compared (`pp`, `prp`, `ptp`, `abs`, `inf`, `ind`, `adv`, `adj`, `pron`, `rel`, `dem`, `interr`, `card`, `ord`, `prefix`, `sandhi`, `interj`, `comp`, `caus`, `denom`, and noun gender when the word is not adj/pron/participle/numeral), 308 words remain, and about half of a sample of 20 are real candidates (*sayaṁ* adv/ind, *sudesitaṁ* pp/adj, *joti* fem/nt, *paṭipanno* with and without `pp`).

**Decision.** `index.py index` prints the etymology conflicts and the **word-class** tag conflicts by default; `--all-tags` prints every tag conflict. This is a fixed projection of the tags, not a judgment: it hides only differences that depend on the line, which grammar review (the `pali-word-analysis` skill) covers.

### Results: align

Seven rules were rebuilt from the S22 and later changelog rows (*bhagavant*, *sāvaka*, *anuttara* tags and construction, *abhiññāya*, *sacca*, *no*). They were run on the pre-S22 `FINAL` tree with the legacy match (`old in line`) and with a match inside the named cell only. There were **0 spurious hits** either way: in practice the etymology strings never appear in the meaning or tags cells.

The real hazard is different: **re-running a rule whose `old` is a substring of its `new`.** The *no* rule (`na + u` → `na + u > no`) would now hit all 40 rows it fixed, making `na + u > no > no`. The *bhagavant* rule is safe to re-run only because its `new` happens not to contain its `old`.

**Decision.** `align.py` matches `old` against the whole cell content after trimming. That is the etymology inside `**[…]**`, the whole tag group, or the meaning. `"match": "substring"` is allowed, but then a cell that already contains `new` is skipped and counted. A test checks that applying the same rules twice changes nothing the second time. The cell scoping from the PRD is kept.

### Results: draft `I|`

The legacy drafts in `BACKUP/_tools/drafts/` hold 12 `I|file|from|to` lines (all in 09b and 09c). All 12 ranges still start at a Pāli line and end at a unit boundary in the current texts, but only because no edit since has changed a line count (S22's edits were all within lines). 9 of the 12 copied blocks are still word for word in their target file. The other 3 (09c/12, from 02/04, 02/06, 02/08) were edited after copying, as logged: alignment of *kāla*, and repeat notes for the second and third *Kāyena* lines. So `I|` is a copy made at build time, not a live include. A key-based `I|` survives row insertions in the source file, which line numbers do not.

**Decision.** As planned: `I|<text path>|<Pāli line>`, found by `norm_line` key; zero or two matches is an error.

### Decision summary

| Tool | Script does | Skill does | Change from the plan |
| :--- | :--- | :--- | :--- |
| `compare.py extract`, `diff` | keyed passage, structural rules, diff or containment | write the map; classify differences; review `contain` passages for omissions | key syntax `anchor`, `anchor..end`, `seg..seg`; `mode` column; extra structural rules (divs, italic lines, links, entities); no cleaned copies of Vinaya passages |
| `index.py` | E and T reports, dupes, stats, rows, overlaps | decide which conflicts to align | T report by word class by default; `--all-tags` |
| `align.py` | apply rules in one cell, dry run, log | write the rules and the "Why" | whole-cell match by default; skip cells that already contain `new`; idempotence test |
| `draft.py` | build/extract, `I|` by key | compose rows | none |

### The full run (2026-10-23)

Writing `sources/ref-map.tsv` for all 209 texts and classifying the first `make compare` (the review is in `docs/legacy-migration.md`, "Compare review") needed a few things the spike had not seen:

- **Anchors off headings.** BM puts a few anchors on other lines (`**1.**<a id="yankinci-vittam"></a>`, the numbered Ratana verses). A key may start at such an anchor; a passage still ends only at an anchored heading.
- **A BM table with English cells.** The thirty-two parts (03/09) are a table whose second column is italic English. Wholly italic table cells are dropped, as wholly italic lines are; with that, 03/09 is identical.
- **Chanting Guide passages need an end.** The conversion's headings are unreliable (`######` marks page breaks), so a passage that runs to the end of the file lets one early match break the order check. Chanting Guide keys are `Start heading..End heading`.
- **`contain` is useful beyond the Vinaya pages.** It also fits a chanted extract of a longer source (03/21, AN 10.58), a text that is part of an anchored passage with no anchor at its end (04a/09a), and BM's paritta invitation (04a/02), whose English notes are not marked off.
- **Book 10 variant lists need the cue's English.** A cue may apply to several units ("the four units above repeated"), drop words ("without *Idha, bhikkhave, bhikkhu*"), or replace a word wherever it occurs in the item. Rebuilding the lists therefore needs the skill to read the cues; a throwaway rebuild that tries each scope confirmed every list in 07 and 10–17. This stays skill work, as planned.
- **Locating passages needed the changelogs.** Best-match search proposed good anchors for most of 01–08, but every proposal had to be confirmed: the source of 03/18 (the Chanting Guide's longer *Dhamma-gārav'ādi Gāthā*, not BM's) and of the Chanting Guide suttas came only from the changelogs, and 03/19's source is still unknown.

Writing the map also found a build bug: `chantlib.books.folder_files` matched only `NN_*.md`, so the three texts named `NNa_*` (04a/09a and 09b *Ratana-sutta*, 04b/07a *Pacchima-ovāda-gāthā*) were left out of the built books. It now matches `NN*.md`.

Maintainer review (2026-10-23): accepted — "continue with the approach that was reliable": the keyed extractor, the `contain` mode for the Vinaya pages, the word-class tag report and whole-cell alignment. The unlogged 07a/01 *khandhā* fix stays listed for review in `docs/legacy-migration.md`.
