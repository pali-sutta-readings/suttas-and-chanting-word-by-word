# Maintainer decisions

The maintainer's dated decisions, collected from the legacy project's specs, PRDs, checkpoints and changelogs, so that the reasons behind the rules survive. The maintainer is the bhikkhu who answered the legacy project's queries. The rules that follow from these decisions are in `docs/style-spec.md`; this file records when and where each was made.

**Sources.** Paths starting `books/` are this repo's changelogs. Paths starting `legacy:` are relative to the legacy `BACKUP` snapshot (see `docs/legacy-migration.md`). Those files were not migrated, but they can be read in place.

**Query numbers.** The main project numbered its queries 1–60. The Vinaya and DN 22 sub-projects numbered theirs V1–V19 and D1–D17. Only some of queries 1–60 are recorded in the files that survive: queries 1–12, 28–32, 38–45, 47 and 52–55 have no record. Decisions without a query number are marked "—".

**New decisions.** Add a row to the right table, with the date and the file where the decision is applied (usually a changelog entry or a spec section). Decisions made while setting up this repo are in the PRD, `tasks/2026-10-22-153945-prd---repo-setup-and-legacy-migration.md` (marked "maintainer decision, 2026-10-22").

## Main chant books (01–08)

| Date | ID | Decision | Source |
| :--- | :--- | :--- | :--- |
| 2026-10-01 | — | Every compound gets a whole-compound row and one ↳ member row per part, for novice students. | `books/01_morning_chanting/texts/CHANGELOG.md` (S1, second pass); legacy: `_tools/style-spec.md` §4 |
| 2026-10-01 | — | The compound tag is `comp`; it replaces `cmpd`, `compound`, `in cmpd`, `in compound`. | legacy: `_tools/style-spec.md` §4 Tags |
| 2026-10-01 | — | No `---` separator lines between units; `lint --fix` removes them. | legacy: `_tools/style-spec.md` §1 |
| 2026-10-01 | — | BM's *Handa mayaṁ …* leader lines are included as the first unit, unmarked. | `books/01_morning_chanting/texts/CHANGELOG.md`, `books/02_evening_chanting/texts/CHANGELOG.md`, `books/03_reflections/texts/CHANGELOG.md` |
| 2026-10-01 | — | Pāli titles stay (with the incipits for 01/01 and 01/07); *sīladharānaṁ* `(fem)` and *pacchimā-janatānukampa-mānasā* `(nt abl sg comp)` confirmed. | `books/01_morning_chanting/texts/CHANGELOG.md` (S1, second pass) |
| 2026-10-04 | 13 | A present indicative or aorist used as a wish (*homi*, *pariharāmi*, *nivedayuṁ*) is decided case by case; the row keeps its true tag with a note, and the Faithful line says *may…*. | `books/03_reflections/texts/CHANGELOG.md` (S3 follow-up); legacy: `_tools/style-spec.md` §3 |
| 2026-10-04 | 14 | *(Optional)* is a rubric, on its own line above a line BM marks as optional (03/11 *Dasapuññānubhāvena …*). | `books/03_reflections/texts/CHANGELOG.md` (S3 follow-up) |
| 2026-10-04 | 13, 15, 16 | The wish renderings in 03/07 and 03/10 stand; the English titles of 03/04, 03/07, 03/10 and 03/11 are approved. | `books/03_reflections/texts/CHANGELOG.md` (S3 follow-up) |
| 2026-10-04 | 17 | 03/13 keeps BM's *Pasannā hontu* verses. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 18 | 03/19 is Amaravati's version of the path chant, kept with the citation *SN 45.8*. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 19 | 03/12 keeps BM's spelling *pahaṁsāna*. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 20 | The English titles of 03/17 and 03/18 are approved. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 21 | 03/13 keeps the participle reading of *karonte'dha*. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 22 | The leader line of 03/21, probably a local composition, is kept as it is. | `books/03_reflections/texts/CHANGELOG.md` (S4 follow-up) |
| 2026-10-04 | 23 | In 04a/02, six rubrics (*(Before royal ceremonies)* … *(Or, at the monastery, conclude with)*) replace BM's section letters A–F and say when each section is chanted. | `books/04a_parittas/texts/CHANGELOG.md` (S5 follow-up); legacy: `_tools/style-spec.md` §7 |
| 2026-10-04 | 24 | Chants that BM names only in English keep the English name as the `#` title, with no English-title line: 04a/01 *Invitation for Paritta Chanting*, 04a/02 *Invitation to the Devas*. | `books/04a_parittas/texts/CHANGELOG.md` (S5 follow-up); legacy: `_tools/style-spec.md` §1 |
| 2026-10-04 | 25 | The analysis of *omāty-* is kept: DPD *omāti*, with *oṁ + iti* marked `(trad.)`. | `books/04a_parittas/texts/CHANGELOG.md` (S5 follow-up) |
| 2026-10-04 | 26 | BM's explanatory notes are not rubrics and are left out. (Known only as the precedent cited for 04a/24, "as query 26".) | `books/04a_parittas/texts/CHANGELOG.md` (S6) |
| 2026-10-04 | — | *bhaṇāmase* is one word (middle imperative), also where BM spaces it *bhaṇāma se*. | `books/04a_parittas/texts/CHANGELOG.md` |
| 2026-10-04 | 27 | A blessing line with no finite verb (*So attha-laddho sukhito …*) is read as a wish: participle/adjective tags kept with the note `[participle, read here as a wish]`, Faithful *may…*. | `books/04a_parittas/texts/CHANGELOG.md` (25_so_attha_laddho); legacy: `_tools/style-spec.md` §3 |
| 2026-10-04 | 33 | 04b/06 is left as BM prints it (no fourth Thag line). | `books/04b_verses_on_the_dhamma/texts/CHANGELOG.md` (S8, after queries 33–37) |
| 2026-10-04 | 34 | The missing *Pacchima-ovāda-gāthā* is added to 04b, drafted from BM 4.16. | `books/04b_verses_on_the_dhamma/texts/CHANGELOG.md` |
| 2026-10-04 | 35 | An absolutive with no main verb in a blessing (04b/09 *Hantvā tesaṁ upaddave*) is read as a wish: `(abs)` kept with a note, Faithful *may…*. | `books/04b_verses_on_the_dhamma/texts/CHANGELOG.md`; legacy: `_tools/style-spec.md` §3 |
| 2026-10-04 | 36 | 04b/10 *Verses on Respect* takes the English title only, since BM names it only in English. | `books/04b_verses_on_the_dhamma/texts/CHANGELOG.md` |
| 2026-10-04 | 37 | Vinaya citations use SuttaCentral's short display form (`Kd`, `Pvr`, `Bu …`, `Bi …`), e.g. *Kd 1:23.5*, not *Pli Tv Kd 1:23.5*. | `books/04b_verses_on_the_dhamma/texts/CHANGELOG.md`; legacy: `_tools/style-spec.md` §5 |
| 2026-10-04 | 46 | 06/10 gets the rubrics *(For the dead)* and *(For the living)*; no `(×3)` (BM: "often" repeated). | `books/06_funeral_chants/texts/CHANGELOG.md` |
| 2026-10-04 | 48 | BM's misprints in 07a/01 (*Pathamaṁ*, *appativattiyaṁ*, *Veyyākaraṇapāthena*, *maranampi*) are corrected to the retroflex forms. | `books/07a_suttas/texts/CHANGELOG.md` |
| 2026-10-05 | 49 | 07a keeps BM's *viññūṇaṁ* (and *-saññāṇaṁ*), a later commentarial style, with a note. | `books/07a_suttas/texts/CHANGELOG.md` |
| 2026-10-05 | 50 | *sutvā* in *Evaṁ passaṁ …* is `(abs)` "having heard", with Literal and Faithful to match (07a and 03). | `books/07a_suttas/texts/CHANGELOG.md` |
| 2026-10-05 | 51 | BM's omission in *ye loke …* is restored: *upāyupādānā* (from Ṭhānissaro, AN 10.60, DPD). | `books/07a_suttas/texts/CHANGELOG.md` |
| 2026-10-05 | 56 | An identical line whose words have different grammar keeps its own full table (07b/03 *okkamane pubbaṅgamā …*). | legacy: `_tools/style-spec.md` §6; legacy git `e5cd09f` |
| 2026-10-05 | 57 | Words with the preverb *antara-* are single rows, not compounds, although DPD labels them "comp". | legacy: `_tools/style-spec.md` §4; legacy git `3a0a7bb` |
| 2026-10-11 | 58 | *MN 6:2.1* is added to the 08/03 citation; BM's references are kept. | `books/08_patimokkha_chants/texts/CHANGELOG.md` |
| 2026-10-11 | 59 | 08/05: the fifth precept keeps DPD's reading in the Faithful line, with the commentarial reading in the row note. | `books/08_patimokkha_chants/texts/CHANGELOG.md` |
| 2026-10-11 | 60 | The English titles of 08/02, 08/03 and 08/05 are accepted. | `books/08_patimokkha_chants/texts/CHANGELOG.md` |
| 2026-10-23 | — | Source priority: *Bhikkhu Manual*, then the *Community Chanting Book*, then the *Chanting Guide*, then SuttaCentral (book 10 and the Vinaya formulae unchanged). 03/19 (query 18) is compared with the CCB. | `docs/style-spec.md` §2 |
| 2026-10-23 | — | 03/19:425 *ariyo sāvako* is the compound *ariya-sāvako*. | `books/03_reflections/texts/CHANGELOG.md` |
| 2026-10-23 | — | Blank lines and final newlines missing in 03/02–11, 07a/02 and 07a/03 are added, so that every text gives itself back through `draft.py extract`. | `books/03_reflections/texts/CHANGELOG.md`, `books/07a_suttas/texts/CHANGELOG.md` |

## Vinaya formulae (09a–09e)

Founding decisions, all 2026-10-12, from legacy: `_tools/vinaya/prd-vinaya.md` (Decisions):

| Date | ID | Decision | Source |
| :--- | :--- | :--- | :--- |
| 2026-10-12 | — | Source: BM only; fix only obvious misprints, and log them; no Ṭhānissaro or SuttaCentral cross-check. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | One file per procedure, in BM order; BM's text kept as `00_original_*`, never edited, linted or built. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Kept English: only instruction lines (who speaks to whom, when, short setup). Rules and explanations are dropped. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Faithful line = BM's English, ellipses filled from BM's wording; a new rendering only where BM has none; a possible BM mistranslation is kept and queried. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Literal line and tables are new work, with the same rigour as 01–08. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Variants: base formula in full, then a cue and a table for the new words per substitution. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Units identical to settled 01–08 lines are copied verbatim, source cited in the changelog. | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Scope: everything with a formula (bhikkhu formulae, Thai lay requests, forms "from a nun", disrobing). | legacy: `_tools/vinaya/prd-vinaya.md` |
| 2026-10-12 | — | Citations: Vinaya by SuttaCentral short form; commentaries in BM's form (*Sp.III.643*, *Kv.122* = Kaṅkhāvitaraṇī). | legacy: `_tools/vinaya/prd-vinaya.md` |

