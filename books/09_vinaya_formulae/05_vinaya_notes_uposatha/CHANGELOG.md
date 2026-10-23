# Changelog: 09e_vinaya_notes_uposatha

## 2026-10-12 — session S5 (consistency, whole-tree index)

### 02_parisuddhi_three_bhikkhus.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| row `aññamaññaṁ` | [añña + añña] | [aññaṁ + aññaṁ] | DPD (sandhi) | `index` |

### 08_patimokkha_in_brief.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| rows `cattāro` (×2) | [catu] | [catu + āro] | DPD; as 09b/01, 09b/05 | `index` |


## 2026-10-12 — Queries V16, V18 answered (bhikkhu), 01, 05

| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | 22 | *Vin.I.120-129* (query V16) | kept | V16 (a): BM's form kept at the bhikkhu's decision | query V16 |
| 05 | 67 | cue written as *Āyasmā bhante uttaro bhikkhu* → *Uttaro bhante bhikkhu* (query V18) | kept | V18 (a) | query V18 |

## 2026-10-12 — session S4 (01–08)

All eight files drafted to spec from `_tools/drafts/09e/gen.py` (writes 01–08.c; b.py). `lint --fix`: no changes; two WARNs: *Vin.I.120-129* (query V16) and `pārisuddhi` `(fem comp)` written apart by BM (02, as S3). Pāli check: 01–04 and 07 identical after normalisation; the rest differ only by BM English and the misprint below; originals untouched (R100). DPD: no flags beyond *uttaro* (proper name, V2) and *pārisuddhiñca* (sandhi). Spot check (with 09d) 10/10. Consistency (`xidx.py`): *dhāre-* etymology aligned with 09c/14 (√dhar + e > dhāre); *paṇṇaraso* aligned with 05_/01 (masc, in apposition); other divergences are grammar-driven.

Applies to all files: BM's quotation marks and the quotes/italics round *Uttaro* dropped; Pāli prose divided where BM's English sentences end; BM's "Sangha" kept in copied Faithful lines.

| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | 22 | *Vin.I.120-129* | kept | BM's form kept, V16 (a) | query V16 |
| 03 | 10 | — | I, friend, am quite pure. Understand that I am quite pure. | new rendering (from BM's wording in 02) | spec §10.2 |
| 05 | 43 | acknowedges | acknowledges | English typo | spec §10.2 |
| 05 | 67 | cue *Āyasmā bhante uttaro* → *Uttaro bhante bhikkhu* | *Āyasmā bhante uttaro bhikkhu* → *Uttaro bhante bhikkhu* | BM's cue would give *bhikkhu bhikkhu* (base has *bhikkhu*); inference; kept, V18 (a) | query V18 |
| 08 | 3 | rules and explanation | one instruction line | spec §10.1 | — |
| 08 | 5 | *nidānam* | *nidānaṁ* | misprint (niggahīta) | spec §2, §10.6 |
| 08 | 5–166 | — | Literal and Faithful for all twelve lines | new rendering (BM has none) | spec §10.2 |

## 2026-10-12 — session S0 (split of BM original)

BM's `uposatha.md` (baseline commit e3f3bb5) renamed `00_original_uposatha.md`: kept unchanged, never linted or built; it is the reference for the Pāli check (`compare --vinaya`). Split into one raw file per procedure with `_tools/vinaya/split_originals.py`: a `#` title and `*English title*` from BM's heading, then BM's lines verbatim (Contents block and `<a id>` anchors removed). Not yet to spec.

| File | Original lines | Title |
| :--- | :--- | :--- |
| 01_parisuddhi_before_sangha.md | 16–26 | Pārisuddhi-uposatha — Purity Uposatha: Before the Saṅgha |
| 02_parisuddhi_three_bhikkhus.md | 28–55 | Pārisuddhi-uposatha — Purity Uposatha: Three Bhikkhus |
| 03_parisuddhi_two_bhikkhus.md | 57–65 | Pārisuddhi-uposatha — Purity Uposatha: Two Bhikkhus |
| 04_adhitthanuposatha.md | 67–74 | Adhiṭṭhānuposatha — For a Lone Bhikkhu |
| 05_sick_parisuddhi.md | 76–101 | Pārisuddhi — Sick Bhikkhus: Conveying Purity |
| 06_sick_chanda.md | 103–126 | Chanda — Sick Bhikkhus: Sending Consent |
| 07_sick_parisuddhi_and_chanda.md | 128–137 | Pārisuddhi and Chanda — Sick Bhikkhus: Purity and Consent |
| 08_patimokkha_in_brief.md | 139–173 | Reciting the Pāṭimokkha in Brief |
