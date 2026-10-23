# Changelog: 04b_verses_on_the_dhamma

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 06_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 84 | *viharissanti* vi + √har + issa +  | vi + √har + a + issa > harissa +  | DPD future-stem construction | DPD viharissati |


## 2026-10-05 — session S19c (cross-file index, from 07b_anagatabhaya_suttas)

Step-9 alignment after 07b was completed: each word now has the DPD analysis in every file.

### 06_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 128 | sad `(adj comp)` | `(ind comp)` | DPD: sat is ind, in comps | DPD sat 1 |
| 128 | sad **[sat, no root in DPD]** | **[√as + a > sa + nta > sat]** | DPD gives a root | DPD sat 1 |

## 2026-10-05 — session S18b (step 9: index alignment for 07a)

Etymologies aligned across the checked subfolders (01–07a) to the DPD constructions used in 07a (S12–S18b), from the `index` report. Same lemma, same analysis in every file; homonyms, sandhi rows and bare-lemma variants were left.

### 05_ti_lakkhan_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 35 | nibbindati [nī + √vid > vind + a + ti] | [nī + √vid > vinda + ti] | align with DPD construction | DPD nibbindati |

## 2026-10-04 — session S9b (cross-file index, from 05_anumodanas)

### 01_pabbatopama_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 187 attano | [atta, no root in DPD] | [atta + no] | same word, one analysis | DPD attano |

## 2026-10-04 — session S8, after queries 33–37 (bhikkhu, same day)

Query 33: 04b/06 left as BM prints it (no fourth Thag line). Query 37: the script's citation check now accepts SuttaCentral's short Vinaya IDs (`Kd`, `Pvr`, `Bu …`, `Bi …`).

### 07a_pacchima_ovada_gatha.md (new file)
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | — (chant missing from the tree) | *Pacchima-ovāda-gāthā*, 4 units, 17 rows, drafted from BM 4.16; exact against BM | query 34 | BM 4.16; DN 16:6.7 |

### 08_ye_dhamma_hetuppabhava.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 57 | *Pli Tv Kd 1:23.5* | *Kd 1:23.5* | short Vinaya ID | query 37; spec §5 |

### 09_nakkhattayakkha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 41 | Faithful "having struck down their calamities." | "may their calamities be struck down." | absolutive without main verb read as a wish | query 35; spec §3 |
| 45 | *hantvā* `(abs)` having struck down | note `[absolutive with no main verb, read here as a wish]` added | as above | query 35 |

### 10_verses_on_respect.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `# Satthu-garu dhamma-garu` + `*Verses on Respect*` | `# Verses on Respect` (English title only) | BM names it only in English | query 36; spec §1 |

## 2026-10-04 — session S8, step 9 (index alignment after 04b was completed)

Same lemma analysed two ways in the checked files (01–03, 04a, 04b): the DPD construction is now used in all of them (local DPD, release 26 Sept 2026). Homonyms (*no*, *santo*, *pattiyā*) and context-dependent tags were left.

### 03_khemakhema_sarana_gamana_paridipika_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 184 | *aṭṭh'* [aṭṭha] | [aṭṭha, no root in DPD] | same word, one form (as 03/19) | DPD |

### 06_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 217 | *sukham-āvahāti* [√sukh + a; + ā + √vah + a + ti] | [√sukh + a + ā + √vah + a + ti] | same word, one form (as 03/18) | — |

## 2026-10-04 — session S8 (04b_verses_on_the_dhamma, all 10 files)

