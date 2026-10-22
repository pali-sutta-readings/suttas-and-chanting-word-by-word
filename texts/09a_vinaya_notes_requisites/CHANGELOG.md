# Changelog: 09a_vinaya_notes_requisites

## 2026-10-12 — Queries V7, V8 answered (bhikkhu), 07_vikappana_paccuddharana.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20, 39 | row note "query V7" | "kept at the bhikkhu's decision, V7" | V7 (b): BM's *visajjehi* / *visajjetha* kept, not corrected to *vissajj-* | query V7 |
| 86 | no citation after the witness formula | *Bu Pc 59* | V8 (a) | query V8 |

## 2026-10-12 — session S1 (01–07, pilot)

All seven files drafted to spec from `_tools/drafts/09a/NN.c` (b.py). `lint --fix`: no changes in any file. Pāli check (`compare --vinaya`): every difference is BM English or BM's item list, now variant cues; originals untouched (R100). Spot check 10/10.

Applies to all files: BM's instruction text kept only where it says who speaks, when or in what situation (rules, notes and links dropped; the original keeps them); BM's PTS citations mapped to SuttaCentral IDs (Vin.IV.120 = *Bu Pc 58*, Vin.IV.122 = *Bu Pc 59*, both checked against SC's PTS page references); placeholder names tagged `[proper name]` (V2).

### 01_bindu.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20 | Vin.IV.120 | Bu Pc 58 | citation mapped | spec §5 |

### 02_adhitthana.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | Pali | Pāli | spelling in instruction line | spec §3 |
| 18–83 | item list for *saṅghāṭiṁ* | nine variants; *imaṁ* on both sides where its gender changes (masc: *uttarā-saṅgaṁ*, *antara-vāsakaṁ*, *pattaṁ*; nt: *nisīdanaṁ*, *paccattharaṇaṁ*, *-colaṁ*) | variant blocks | spec §10.3 |
| 73, 83 | *-colaṁ* | tagged nt, against DPD's masc *mukhapuñchanacoḷa*, *parikkhāracoḷa* | BM's own plurals *-colāni* are nt; DPD has *coḷa* as masc and nt (inference) | DPD |
| 73–120 | *cola* | kept | BM's spelling; DPD *coḷa*; noted in the rows | spec §10.6 |
| 92 | — | instruction line written for *Imāni paccattharaṇāni* | BM's rule (no limit on number) restated as situation | spec §10.1 |
| 128 | Sp.III.643-644 | Sp.III.643–644 | en dash, as in the spec | spec §5 |

### 03_paccuddharana.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 18–43 | "Substitute the appropriate item" | four variants (upper robe, lower robe, bowl, sitting-cloth), Pāli forms from BM's list in 02 | BM's item list written out; each file stands alone | spec §10.3 |
| 50 | Sp.III.643 (after the formula) | after the last variant | citation under the last variant it covers | spec §1 |

### 04_vikappana_general.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 22 | … these robes … | I share these robes with you. | elision filled | spec §10.2 |
| 34 | … this bowl … | I share this bowl with you. | elision filled | spec §10.2 |
| 46 | … these bowls … | I share these bowls with you. | elision filled | spec §10.2 |
| 75 | Vin.IV.122 | Bu Pc 59 | citation mapped | spec §5 |

### 05_vikappana_by_name.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 33–55 | "substitute as in Generally Addressing" (plural, beyond forearm's length) | written out: bowl, plural (*imāni cīvarāni*, *ime patte*), *etaṁ*/*etāni*/*ete* | each file stands alone | spec §10.3 |
| 57 | Vin.IV.122 | Bu Pc 59 | citation mapped | spec §5 |

### 06_vikappana_absent.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 22–38 | bowl, plural and forearm cues after the citation | variant blocks directly after the formula they change (*Imaṁ cīvaraṁ vikappanatthāya …*) | variants follow their base formula | spec §10.3 |
| 46, 64, 80, 93 | — | instruction lines from BM's prose (*The witness should then ask …*, *The original owner tells their names*, *The witness then says*, *Or the witness says*) | dialogue turns | spec §10.1 |
| 108 | Vin.IV.122 (before the cues) | Bu Pc 59, at the end | citation under the last unit | spec §1, §5 |

### 07_vikappana_paccuddharana.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20, 39 | *visajjehi*, *visajjetha* | kept | DPD gives "give away" only under *vissajjeti*; *visajjeti* = "answers"; BM itself has *vissajjehi* at line 69 | query V7 |
| 17, 32, 55, 77 | *santakaṁ* | tagged as noun (nt, "property") in apposition | DPD *santaka* 2.1; also fits *tesaṁ santakaṁ* (inference) | DPD |
| 49 | "alter according to Generally Addressing" (bowls) | *imaṁ pattaṁ* → *ime patte*; *santakaṁ* → *santakāni* | written out; *santakāni* taken from BM's own robe cue (inference) | spec §10.3 |
| 57 | *imaṁ* → *etaṁ*; *imāni* → *etāni* | one cue with *ime* → *ete* added, after the bowl cues | covers bowls; from BM's 04 | spec §10.3 |
| 65 | Kv.122 (after the formula) | after the last variant | citation under the last variant it covers | spec §1 |
| 17, 32, 55, 77 | etymology [sa + nta + ka] | [√as > sa + nta + ka] | DPD root √as | DPD |

## 2026-10-12 — session S0 (split of BM original)

BM's `requisites.md` (baseline commit e3f3bb5) renamed `00_original_requisites.md`: kept unchanged, never linted or built; it is the reference for the Pāli check (`compare --vinaya`). Split into one raw file per procedure with `_tools/vinaya/split_originals.py`: a `#` title and `*English title*` from BM's heading, then BM's lines verbatim (Contents block and `<a id>` anchors removed). Not yet to spec.

| File | Original lines | Title |
| :--- | :--- | :--- |
| 01_bindu.md | 14–20 | Bindu — Marking |
| 02_adhitthana.md | 22–62 | Adhiṭṭhāna — Determining |
| 03_paccuddharana.md | 64–76 | Paccuddharaṇa — Relinquishing |
| 04_vikappana_general.md | 78–109 | Vikappana — Sharing Ownership: Generally Addressing the Recipient |
| 05_vikappana_by_name.md | 111–131 | Vikappana — Sharing Ownership: Addressing the Recipient by Name |
| 06_vikappana_absent.md | 133–166 | Vikappana — Sharing Ownership: Receiving Bhikkhu is Absent |
| 07_vikappana_paccuddharana.md | 168–208 | Vikappana-paccuddharaṇa — Relinquishing Shared Ownership |