Queries:

| Date | ID | Decision | Source |
| :--- | :--- | :--- | :--- |
| 2026-10-12 | V1 | Licence: BM's CC BY-NC-ND accepted for filled ellipses in Faithful lines; no permission request. | legacy: `_tools/vinaya/prd-vinaya.md`, `checkpoint.md` |
| 2026-10-12 | V2 | Placeholder names (*Uttaro*, *Tisso*, *Amaro*): option (a), name only: the row gives the tags, the note "[example name; substitute the actual name]", the name and `[proper name]`; no meaning. | legacy: `_tools/vinaya/style-spec.md` §10.4 |
| 2026-10-12 | V3 | BM's English headings stay as titles where BM gives no Pāli name. | legacy: `_tools/vinaya/checkpoint.md` |
| 2026-10-12 | V4 | Book: *Vinaya Formulae*, Pāli subtitle *Vinaya-pāṭha*, five parts with BM's English headings only. | legacy: `_tools/vinaya/checkpoint.md`; legacy git `cc8b001` |
| 2026-10-12 | V5 | Explanation-only sections, with no formula, stay out (only in the originals). | legacy: `_tools/vinaya/checkpoint.md` |
| 2026-10-12 | V6 | BM's slash alternatives become base formula + variants. | legacy: `_tools/vinaya/style-spec.md` §10.3 |
| 2026-10-12 | V7 | (b) BM's *visajjehi* / *visajjetha* kept, not corrected to *vissajj-* (09a/07). | `books/09_vinaya_formulae/01_vinaya_notes_requisites/CHANGELOG.md` |
| 2026-10-12 | V8 | (a) *Bu Pc 59* added after the witness formula in 09a/07. | `books/09_vinaya_formulae/01_vinaya_notes_requisites/CHANGELOG.md` |
| 2026-10-12 | — | The 09a pilot format is approved. | legacy: `_tools/vinaya/checkpoint.md` |
| 2026-10-12 | V9 | (b) The missing clause ("the Community's Kaṭhina has been spread") is added to the 09b/11 Faithful lines. | `books/09_vinaya_formulae/02_vinaya_notes_rains_and_kathina/CHANGELOG.md` |
| 2026-10-12 | V10 | 09c/06 citation *Kd 2:16.1* (BM's *Vin.I.113* gives the rule, not the formula). | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/CHANGELOG.md` |
| 2026-10-12 | V11 | 09c/06: *taṁ* read as BM does ("that"), with the "you" reading of Kd 2:16.1 in the row note. | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/CHANGELOG.md` |
| 2026-10-12 | V12 | 09c/08: new rendering "implored the Unsurpassed One" (DPD *anadhivara*), replacing BM's "requested a favour". | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/CHANGELOG.md` |
| 2026-10-12 | V13 | 09c/07: citation *SN 6.1; MN 26; Kd 1:5.12* added. | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/CHANGELOG.md` |
| 2026-10-12 | V14 | 09c/10: first round copied from 04a/04 with its Faithful, rounds 2–3 with BM's wording: kept. | `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/CHANGELOG.md` |
| 2026-10-12 | V15 | (a) 09d/01 keeps BM's citation form *Vin.IV.122*. | `books/09_vinaya_formulae/04_vinaya_notes_offences/CHANGELOG.md` |
| 2026-10-12 | V16 | (a) 09e/01 keeps BM's citation form *Vin.I.120-129*. | `books/09_vinaya_formulae/05_vinaya_notes_uposatha/CHANGELOG.md` |
| 2026-10-12 | V17 | (b) 09d/18: new rendering "for more than six nights" (*atireka-chā-rattaṁ*). | `books/09_vinaya_formulae/04_vinaya_notes_offences/CHANGELOG.md` |
| 2026-10-12 | V18 | (a) 09e/05 keeps the changed cue (*Āyasmā bhante uttaro bhikkhu* → *Uttaro bhante bhikkhu*). | `books/09_vinaya_formulae/05_vinaya_notes_uposatha/CHANGELOG.md` |
| 2026-10-12 | V19 | (b) 09d/06: *upasaṁkamitvā* added to the plural formula, from the singular. | `books/09_vinaya_formulae/04_vinaya_notes_offences/CHANGELOG.md` |

## Mahāsatipaṭṭhānasutta (10)

Founding decisions, all 2026-10-12, from legacy: `_tools/dn22/prd-dn22.md` (Decisions):

| Date | ID | Decision | Source |
| :--- | :--- | :--- | :--- |
| 2026-10-12 | — | A study text, read, not chanted, for novices: every compound keeps its member rows. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Source: SuttaCentral's Mahāsaṅgīti text only (no BM, no Ṭhānissaro); its 12 *Variant:* notes and first line dropped; checked against SC's bilara root JSON. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | One sentence per unit; long sentences split at clause boundaries. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Refrains written out in full; later identical lines, also in later files, get the repeat note. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Lists that change use the variant method; elisions expanded from the sutta's own wording. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Faithful: new rendering, never checked against published English; *satipaṭṭhāna* = "establishments of mindfulness". | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Row notes from DPD only, no commentary; usually at most one per unit. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Units identical to settled 01–09 lines are copied, adapted to SC spelling and "establishments". | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | One citation per file: the SC segment range. | legacy: `_tools/dn22/prd-dn22.md` |
| 2026-10-12 | — | Book: English title first; About page names SC Mahāsaṅgīti, DPD, and CC BY-NC 4.0 for the English. | legacy: `_tools/dn22/prd-dn22.md` |

Queries:

| Date | ID | Decision | Source |
| :--- | :--- | :--- | :--- |
| 2026-10-12 | D1 | 19 files, one per SC section; SC 7–10 (charnel grounds) as one file. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (answers to S0 queries) |
| 2026-10-12 | D2 | Title plus SC's numbered `###` headings with English glosses. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S0 answers) |
| 2026-10-12 | D3 | Quotation marks dropped; elided *iti* written `'ti`. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S0 answers) |
| 2026-10-12 | D4 | Titles as in the raw split files; *Nigamana* accepted. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S0 answers) |
| 2026-10-12 | D5 | About-page licence wording accepted. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S0 answers) |
| 2026-10-12 | D6 | Key renderings accepted unchanged (style spec §12.2). | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S1 answers) |
| 2026-10-12 | D7 | Clause-level unit size kept. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S1 answers) |
| 2026-10-12 | D8 | Heading-gloss pattern ("Contemplation of the body: the section on …") kept. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S1 answers) |
| 2026-10-12 | D9 | *kaṅkehi* "by kaṅka crows" kept. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S2 answers) |
| 2026-10-12 | D10 | Double quotation marks in the Faithful lines of the copied body-part units in 05 (left to Claude; consistency within 10). | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S2 answers) |
| 2026-10-12 | D11 | The ninth charnel-ground stage stays a variant. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S2 answers) |
| 2026-10-12 | D12 | *sampajānakārī* rendering kept ("acts with clear comprehension"; rows add DPD's "forming a clear perception (of)"). | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S2 answers) |
| 2026-10-12 | D13 | *vicikicchā* stays as full units: a list item with more than three changed words is a full unit. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S3 answers) |
| 2026-10-12 | D14 | *pana* rows follow DPD: "moreover, and so, but" (left to Claude). | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S3 answers) |
| 2026-10-13 | D15 | The inferred year/month dismissals in 19 are kept, including the one-month *ekaṁ māsaṁ*. | `books/10_mahasatipatthanasutta/texts/CHANGELOG.md` (S7) |
| open | D16 | Not answered: should a member that is itself a compound (*mahāpathe* in *catumahāpathe*) get nested member rows? Currently it does not. | legacy: `_tools/dn22/checkpoint.md` |
| open | D17 | Not answered: should etymologies keep the shortened DPD construction (*pajānāti* `[pa + √ñā > jānā + ti]`, asterisks dropped) or follow DPD's full chain? | legacy: `_tools/dn22/checkpoint.md` |