All ten files were in pre-spec form (English `###` headings, no `*English title*` lines, no citations, no ↳ member rows, non-canonical tags such as `(ind adv)`, `(ind pot)`, `(nt acc sg indef)`, `(3rd sg opt caus)`, Sanskrit-style roots such as *√vart*, `[cite: n]` tags in 09, Faithful lines close to BM's English). As in S5–S7, the Literal/Faithful lines and word tables were redrafted unit by unit from the Pāli and the local DPD database (release 26 Sept 2026); the Pāli was kept except where noted. Every file is exact against BM 4.9–4.19 (checked with `sub.py`). `lint --fix` safe fixes were applied first. 145 Pāli lines, 504 word rows (incl. ↳ member rows).

### All files
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `# Title` + `### English heading` (or none) | `# Pāli title` + `*English title*` | title rule | spec §1 |
| all | tags `(ind adv)`, `(ind pot)`, `(nt acc sg indef)`, `(3rd sg opt caus)`, `(3rd sg pres act)` (no mood), `(masc nom sg adj)` order | canonical tags; every compound with ↳ member rows | tags; compounds | spec §4 |
| all | roots such as *adhi-√vart*, *√madd*, *[nabhas]*, *[pusa]*, *[silā + a]*, *[pāṇa + in]* | DPD constructions (*adhi + √vatt + a + nti*, *√ar + tha*, *purisa > porisa > posa*, etc.) | wrong or invented roots | DPD |
| all | Faithful lines echoing BM's English | new Faithful lines from the Pāli and DPD | spec §3 | spec §3 |
| end | no citation | SuttaCentral citation | citations | spec §5 |

### 01_pabbatopama_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `### Verses on Mountains` | `*Verses on the Simile of the Mountains*` | title | spec §1 |
| — | *pattiyā* [pa + √ap + ti] "attainment" | [√pad + ti] "infantry" | wrong homonym | DPD patti 2.1 |
| — | *sakkā* `(ind pot)` | `(ind)` [√sak + yā] | tag | DPD sakkā 1 |
| end | — | *SN 3.25* | citation (BM S.I.102) | SuttaCentral |

### 02_bhara_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | Pāli lines not recognised by `stats` (0 lines) | standard units | format | spec §1 |
| end | — | *SN 22.22* | citation (BM S.III.26) | SuttaCentral |

### 03_khemakhema_sarana_gamana_paridipika_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| last | *pamuccatī'ti.* | full stop removed | punctuation | spec §2 |
| end | — | *Dhp 188–192* | citation | BM |

Line order *n'etaṁ saraṇam-uttamaṁ* / *N'etaṁ saraṇam-āgamma* kept (Dhp 189); BM's different order is a two-column PDF artefact.

### 04_bhadd_eka_ratta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| — | *viddhām-* `(abs)` [√vid + tvā] "having known" | `(masc nom sg)` BM's spelling of *vidvā* (*vidvant*) with *-m-*: "the wise one" | grammar | DPD vidvant; MN 131 |
| end | — | *MN 131* | citation (BM M.III.187) | SuttaCentral |

### 05_ti_lakkhan_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | no English title | *Verses on the Three Characteristics* | title (BM's English heading) | spec §1 |
| 6 lines | lines 6–8 and 10–12 written out in full | repeat note | repeats | spec §6 |
| — | — | *Dhp 277–279* after line 12; *Dhp 85–89* at the end | citations | BM; Dhp |

### 06_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `### Verses on Respect for the Dhamma` | `*Verses on Reverence for the Dhamma*` | title; same as 03/18 | spec §1 |
| — | rows for lines shared with 03/18 | rows aligned with 03/18 (except *adhammo* and *mahattam-abhikaṅkhatā*, now DPD; 03/18 aligned in step 9) | consistency | DPD |
| — | — | *SN 6.2* after line 12; *Thag 4.10* at the end | citations (BM S.I.140, Thag 303–304) | SuttaCentral |

### 07_pathama_buddha_bhasita_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `### Verses on the Buddha's First Exclamation` | `*Verses of the Buddha's First Utterance*` | title | spec §1 |
| end | — | *Dhp 153–154* | citation | BM |

### 08_ye_dhamma_hetuppabhava.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Ye Dhammā Hetuppabhavā` | `# Ye dhammā hetuppabhavā` | BM capitalisation | BM 4.17 |
| end | — | *Pli Tv Kd 1:23.5* | citation (BM Mv.1.23.5); form accepted by the script's citation check | SuttaCentral pli-tv-kd1 |

### 09_nakkhattayakkha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | one-row tables for compounds, Pāli lines not recognised by `stats` | whole-compound rows with ↳ members | spec §4 | spec §4 |
| 4 | — | *(×3)* on the last line | BM "(Three times)" | BM 4.18 |
| — | *Pāpa-ggaha-nivāraṇā* `(fem nom sg)`, one row | `(nt abl sg comp)` with ↳ members | grammar | DPD nivāraṇa |
| — | Faithful "May their afflictions … be destroyed" | "having struck down their calamities" | *hantvā* is an absolutive, not a wish (see query) | grammar |

### 10_verses_on_respect.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–3 | `# Verses on Respect` + `### A.IV.28` | `# Satthu-garu dhamma-garu` + `*Verses on Respect*` | Pāli title from the incipit; heading was a citation | spec §1 |
| end | — | *AN 7.32* | citation (BM A.IV.28) | SuttaCentral an7.32 |


## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 05_ti_lakkhan_adi_gatha.md | 16 etymologies | aligned: *anattā*, *aniccā*, *cittaṁ*, *dukkhe*, *passati*, *paññāya*, *paṇḍito*, *saṅkhārā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 01_pabbatopama_gatha.md | 6 etymologies | aligned: *dhamma-cārī*, *kāyena*, *pattiyā*, *paṇḍito*, *pi* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 04_bhadd_eka_ratta_gatha.md | 1 etymologies | aligned: *maraṇaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 06_dhamma_garav_adi_gatha.md | 25 etymologies | aligned: *adhammo*, *anāgatā*, *atta-kāmena*, *atītā*, *bahunnaṁ*, *dhamma-cāriṁ*, *dhammatā*, *garu-kātabbo*, *neti*, *nirayaṁ*, *pi*, *pāpeti*, *saddhamma-garuno*, *saddhammo*, *sama-vipākino*, *sambuddhā*, *saraṁ*, *soka-nāsano*, *suciṇṇe*, *suciṇṇo*, *tasmā*, *ubho*, *viharissanti*, *vihariṁsu* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_bhara_sutta_gatha.md | 1 etymologies | aligned: *sukhaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 03_khemakhema_sarana_gamana_paridipika_gatha.md | 3 etymologies | aligned: *maggaṁ*, *passati*, *yanti* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 10_verses_on_respect.md | 1 etymologies | aligned: *ātāpī* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 01_pabbatopama_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 227 | saṅghe [saṁ-√han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 254 | kāyena [kāya] | [√ci + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 265 | vācāya [vāc] | [√vac + ā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 267 | cetasā [cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 03_khemakhema_sarana_gamana_paridipika_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | saraṇaṁ [√sr + -ana > saraṇa] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 69 | saraṇaṁ [√sr + -ana > saraṇa] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 135 | saraṇaṁ [√sr + -ana > saraṇa] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 148 | ariya [√ar + -iya] | [ariya, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 174 | dukkhassa [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 187 | dukkhassa [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 229 | saraṇaṁ [√sr + -ana > saraṇa] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_ti_lakkhan_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | 'ti [sandhi of iti] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 58 | 'ti [sandhi of iti] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 103 | 'ti [sandhi of iti] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 393 | 'ti [sandhi of iti] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 06_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 43 | sambuddho [saṁ-√budh + ta] | [saṁ + √budh + ta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 10_verses_on_respect.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24 | saṅghe [saṁ + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 02_bhara_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 39 | dukkhaṁ [du- + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 40 | loke [loka (√luj + -a)] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 03_khemakhema_sarana_gamana_paridipika_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 107 | dukkhā [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 147 | cattāri [catu] | [catu + āri] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 173 | dukkhaṁ [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 267 | dukkhā [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 05_ti_lakkhan_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 12 | aniccā [an- + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 57 | dukkhā [du- + √kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 102 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 07_pathama_buddha_bhasita_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 50 | dukkhā [du- + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 08_ye_dhamma_hetuppabhava.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 26 | tathāgato [tathā + gata] | [tathā + gata (√gam + ta) / tatha + āgata] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01_pabbatopama_gatha.md | 63 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 04_bhadd_eka_ratta_gatha.md | 165 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_ti_lakkhan_adi_gatha.md | 10 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |
| 05_ti_lakkhan_adi_gatha.md | 55 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |
| 05_ti_lakkhan_adi_gatha.md | 100 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |

