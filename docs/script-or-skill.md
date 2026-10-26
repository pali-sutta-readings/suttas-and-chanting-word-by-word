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
| `bm`, `ccb`, `original` | `anchor` | from the heading that carries `<a id="anchor">` up to the next heading that carries any anchor |
| `bm`, `ccb`, `original` | `anchor..end` | from `anchor` up to (not including) the heading with anchor `end`; `..END` runs to the end of the file |
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

## Spike 2: DPD check and gloss (2026-10-24)

### Method

Throwaway code in the session scratchpad, against the live Simsapa app. The first attempt (2026-10-23, Simsapa 1.0.0-alpha.8 and 1.1.0-alpha.2) used `/dict_combined_search` and the default `/gloss_text`. It found that neither answers exactly, and the maintainer added two exact routes to Simsapa: `POST /lookup_forms` and `/gloss_text` with `"options": {"exact": true}` (`docs/simsapa-localhost-api-search-endpoints.md` §18–§19). The spike was then run with these routes, on **1.1.0-alpha.2, DPD `v0.4.20260501`**, over the **whole tree** rather than the planned four-text sample, because a full run takes seconds (see "Cost"). The row words are those `chantlib.parse` finds in every text, unit rows and variant rows alike.

### Results: what the routes return

- **`/dict_combined_search` and the default `/gloss_text` are not exact** (tier 2 in the API doc). Search matches stems and prefixes: `bhagav`, not a word, returns *bhagavant*; `atthañ` gets the split `atthaṁ + ca`. The default gloss also drops a word whose stem already occurred in the text (`bhagav bhagavantaṁ` gives one entry), lists unknown words only in `unrecognized_words`, and cuts an iti form to its base (`bhavissan'ti` → `bhavissaṁ`, iti lost). Its entries cannot be matched to our words by position. A "not found" check built on them would need to fetch every candidate's `word.json` and search its `inflections` list itself.
- **`/lookup_forms` is exact.** It takes up to 5,000 forms per call and gives one result per form, in input order. Each result has `status` (`found`, `deconstructed`, `not_found`, `invalid`), every headword of the form's DPD lookup row (`lemma_1`, `pos`, `grammar`, `construction` as a list of lines, `root_key`, `meaning_1`, `matched_as` `lemma`/`inflection`), and every split, with each component's own exact uids. It handles our spellings: `cittan'ti` → `cittanti`, found, with the split `cittaṁ + iti`; `c'ānanda` → `ca + ānanda`; `vijjācaraṇa-sampanno` → `vijjācaraṇasampanno`; `sabb'ītiyo` → `sabba + ītiyo`. No apostrophe join is needed in our scripts. The response carries `dpd_version`.
- **Exact `/gloss_text` keeps every token, in order** (`token_index`), each with its `/lookup_forms` result. On six sample lines, 27 of 27 tokens lined up with our rows by position. Iti forms stay whole (`gacchāmī'ti`).

### Results: cost

All 7,465 distinct row words (22,762 rows) and the 1,826 respellings below go through `/lookup_forms` in six calls in **about 2.6 s**. The PRD's estimate (about 50 ms per word, minutes per run) was for one search per word. No disk cache is needed: a full check costs less than its own parsing.

### Results: not found

673 distinct row words are `not_found`. Two kinds are our own notation, and a fixed, exact respelling resolves them:

| Kind | Words | Rule |
| :--- | ---: | :--- |
| Elided compound member, `dhamm'`, `dhaj'` | 129 | look up the stem + each vowel (`dhamma`, `dhammā` …) and keep headwords that are citation forms (`matched_as: lemma`) |
| Sandhi spelling, `attham-`, `buddhañ`, `aham-` | 135 | strip the hyphens; final `m`/`ñ`/`ṅ`/`n` → `ṁ` |

The elided rule must be applied to **every** form ending in `'`, even when the bare stem is found: `sat'` stripped is `sat`, a form of *sant* (√as), which made a false root flag on a row that means *sati* (√sar).

What is left after the respellings:

| Kind | Rows | Meaning |
| :--- | ---: | :--- |
| `comp` row | 154 | DPD has no headword for the compound (`dasa-pāramitānubhāvena`). Expected; its member rows are checked. |
| `(sandhi)` row | 59 | Its parts are in the note (`[*vuccati* (…) + *ānanda* (…)]`) and can be looked up exactly. |
| member row | 264 | Mostly fragments cut at a sandhi junction (`bbalā`, `avijj`, `di`, `ek`), plus some real forms (`abhigītiṁ`, `colaṁ`). |
| plain row | 78 | Mostly forms DPD lacks (`abhipūjayāmi`, `pamuccantu`, `jayassu`, `konāgamanassa`), a few notation (`buddhass'`, `dāso/dāsī`). |

**"Not found" is therefore not an error.** Almost every case is a gap in DPD or our notation, and it would come back on every run. It becomes a reviewed item (below), not a flag.

### Results: flags

| Check | First cut | After the fix | Fix |
| :--- | ---: | ---: | :--- |
| "no root in DPD", but DPD has a root | 303 rows | 1 (*patī*) | Compare only the headwords whose `lemma_1` without its number is the lemma the row names (`[agga, no root in DPD]`); other homonyms of the form don't count. |
| our √root matches no `root_key` | 18 rows, 8 words | 7 words | Read DPD's roots from `root_key` **and** from the `construction` lines; apply the elided rule to `'` forms. |
| our √root where DPD's headwords have none | 119 rows | — | Not an error: DPD gives compounds and denominatives no `root_key` (*bojjhaṅga*, *bahulīkata*), and the spec adds member roots "where useful" (§6). Dropped. |

Of the 7 root words, a hand check found real candidates (*citto*: DPD gives the form only under *citta 2*, √citt; *vattu*: the infinitive is from √vac, the row says √vad (wrong: see "Implementation"); *candani*: DPD √sand) and one false flag caused by DPD: the lookup row for `pattiyā` lists *patti 1.x* (√ap) but not *patti 2.1* (√pad), although `patti` itself does. **Exact lookup rows can be incomplete**, so flags too are reviewed and kept in the ledger, not treated as certain errors.

### Results: etymology candidates

Comparing each row's etymology with every `construction` line of the form's headwords and with every split, after only spaces, `*` and `>` spacing are normalised, gives **3,709 distinct candidates**: far too many to review. Nearly all are a few systematic notation differences. Each of these fixed rules was measured, and each removes a class without looking at meaning:

| Rule | Example (ours / DPD) |
| :--- | :--- |
| (a) a bare lemma is accepted when it is a headword's `lemma_clean` | `[ya]`, `[dasa]`, `[agga, no root in DPD]` |
| (b) no candidate when DPD gives no construction and no split | *cīvara*, *purisa*, pronouns |
| (c) DPD's `[y]` brackets and `*` dropped | `ā + √khā + y + ī` / `ā + √khā + [y] + ī` |
| (d) our nested sub-analyses dropped | `vibhūsana (vi + √bhūs + ana) + ṭhāna (…)` / `vibhūsana + ṭhāna` |
| (e) each member may match any link of DPD's `>` chain | `adhi > ajjh + …` / `adhi > adhy > ajjh + …`; `√nī + a` / `√nī > nay + *a` (query D17) |
| (f) DPD's trailing bare ending dropped | `viññāṇa + paccaya` / `viññāṇa + paccaya + ā` |
| (g) a split's last member may be inflected | `gaja + vara` / split `gaja + varaṁ` |
| (h) verb stems: the row passes when its root is a `root_key` of the headwords (checked by the root flag). **Dropped**: see "Follow-up" below | `√bhaṇ + a + mase` / `bhaṇa + mase`; `vi + √har + a + nti` / `vi + hara + ti` |

After (a)–(h), **389 distinct candidates** remain. They are judgment cases, the work the `dpd-review` skill was planned for: member grouping (`saḷ + āyatana + nirodha` / `saḷāyatana + nirodha`), *anubhāva* / *ānubhāva*, enclitics in our etymology (`saṅgha… + ca`), real differences (`khippa + abhiñña` / `khippa + ābhiñña`), and absurd DPD splits that must not be followed (`abhisaññūhitvā` → `na + bhisa + ñū + hitvā`). A split is evidence, never the authority.

Rule (h) is the only one that can hide a real error: a wrong stem or suffix chain on the right root (a verb put in the wrong conjugation class) is not seen by the script. Its premise was also wrong: DPD does not write verb stems without the root. It stores the construction from the stem and the root chain in a separate column, `root_base`, which `/lookup_forms` did not return at first (see "Follow-up").

### Results: ledger key

Two runs gave byte-identical output, so the keys are stable. The key is word + our etymology + a short hash of the DPD data compared: each headword's `lemma_1`, `root_key` and `construction` lines, and the split strings. Meanings are left out, so that a DPD edit to a meaning does not bring a reviewed item back. Editing a row's etymology changes only that row's key, because the key contains it.

### Results: gloss

On six lines (01/03, 07a/02, 10/03), composing rows mechanically from the first headword's first construction gave the right etymology for 16 of 27 rows and the right word class for 18 of 27. The misses are judgment cases: *arahaṁ* (the first headword is *araha*, adj; the row is *arahant*), *vā* (the first headword is the letter *va*), *tathāgato* (two analyses, the row gives both), and every finite verb (DPD's construction is the lemma's). Case, number, person and mood are not in the data at all. This confirms PRD FR-20: the script presents the candidates and the agent writes the rows.

### Decision

| Tool | Script does | Skill does | Change from the plan |
| :--- | :--- | :--- | :--- |
| `simsapa.py` client | `/lookup_forms`, exact `/gloss_text`, `/word.json` for `--inflections`, `/health` | — | Uses the exact routes; `/dict_combined_search` only to widen a `not_found` form in `lookup`, labelled as guesses. No disk cache. No apostrophe join. |
| `check` | exact lookup; the two respellings; flags for root and "no root in DPD"; candidates for etymology (DPD's construction forms, rules a–g and the new h–j), grammar (DPD's parses), not-found, and members; ledger keys | `dpd-review` classifies flags and candidates into the ledger | "Not found" is a reviewed item, not a flag. Flags also go through the ledger. `comp` rows that DPD lacks are not reported (their members are). `(sandhi)` rows are checked through the words in their note. |
| `gloss` | exact `/gloss_text`, tokens zipped with the line's words, `index.py rows` per word | `pali-word-analysis` writes the rows | No apostrophe join or remapping: exact mode keeps our spelling. |

Awaiting maintainer review.

### Follow-up: DPD's displayed construction and parse of the form (2026-10-24 to 2026-10-26)

**What was missing.** DPD's rendered entry for *bhaṇāmase* shows `[√bhaṇ + a + mase]`, our notation, while `/lookup_forms` gave `bhaṇa + mase`. DPD stores a construction from the stem and the root chain in `root_base` (`√bhaṇ + a > bhaṇa`) and `root_sign`; its entry displays the two combined. Rule (h) was compensating for data the route did not return. DPD's `lookup` table also parses each form per lemma (`carissanti`: *carati*, verb, `fut 3rd pl`), and no route returned that either. Simulated from Simsapa's DPD database (read-only): with DPD's display form and the `root_base` substitution in place of rule (h), etymology candidates go from 2,372 rows (863 distinct) to 1,302 (545 distinct); about 170 of those are future or aorist forms under a present-tense headword, which stay judgment cases. The extra distinct candidates over rule (h)'s 389 are the wrong-stem cases rule (h) hid.

**Requested and added to Simsapa** (`docs/simsapa-localhost-api-search-endpoints.md` §19.1): on each headword `root_base`, `root_sign`, `construction_summary` (the construction as DPD's entry displays it) and `form_grammar` (the parses assigned to that headword); on each result `form_grammar_raw` (DPD's triples verbatim); on each split component its own `form_grammar_raw`. A spelling suggestion for `not_found` forms was also suggested, as low value; it was not added and is not needed.

**Checked on the running app (2026-10-26; `app_version` still 1.1.0-alpha.2, DPD `v0.4.20260501`).** Every field is present in `/lookup_forms`, in exact `/gloss_text` tokens, and (`construction_summary`) in `/word.json`:

| Form | Field | Value |
| :--- | :--- | :--- |
| *bhaṇāmase* (`49236/dpd`) | `construction` / `construction_summary` | `bhaṇa + mase` / `√bhaṇ + a + mase` |
| *adesesi* | `construction_summary`, `root_base` | `a + √dis + *e + si`, `√dis + *e > dese (caus)` |
| *bhagavantaṁ* | `form_grammar` | *bhagavant 1* `masc acc sg`; *bhagavant 2* `nt nom sg`, `masc acc sg`, `nt acc sg` |
| *carissanti* | `form_grammar` | `fut 3rd pl`, on all four *carati* headwords |
| *katamo* | `form_grammar_raw` / `form_grammar` | `katama interr masc nom sg` / none (`interr` maps to no `pos`, by design) |
| *cittan'ti* | result / `cittaṁ` component | no parses / `citta noun nt nom sg` & co. |
| *magga’’nti* | `maggaṁ` component (`iti_rule`) | `magga noun masc acc sg` & co. |

Two things the scripts must allow for:

- **`construction_summary` is DPD's display, which is short for entries without `meaning_1`**: *bhagavant 2* `√bhaj`, *vicāra 2* `vi + √car`, *carati 2.3* `√car`. The rendered entries show the same. So the summary is one of DPD's forms to compare with, alongside the `construction` lines and the `root_base` substitution, and never replaces them.
- **The new fields came without an `app_version` change**, so `simsapa.py` and `check-tools.sh` test for `form_grammar_raw` in a response, not for a version. `construction_summary` is `null` when the installed `dpd.sqlite3` predates the column.

**Grammar against the live fields.** A throwaway comparison over the tree (non-member rows; case, number and gender, or person, number and tense): 16,093 rows, 5,531 distinct words, one `/lookup_forms` pass in 2.3 s. 12,286 rows agree with one of DPD's parses, 109 do not (62 distinct words), 405 have no DPD parse, and 3,293 have no case or person tags. Most of the 62 are notation the check maps by a fixed rule (DPD's `imperf` for our `aor`: *āgū*, *ajjhagā*; `dual` for *ubho*; our `instr/loc`), and the rest are review items: metrical lengthening DPD does not list (*sakya-munī*, *lokassā*), DPD gaps (*bahunnaṁ* gen pl), compounds DPD parses under another gender (*dukkhanirodhaṁ*: DPD masc acc sg, ours nt nom sg), and *mahārājā* tagged nom pl (DPD: nom sg). This agrees with the simulation (11,644 of 11,738, before the comparator was fixed).

**Changes.** Rule (h) as first written is dropped. `check` compares a row's etymology with each `construction` line, the `construction_summary`, and each line with its stem replaced by the `root_base` chain, and adds a third kind of candidate: our tags match none of DPD's parses of the form. This compares labels with DPD's; assigning them stays with the agent and the `pali-word-analysis` skill, which now starts from the parses and reads `inflections_html` only for a form DPD gives none. `simsapa_fmt.py` prints `/lookup_forms` and exact `/gloss_text` responses (it treated a `/lookup_forms` response as an empty search before), and `check-tools.sh` reports `dpd_version` and warns when the fields are missing. The fixtures `lookup_forms.json`, `gloss_exact.json`, `health.json` and `word_*.json` were re-recorded with the fields. PRD FR-17–FR-20a and tasks 9.0–9.8 are updated.

### Implementation (task 9.5, 2026-10-26)

`scripts/simsapa.py check` on the whole tree, live API: 22,546 rows (variant rows of book 10 included) in about 5 s. First run: **7 flags**, 6 root (*citto*, *vattu*, *candani*, *pattiyā*, as in the spike, plus *pasutaṁ* `[pa + √su + ta; DPD pasūta]` and *saccañ-* `[√su + ta + ya]`, respelled *saccaṁ*) and 1 no-root (*patī*); **768 distinct candidates**, 434 etymology, 113 grammar and 221 not found. After the review rules below: 7 flags, 303 etymology, 113 grammar, 221 not found (644 items).

Etymology first came out at 806 distinct. A new rule (h) took it to 452: a **verb headword the form inflects** has DPD's construction for the lemma (`anu + √mud + *a + ti`), while our row ends in the form's ending (`anu + √mud + a + tha`, `upa + √ṭhā > ṭhāpe + ssa + nti`). For these the last member on both sides, and our tense sign before it, are left out. This hides nothing that the old rule (h) hid: the stem chain is still compared, and the ending is what the grammar comparison checks against DPD's parses. Further rules are in "Review" below. What is left is the judgment the spike described: member grouping (`dhamma + savana + kāla` / `dhammassavana + kāla`), *ānubhāva* / *anubhāva*, `aṇa` / `ṇa`, absurd splits.

The grammar candidates are review items, nearly all explained by the row's note or its line: a noun as the last member of a possessive compound taking its noun's gender (*manussaṁ* `(fem acc sg)` in *sadeva-manussaṁ pajaṁ*), metrical lengthening (*munī*, *ujū*), eastern nominatives in *-e*, and DPD gaps (*mahārājā* as an a-stem nom pl). Voice is not compared (DPD lists the `reflx` and plain forms separately, and our `mid` labels follow the line).

**Review (task 9.10).** Reviewing the 806 etymology candidates of the first run showed three more notation classes that a fixed rule removes without looking at meaning, and one bug:

| Rule | Example (ours / DPD) | Candidates after |
| :--- | :--- | ---: |
| (h) as above: a verb headword's lemma ending, and our tense sign, left out | `anu + √mud + a + tha` / `anu + √mud + *a + ti` | 452 |
| bug: a string that is both a headword's construction and a split was compared only as a construction | `ta + api` / split `taṁ + api` | 449 |
| (i) a run of members whose letters join to exactly the other side's member, in either direction; members with a root are never joined | `pubba + bhāga` / `pubbabhāga`; `abyāpāda` / `na > a + byāpāda` | 349 |
| (g) widened: a split's member may be ours plus an ending of up to four letters, at any position | `muni + rāja` / `muni + rājassa` | |
| (j) an enclitic we add to the analysis (`ca`, `api`, `pi`, `eva`, `va`, `iti`) when DPD splits it off | `saṁ + √ghaṭ + a + ca` / split `saṅghaṁ + ca` | 306 |
| (c) extended, found by the trial of task 9.12: DPD's "uncertain" marker `??` dropped like its `*` | `siri + ttha` / `?? siri + *ttha` | 303 |

The other etymology items, the 113 grammar items, the 221 not-found items and the 7 flags were reviewed one by one into `checks/dpd-review.tsv`: 644 items after the last rule; 2 errors, and 6 questions of analysis that the agent then decided (3 more errors, 3 rows that stand), after the maintainer's direction that such questions are the agent's to decide (`docs/legacy-migration.md`, "DPD check review"). The review corrected one finding of spike 2: *vattu* `[√vad + tuṁ]` is right. The form *vattu* alone is only *vattar* (√vac) in DPD, but the row means the infinitive *vattuṁ*, which DPD gives as `√vad + tuṁ`. It is a `homonym`.

Reviewing needed the verdicts `expected` (a spec rule or a decision makes the row differ on purpose, usually named in its note) and `query` (only for a doubt about the Pāli text itself), beside `notation`, `homonym`, `dpd-gap` and `error`; the planned `other` was not needed.

### Trial (task 9.12, 2026-10-26)

Following the `draft-new-text` skill, the table for the first line of *Dhp 1*, *Manopubbaṅgamā dhammā, manoseṭṭhā manomayā*, which is in no text of the repo, was drafted in a scratch file (Pāli from Simsapa, `GET /sutta.json?uid=dhp1-20/pli/ms`, segments `dhp1:1–2`). `simsapa.py gloss` gave every word's DPD data: *dhammā* as `masc nom pl` among DPD's parses, and the three compounds as adjectives whose parses include `masc nom pl`, with constructions `mano + pubbaṅgama`, `mano + seṭṭha`, `mano + maya`. The rows, labels and member rows were written with the `pali-word-analysis` skill (4 rows, 6 member rows), and `draft.py build` wrote the file.

- `lint.py`: 0 ERROR, 0 STRAY, 0 WARN.
- `simsapa.py check --strict`: first 1 candidate, *seṭṭhā* `[siri + ttha]` against DPD's `?? siri + *ttha`. The row follows DPD; only DPD's "uncertain" marker blocked the match. Rule (c) now drops `??` like `*`, and the check passes with 0 flags and 0 candidates.
- Skill fixes: `index.py overlaps` reads chant files, not drafts, so `draft-new-text` and `docs/drafting-workflow.md` now say to build the draft's `P|` lines into a scratch file first (tried: it found *Namo tassa …* in four texts).

The scratch file was not committed.

