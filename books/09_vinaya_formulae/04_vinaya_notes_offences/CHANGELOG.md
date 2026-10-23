# Changelog: 09d_vinaya_notes_offences

## 2026-10-12 — Queries V15, V17, V19 answered (bhikkhu), 06, 18

| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | 223 | *Vin.IV.122* (query V15) | kept | V15 (a): BM's form kept at the bhikkhu's decision | query V15 |
| 06 | 26–33 | plural formula without *upasaṁkamitvā* (as BM) | *Imāni me bhante cīvarāni aññātakaṁ gahapatikaṁ upasaṁkamitvā tat'uttariṁ viññāpitāni nissaggiyāni.* | V19 (b): word added from the singular formula; Literal "[an] unrelated householder having approached", row added | query V19 |
| 18 | 8 | "for a night" (BM, copied from NP 2) | "for more than six nights" | V17 (b): new rendering; the Pāli is *atireka-chā-rattaṁ* | query V17 |

## 2026-10-12 — session S4 (01–19)

All nineteen files drafted to spec from `_tools/drafts/09d/01.c` and `gen.py` (writes 02–19.c; b.py). `lint --fix`: no changes; one WARN (*Vin.IV.122*, kept, V15). Pāli check (`compare --vinaya`): every difference is BM English, a filled elision or a written-out returning formula (below); originals untouched (R100). DPD: 1 flag explained (*thullaccaya* used adjectivally); not-found forms are inflections (*accayāyo*, *viññāpitāni*). DPD: *paṭiggahesiṁ* → pati + √gah > gahe + siṁ; *samāpajjiṁ* → saṁ + ā + √pad > pajja + iṁ; *attano* → atta + no. Spot check (independent subagent) 10/10; its note applied: *accaya* member rows marked "noun used adjectivally" (01).

Applies to all files: BM's quotation marks dropped; BM's PTS citations mapped to *Bu NP n* (each page falls in that rule); NP frame rows identical across files (*me* = `(1st sg instr)`, agent of *nissaggiya*); *bhante* `(masc voc pl)` where BM addresses the Saṅgha ("Ven. sirs": 10, 11, 14), else sg. BM's "This formula for returning the article(s) also applies in NP. 2, 3, 6, 7, 8, 9, 10" written out: each of those files carries *Imaṁ cīvaraṁ āyasmato dammi* (BM's Faithful from NP 1), with the plural variant where the file has a plural formula.

### 01_apatti_patidesana.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | (Thai Formula); **JB**/**SB** | instruction lines; speakers written out | spec §10.1 | — |
| 155–177 | "replacing *thullaccayāyo* with …"; "with *dubbhāsitāyo* omit *nānā-vatthukāyo*"; *sambahulā* → *dve* | four variants; *dubbhāsita* cue replaces both words | variant blocks | spec §10.3 |
| 181 | *Sambahulā … tā paṭidesemi* → *Ekaṁ … taṁ paṭidesemi* | full formula *Ahaṁ bhante ekaṁ thullaccayaṁ āpattiṁ āpanno taṁ paṭidesemi.* | elision filled (*Ahaṁ bhante* from BM's base); more than three words change | spec §10.3 |
| 183 | — | I, ven. sir, having fallen into one grave offence, this I confess. | new rendering (BM has none) | spec §10.2 |
| 199–219 | — | variants *bhante* → *āvuso* (senior confessing); *pācittiyaṁ*, *dukkaṭaṁ*, *dubbhāsitaṁ* | BM's list; the senior form follows BM's dialogue | spec §10.3, §10.5 |
| 223 | *Vin.IV.122* | kept | BM's form kept, V15 (a) | query V15 |
| 225–241 | NP section (prose, link) | instruction line + two variants (*nissaggiyāyo pācittiyāyo*; *nissaggiyaṁ pācittiyaṁ*); *Vin.III.196f* → *Bu NP 1* | variant blocks; citation mapped | spec §10.3, §5 |

### 02_np_01_extra_robe.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 31 | — | These robes, ven. sir, which have passed beyond the ten day (limit), are to be forfeited by me: I forfeit them to you. | new rendering | spec §10.2 |
| 49 | *āyasamato* | *āyasmato* | misprint | spec §10.6 |
| 53 | *āysamantānaṁ* | *āyasmantānaṁ* | misprint | spec §10.6 |
| 65–77 | four forearm pairs in one list | two variants (singular, plural) | variant blocks | spec §10.3 |

### 03_np_02_separated_from.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 28–42 | *dvicīvaraṁ*/*ticīvaraṁ* | two variants; *dvicīvara* not in DPD (noted in the row) | slash alternatives | V6 |
| 44 | — | returning formula | written out from NP 1 | spec §10.3 |

### 04, 05, 06 (NP 3, 6, 7)

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 31 | — | plural Faithful line (*These … robes …, are to be forfeited by me: I forfeit them to you.*) | new rendering | spec §10.2 |
| ~49 | — | returning formula + plural variant | written out from NP 1 | spec §10.3 |
| 06: 26 | plural formula lacks *upasaṁkamitvā* | word added (see above) | V19 (b) | query V19 |
| 06: 18 | *upasaṁkamitvā* | kept (BM *-ṁk-*; DPD *-ṅk-*), noted in the row | BM spelling | spec §2 |

### 07–09 (NP 8, 9, 10)

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 08: 5–10 | "Use formula of NP 8 but change *aññātakaṁ gahapatikaṁ* → *aññātake gahapatike*" | full formula written out | each file stands alone | spec §10.3 |
| 08: 10 | — | Faithful from NP 8 with "unrelated householders" | new rendering | spec §10.2 |
| 07–09: ~30 | (08: "see NP 1") | returning formula | written out from NP 1 | spec §10.3 |

### 10–19 (NP 18–30)

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10–12 | one Pāli sentence pair | divided after *paṭiggahesiṁ* / *samāpajjiṁ*, where BM's first English sentence ends | spec §2 | — |
| 10, 11, 14 | "To be forfeited to the Sangha only." | instruction line | situation | spec §10.1 |
| 17: 9 | BM's Faithful (lacks "which") | kept | BM wording | spec §10.2 |
| 18: 8 | "for a night" (as NP 2) | kept; Pāli *atireka-chā-rattaṁ* = more than six nights | suspected BM error | query V17 |
| 19: 26–31 | *Imaṁ āyasmato dammi* (no English) | Faithful "I give this to you." | new rendering | spec §10.2 |

## 2026-10-12 — session S0 (split of BM original)

BM's `offences.md` (baseline commit e3f3bb5) renamed `00_original_offences.md`: kept unchanged, never linted or built; it is the reference for the Pāli check (`compare --vinaya`). Split into one raw file per procedure with `_tools/vinaya/split_originals.py`: a `#` title and `*English title*` from BM's heading, then BM's lines verbatim (Contents block and `<a id>` anchors removed). Not yet to spec.

| File | Original lines | Title |
| :--- | :--- | :--- |
| 01_apatti_patidesana.md | 58–144 | Āpatti-paṭidesanā — Confession of Offences |
| 02_np_01_extra_robe.md | 146–183 | Nissaggiya Pācittiya 1 — Extra Robe |
| 03_np_02_separated_from.md | 185–196 | Nissaggiya Pācittiya 2 — Separated From |
| 04_np_03_over_kept_cloth.md | 198–209 | Nissaggiya Pācittiya 3 — Over-kept Cloth |
| 05_np_06_asked_for.md | 211–224 | Nissaggiya Pācittiya 6 — Asked For |
| 06_np_07_beyond_limit.md | 226–239 | Nissaggiya Pācittiya 7 — Beyond Limit |
| 07_np_08_instructing.md | 241–250 | Nissaggiya Pācittiya 8 — Instructing |
| 08_np_09_instructing.md | 252–261 | Nissaggiya Pācittiya 9 — Instructing |
| 09_np_10_reminding.md | 263–272 | Nissaggiya Pācittiya 10 — Reminding |
| 10_np_18_gold_and_silver.md | 274–283 | Nissaggiya Pācittiya 18 — Gold and Silver |
| 11_np_19_monetary_exchange.md | 285–295 | Nissaggiya Pācittiya 19 — Monetary Exchange |
| 12_np_20_buying_and_selling.md | 297–310 | Nissaggiya Pācittiya 20 — Buying and Selling |
| 13_np_21_extra_bowl.md | 312–324 | Nissaggiya Pācittiya 21 — Extra Bowl |
| 14_np_22_new_bowl.md | 326–336 | Nissaggiya Pācittiya 22 — New Bowl |
| 15_np_23_kept_tonics.md | 338–351 | Nissaggiya Pācittiya 23 — Kept Tonics |
| 16_np_25_snatched_back.md | 353–361 | Nissaggiya Pācittiya 25 — Snatched Back |
| 17_np_28_urgent.md | 363–371 | Nissaggiya Pācittiya 28 — Urgent |
| 18_np_29_wilderness_abode.md | 373–381 | Nissaggiya Pācittiya 29 — Wilderness Abode |
| 19_np_30_diverted_gain.md | 383–394 | Nissaggiya Pācittiya 30 — Diverted Gain |

Not carried into any file (explanation only, no formula; spec §10 keeps only who speaks, when, and short setup): lines 32–56; lines 396–410. The text stays in the original.
