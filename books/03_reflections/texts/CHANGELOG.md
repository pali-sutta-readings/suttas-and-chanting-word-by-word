# Changelog: 03_reflections

## 2026-10-26 — DPD check corrections (10, 13)

Rows corrected after the first full `make dpd-check` review (docs/legacy-migration.md, "DPD check review"). Only the etymology changed; the Pāli, renderings and tags are unchanged. Lint: 0 ERROR, 0 STRAY, 0 WARN in the changed files, as before; `simsapa.py check`: the corrected rows match DPD; `index.py`: no conflicts.

### 10_sabba_patti_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 211 | *nivedayuṁ* [ni + √vid + e + aya + uṁ] | [ni + √vid + aya + uṁ] | DPD has the single causative sign *aya*; *e* removed | DPD nivedayi (ni + √vid + *aya > vedaya + i) |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 102 | ↳ *patī* [pati, no root in DPD] | [√pat + i] | DPD gives *pati* (lord, master) the root √pat | DPD pati 2.1 |

## 2026-10-23 — 19: *ariya-sāvako*

The compound *ariya-sāvako* had been written as two words. The Community Chanting Book and SuttaCentral (SN 45.8) both have *ariyasāvako*; found by `make compare` against the CCB. Lint unchanged; compare: the item is gone.

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 425 | *Idha bhikkhave ariyo sāvako micchā-ājīvaṁ …* | *Idha bhikkhave ariya-sāvako micchā-ājīvaṁ …* | compound, as in the source | CCB; SN 45.8; maintainer, 2026-10-23 |
| 427 | Literal *a-noble disciple* | *a-noble-disciple* | follows the compound | spec §3 |
| 434–435 | rows *ariyo* (adj masc nom sg), *sāvako* (masc nom sg) | *ariya-sāvako* (masc nom sg comp) with ↳ *ariya*, ↳ *sāvako* | follows the compound | spec §4 (compounds); 07a/02, 07a/03 rows for *ariyasāvako* |

## 2026-10-23 — layout fixes (no change to the wording)

Blank lines and final newlines added where the layout differed from the style spec, so that `scripts/draft.py extract` gives each file back; found by the round-trip check (docs/legacy-migration.md, "Layout findings"). Maintainer's decision, 2026-10-23. Lint and compare results unchanged.

### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 21 | no blank line before *Jarā-dhammomhi jaraṁ anatīto* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 230 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20 | no blank line before *Dasa ime bhikkhave dhammā pabbajitena …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 270 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 04_caturappamanna_obhasana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 19 | no blank line before *Mettā-sahagatena cetasā ekaṁ disaṁ …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 284 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 19 | no blank line before *Ajja mayā apaccavekkhitvā yaṁ cīvaraṁ …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 294 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 06_reflection_on_the_off_putting_qualities_of_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20 | no blank line before *Yathā paccayaṁ pavattamānaṁ …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 263 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 18 | no blank line before *Ahaṁ sukhito homi niddukkho homi, avero …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 134 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 08_reflection_on_the_unconditioned.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 19 | no blank line before *Atthi bhikkhave ajātaṁ abhūtaṁ akataṁ …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 98 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 09_reflection_on_the_thirty_two_parts.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 178 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 10_sabba_patti_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20 | no blank line before *Puññass'idāni katassa* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 273 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 288 | no newline at the end of the file | final newline | style spec §1 layout | maintainer, 2026-10-23 |

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 01_reflection_on_the_four_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 141 | *bhavissati* √bhū + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |

### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 117, 220 | *bhavissāmi* √bhū + issa + mi | √bhū + a + issa > bhavissa + mi | DPD future-stem construction | DPD bhavissati 1 |

### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 175, 248 | *bhavissāmī'ti* √bhū + issa + mi; + iti | √bhū + a + issa > bhavissa + mi; + iti | DPD future-stem construction | DPD bhavissati 1 |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 188 | *bhavissati* √bhū + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 124 | *karissanti* √kar + issa +  | √kar + o + issa > karissa +  | DPD future-stem construction | DPD karissati 1 |
| 131 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 181 | *bhavissatī'ti* √bhū > bhava + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |
| 371 | *bhavissati* √bhū + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |
| 419 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |
| 460, 508 | *appamādena* na > a + pa + √mad + a | na > a + pa + √mad > mād + a | DPD construction | DPD appamāda |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 83 | *viharissanti* vi + √har + issa +  | vi + √har + a + issa > harissa +  | DPD future-stem construction | DPD viharissati |


## 2026-10-11 — session S21 step 9 (cross-file index, from 08_patimokkha_chants)

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 294 | ↳ musā [musā] | [√mus + ā] | DPD construction | DPD musā 2 |
| 295 | ↳ vādā [√vad + a] | [√vad > vād + a] | DPD construction | DPD vāda 2 |
| 369 | ↳ atipātā [ati + √pat > pāt + a] | [ati + √pat + e > pāte + a] | DPD construction (causative base) | DPD atipāta |
| 380 | ↳ adinn' [na > a + √dā + na] | [na > a + √dā > dī + na] | DPD construction | DPD adinna 1.1 |

## 2026-10-05 — session S19c (cross-file index, from 07b_anagatabhaya_suttas)

Step-9 alignment after 07b was completed: each word now has the DPD analysis in every file.

### 01_reflection_on_the_four_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 146 | vihāro **[vi + √har + a]** | **[vi + √har > hār + a]** | align with DPD construction | DPD vihāra 1 |
| 159 | sena **[√sī + ana]** | **[√sī > say + ana]** | align with DPD construction | DPD sena 1.1 |

### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 42 | byādhi **[vi + ā + √dhā + i]** | **[vi > vy > by + ā + √dhā + i]** | align with DPD construction | DPD byādhi |
| 156 | byādhi **[vi + ā + √dhā + i]** | **[vi > vy > by + ā + √dhā + i]** | align with DPD construction | DPD byādhi |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 193 | vihāro **[vi + √har + a]** | **[vi + √har > hār + a]** | align with DPD construction | DPD vihāra 1 |
| 208 | sena **[√sī + ana]** | **[√sī > say + ana]** | align with DPD construction | DPD sena 1.1 |

### 06_reflection_on_the_off_putting_qualities_of_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 172 | sena **[√sī + ana]** | **[√sī > say + ana]** | align with DPD construction | DPD sena 1.1 |
| 197 | sena **[√sī + ana]** | **[√sī > say + ana]** | align with DPD construction | DPD sena 1.1 |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 216 | sad `(adj comp)` | `(ind comp)` | DPD: sat is ind, in comps | DPD sat 1 |
| 216 | sad **[sat, no root in DPD]** | **[√as + a > sa + nta > sat]** | DPD gives a root | DPD sat 1 |
| 257 | sad `(adj comp)` | `(ind comp)` | DPD: sat is ind, in comps | DPD sat 1 |
| 257 | sad **[sat, no root in DPD]** | **[√as + a > sa + nta > sat]** | DPD gives a root | DPD sat 1 |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 249 | sad `(adj comp)` | `(ind comp)` | DPD: sat is ind, in comps | DPD sat 1 |
| 249 | sad **[sat, no root in DPD]** | **[√as + a > sa + nta > sat]** | DPD gives a root | DPD sat 1 |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 127 | sad `(adj comp)` | `(ind comp)` | DPD: sat is ind, in comps | DPD sat 1 |
| 127 | sad **[sat, no root in DPD]** | **[√as + a > sa + nta > sat]** | DPD gives a root | DPD sat 1 |

## 2026-10-05 — session S18b (step 9: index alignment for 07a)

Etymologies aligned across the checked subfolders (01–07a) to the DPD constructions used in 07a (S12–S18b), from the `index` report. Same lemma, same analysis in every file; homonyms, sandhi rows and bare-lemma variants were left.

### 01_reflection_on_the_four_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 105 | kāyassa [√ci > kay + a] | [√ci > ki > kay + a] | align with DPD construction | DPD kāyassa |
| 109 | vihiṁsā [vi + √his + ā] | [vi + √his > hiṁsa + ā] | align with DPD construction | DPD vihiṁsā |

### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 15 | abhiṇha [abhi + √ikkh + aṇa] | [abhi + √ikkh + aṇa > abhikkhaṇa > abhiṇha] | align with DPD construction | DPD abhiṇha |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |

### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 16 | abhiṇha [abhi + √ikkh + aṇa] | [abhi + √ikkh + aṇa > abhikkhaṇa > abhiṇha] | align with DPD construction | DPD abhiṇha |
| 18 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 115 | brahmacārī [brahma + cārī (√car)] | [brahma + cārī] | align with DPD construction | DPD brahmacārī |
| 244 | brahmacārīhi [brahma + cārī (√car)] | [brahma + cārī] | align with DPD construction | DPD brahmacārīhi |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 136 | kāyassa [√ci > kay + a] | [√ci > ki > kay + a] | align with DPD construction | DPD kāyassa |
| 148 | vihiṁsā [vi + √his + ā] | [vi + √his > hiṁsa + ā] | align with DPD construction | DPD vihiṁsā |

### 06_reflection_on_the_off_putting_qualities_of_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 18 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 88 | kāyaṁ [√ci > kay + a] | [√ci > ki > kay + a] | align with DPD construction | DPD kāyaṁ |
| 149 | kāyaṁ [√ci > kay + a] | [√ci > ki > kay + a] | align with DPD construction | DPD kāyaṁ |

### 08_reflection_on_the_unconditioned.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 43 | abhavissa [a + √bhū + issa] | [a + √bhū > bhava + issa] | align with DPD construction | DPD abhavissa |

### 09_reflection_on_the_thirty_two_parts.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 33 | pāda [√pad + a] | [√pad > pād + a] | align with DPD construction | DPD pāda |
| 146 | siṅghāṇikā [√siṅgh + āṇa + ikā] | [√siṅgh + aṇa > āṇa + ikā] | align with DPD construction | DPD siṅghāṇikā |
| 164 | pāda [√pad + a] | [√pad > pād + a] | align with DPD construction | DPD pāda |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 181 | bhavissatī'ti [√bhū + issa + ti; + iti] | [√bhū > bhava + issa + ti; iti] | align with DPD construction | DPD bhavissatī'ti |
| 259 | paripūreti [pari + √pūr + e + ti] | [pari + √pūr > pūre + ti] | align with DPD construction | DPD paripūreti |
| 322 | tasmātiha [tasmā + iti + ha] | [ta + smā; ima + ha] | align with DPD construction | DPD tasmātiha |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 127 | sap [sa] | [santa > sat] | align with DPD construction | DPD sap |

### 15_reflection_on_impermanence.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |

### 16_the_guardian_meditations.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 18 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 224 | siyā [√as + iyā] | [√as > siya + ā] | align with DPD construction | DPD siyā |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 382 | sap [sat, no root in DPD] | [santa > sat] | align with DPD construction | DPD sap |

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 18 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |
| 32 | aṅgiko [aṅga + ika] | [√añj > aṅg + a + ika] | align with DPD construction | DPD aṅgiko |
| 558 | bhiyyo [bhiyyo] | [√bhū > bhī + ya + o] | align with DPD construction | DPD bhiyyo |

### 21_mulaka_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | pāṭhaṁ [√paṭh + a] | [√paṭh > pāṭh + a] | align with DPD construction | DPD pāṭhaṁ |

## 2026-10-04 — session S11, step 9 (06 alignment; 15 shares Paṁsukūla lines with 06/10)

### 15_reflection_on_impermanence.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 60 | *addhuvaṁ* [na > a + dhuva] | [na > a + √dhuv + a] | index | DPD addhuva |
| 56 | Faithful: Life is uncertain; | Life is not lasting; | keeps *addhuva* distinct from *aniyata*; same change in 06/10 | spot check S11 |
| 76 | Faithful: I will inevitably die; | I must inevitably die; | renders the ptp (necessity); same change in 06/10 | spot check S11 |
| 82 | *maritabbaṁ* [√mar + itabba] | [√mar > mara + itabba] | DPD construction | DPD maritabba |
| *chuddho* row | [√chaḍḍ > chudh + ta] | note "[BM's spelling of *chuḍḍho*]" + [√chaḍḍ > chuḍḍ + ta]; BM's spelling *chuddho* kept | DPD | DPD chuḍḍha |

## 2026-10-04 — session S8, step 9 (index alignment after 04b was completed)

Same lemma analysed two ways in the checked files (01–03, 04a, 04b): the DPD construction is now used in all of them (local DPD, release 26 Sept 2026). Homonyms (*no*, *santo*, *pattiyā*) and context-dependent tags were left.

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 116 | *mahattam-abhikaṅkhatā* one sandhi row [maha + tta + abhi + √kaṅkh + a + nta] | two rows: *mahattam-* `(nt acc sg)` [√mah + a + tta]; *abhikaṅkhatā* `(prp masc instr sg)` | same words, one analysis (as 04b/06) | DPD mahatta |
| 245, 267 | *adhammo* [na > a + dhamma] | [na > a + √dhar + ma] | same word, one analysis | DPD adhamma |

## 2026-10-04 — session S7, step 9 (index alignment after 04a was completed)

Same lemma analysed two ways in the checked files (01–03, 04a): the DPD construction is now used in all of them (local DPD, release 26 Sept 2026). Homonyms and sandhi forms were left.


### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 193 | *divā* [√div + a] | [√div + a + ā] | same word, one analysis | DPD |
| 236 | *dassana* [√dis > dass + ana] | [√dis > dassa + ana] | same word, one analysis | DPD |

### 04_caturappamanna_obhasana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 31 | *disaṁ* [disā, no root in DPD] | [√dis + ā] | same word, one analysis | DPD |
| 42 | *tathā* [tathā] | [ta + thā] | same word, one analysis | DPD |
| 44 | *tathā* [tathā] | [ta + thā] | same word, one analysis | DPD |
| 46 | *tathā* [tathā] | [ta + thā] | same word, one analysis | DPD |
| 89 | *mahā* [mahant (√mah + ant)] | [√mah + nta + ā] | same word, one analysis | DPD |
| 117 | *disaṁ* [disā, no root in DPD] | [√dis + ā] | same word, one analysis | DPD |
| 175 | *disaṁ* [disā, no root in DPD] | [√dis + ā] | same word, one analysis | DPD |
| 233 | *disaṁ* [disā, no root in DPD] | [√dis + ā] | same word, one analysis | DPD |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 96 | *vigacchantu* [vi + √gam + a + ntu] | [vi + √gam > gaccha + ntu] | same word, one analysis | DPD |

### 10_sabba_patti_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 62 | *satta* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 264 | *ānubhāvena* [anu + √bhū > bhāv + a] | [anu > ānu + √bhū > bhāv + a] | same word, one analysis | DPD |
| 283 | *ānubhāvena* [anu + √bhū > bhāv + a] | [anu > ānu + √bhū > bhāv + a] | same word, one analysis | DPD |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 214 | *mahantañca* [mahant (√mah + ant) + ca] | [√mah + nta + ca] | same word, one analysis | DPD |
| 255 | *mahantañca* [mahant (√mah + ant) + ca] | [√mah + nta + ca] | same word, one analysis | DPD |
| 417 | *maha* [mahant (√mah + ant)] | [√mah + nta + ā] | same word, one analysis | DPD |
| 421 | *mahā* [mahant (√mah + ant)] | [√mah + nta + ā] | same word, one analysis | DPD |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 29 | *santi* [√as + a + nti] | [√as + anti > santi] | same word, one analysis | DPD |
| 308 | *pāṇino* [pāṇa + ī] | [pa + √an > ān + a + ī] | same word, one analysis | DPD |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 545 | *mahā* [mahant (√mah + ant)] | [√mah + nta + ā] | same word, one analysis | DPD |
| 570 | *mano* [√man + a] | [√man + as] | same word, one analysis | DPD |
| 596 | *puthu* [puthu, no root in DPD] | [√puth + u] | same word, one analysis | DPD |

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 75 | *vācā* [√vac + ā] | [√vac > vāc + ā] | same word, one analysis | DPD |
| 284 | *vācā* [√vac + ā] | [√vac > vāc + ā] | same word, one analysis | DPD |
| 344 | *vācā* [√vac + ā] | [√vac > vāc + ā] | same word, one analysis | DPD |

### 20_mettanisamsa_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 153 | *vaṇṇo* [√var + ṇa] | [√var + na] | same word, one analysis | DPD |

## 2026-10-04 — session S4, follow-up (bhikkhu's answers to queries 17–22)

No file change. All S4 readings stand: 13 keeps the *Pasannā hontu* verses (17) and the participle reading of *karonte'dha* (21); 19 is Amaravati's version of the path chant, kept with the citation *SN 45.8* (18); 12 keeps BM's spelling *pahaṁsāna* (19); the English titles of 17 and 18 are approved (20); the leader line of 21 is probably a local composition and is kept as it is (22).

## 2026-10-04 — session S4 (03_reflections 12–21)

Files 12–21 were brought to `style-spec.md`. The Literal/Faithful lines and word tables were redrafted unit by unit from the Pāli and the local DPD database (release 26 Sept 2026); the Pāli lines were kept except where listed. DPD = local database.

### All files (12–21)
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| — | safe fixes (`lint --fix`) | — | safe fixes applied | spec §1, §4 |
| 1–3 | English `#` title (20: also `## AN 11.15` heading) | Pāli `#` title + `*English title*` | file layout | spec §1 |
| all | non-canonical tags (`1s`, `pers pron`, `ind coord conj`, tags out of order, word class after case …) | canonical tags | tag rules | spec §4 |
| all | prose or Sanskrit etymologies (`sa- + akṣi`, "from pronominal base *ya*" …), bare lemmas for nouns | DPD roots and constructions; "no root in DPD" where DPD gives none | DPD wins | DPD |
| all | compounds without member rows | whole-compound row + ↳ member rows | compound rule | spec §4 |
| all | Literal/Faithful lines without trailing spaces; Faithful lines close to BM's English | two trailing spaces; Faithful lines redrafted from the Pāli and DPD | file layout; BM licence precaution | spec §1, §3 |
| all | later identical lines written out in full (12, 19) | repeat note | repeats | spec §6 |
| end | no citations | SuttaCentral IDs: 12 *SN 12.22*; 14 *DN 31*; 15 *Dhp 41*, *DN 16*; 18 *SN 6.2*, *SN 1.32*, *Thag 4.10*, *Dhp 54–59*; 19 *SN 45.8*; 20 *AN 11.15*; 21 *AN 10.58* | citations | SuttaCentral (checked online for SN 1.32, SN 12.22, SN 45.8, Thag 4.10) |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | — | leader line *Handa mayaṁ dhamma-pahaṁsāna-pāṭhaṁ bhaṇāmase* (BM *pāṭham* → *pāṭhaṁ*) | leader lines included | BM 3.14 |
| all | *sadatthaṁ* "own good" | "true good, highest good" (*sat + attha*) | meaning | DPD sadattha |
| all | *avaṅkatā* unanalysed | "not crooked" | meaning | DPD avaṅkata |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | — | leader line *Handa mayaṁ patti-dāna-gāthāyo bhaṇāmase* | leader lines included | BM 3.15 |
| end | chant ended at *Dhamme ariyappavedite* | BM's sub-section *Pasannā hontu sabbe pi* (10 lines) added under a Pāli `###` heading | BM prints it within 3.15; completeness (see query) | BM 3.15 |

### 14_verses_on_friends.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| — | `### Verse 1`, `### Verse 2` | removed | English headings are stray | spec §1, §7 |

### 15_reflection_on_impermanence.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | — | leader line *Handa mayaṁ aniccānussati-pāṭhaṁ bhaṇāmase* | leader lines included | BM 3.17 |

### 16_the_guardian_meditations.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | — | leader line *Handa mayaṁ catur'ārakkhā-kammaṭṭhāna-pāṭhaṁ bhaṇāmase* | leader lines included | BM 3.18 |
| Mettā, Maraṇassati | *Narānara-tiracchāna-* / *bhedā …*; *Jīvit'indriy'upaccheda-* / *saṅkhāta-maraṇaṁ siyā* (compounds split over two lines) | one Pāli line each | a word must not be split between units | BM 3.18 |

### 17_yan_dani_me_katam_punnam.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all Pāli lines | `cite: 1` appended to every Pāli line | removed | stray text | spec §7 |
| 3 | no English title | *Aspiration through the Merit Made* | file layout (see query) | spec §1 |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Pāli | *Viharimsu* | *Vihariṁsu* | niggahīta | Thanissaro |
| 3 | no English title | `*Verses on Reverence for the Dhamma*` | file layout | spec §1 |
| all | *tagara-mallikā* (fem nom sg) | (fem nom pl comp) | number | DPD tagaramallikā |

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | **[Handa mayaṁ ariyaṭṭhaṅgika-magga-pāṭhaṁ bhaṇāmase]** | brackets removed | leader brackets | spec §2 |
| — | English `###` headings (*Chanting Introduction*, *Definition of Right View …*, *Closing Line*) | removed | English headings are stray | spec §1, §7 |
| last | closing *Ayam-eva ariyo aṭṭhaṅgiko maggo* with full table | repeat note | repeats | spec §6 |
| all | *abhijjhā-domanassaṁ* (nt) | (masc acc sg comp) | gender | DPD abhijjhādomanassa |

### 20_mettanisamsa_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 5 | **[Handa mayaṁ mettānisaṁsa-suttaṁ bhaṇāmase]** | brackets removed | leader brackets | spec §2 |
| 2 | `## AN 11.15` | `*AN 11.15*` citation at the end | citations | spec §5 |

### 21_mulaka_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Pāli | *Chanda'mūlakā*, *Manasikāra'sambhavā*, *Phassa'samudayā*, *Vedanā'samosaraṇā*, *Samādhi'ppamukhā*, *Vimutti'sārā*, *Nibbāna'pariyosānā* (apostrophe without elision) | hyphen: *Chanda-mūlakā* … *Nibbāna-pariyosānā* | the apostrophe marks elision only | spec §2; SC an10.58:3.4 |
| Pāli | *Satā'dhipateyyā* | *Sat'ādhipateyyā* (*sati* + *adhipateyya*) | elision mark | SC an10.58:3.4; DPD |

### Cross-file index (step 9), 03_reflections 06–11
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 07:48 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:52 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:56 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:60 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:64 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:77 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:91 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 07:106 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 08:15 | *nibbāna* [nī + √vā + ana] | [nī + √vā > bā + ana] | same word, one analysis | DPD |
| 08:16 | *sutta* [√sīv + ta] | [√siv > suv + ta] | same word, one analysis | DPD |
| 09:30 | *kāyo* [√ci > kay + a] | [√ci > ki > kay + a] | same word, one analysis | DPD |
| 09:65 | *kāye* [√ci > kay + a] | [√ci > ki > kay + a] | same word, one analysis | DPD |
| 09:161 | *kāyo* [√ci > kay + a] | [√ci > ki > kay + a] | same word, one analysis | DPD |
| 10:122 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 10:235 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 11:107 | *sattā* [sa + tta; √as] | [√as > sa + tta] | same word, one analysis | DPD |
| 11:121 | *sukhañca* [√sukh + a; + ca] | [√sukh + a + ca] | same word, one analysis | DPD |
| 11:126 | *khippaṁ* [√khip + a + aṁ] | [√khip + ra + aṁ] | same word, one analysis | DPD |
| 11:247 | *pacceka* [pati + eka] | [pati > paty > pacc + eka] | same word, one analysis | DPD |
| 06:27 | *yathā* [yathā] | [ya + thā] | same word, one analysis | DPD yathā |

## 2026-10-04 — session S3, follow-up (bhikkhu's answers to queries 13–16)

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 271 | — | rubric *(Optional)* above *Dasapuññānubhāvena …* | BM marks the line as optional; rubric added to the spec | bhikkhu, 2026-10-04 (query 14); spec §7 |

Queries 13, 15 and 16 needed no file change: the wish renderings in 07 and 10 stand (decided case by case), and the English titles of 04, 07, 10 and 11 are approved.

## 2026-10-04 — session S3 (03_reflections 01–11)

Files 01–11 were brought to `style-spec.md`. Literal/Faithful lines and word tables were rewritten unit by unit (targeted line-range edits); the Pāli lines were kept except where listed. Line numbers refer to the new files. DPD = local database, release of 26 Sept 2026. Lint: 0 ERROR, 0 STRAY, 0 WARN. `compare`: all eleven files identical to BM after normalisation, apart from BM artefacts (running heads in 06 and 09, the "(Men Chant)" leader line in 02, BM's *mayam* in 07's leader line). Spot check: 4 of 10 units had errors (6 in total); all were fixed and every compound in the unit was re-checked against DPD.

### All files (01–11)
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| — | safe fixes (`lint --fix`) | — | safe fixes applied | spec §1, §4 |
| 1–3 | English `#` title | Pāli `#` title from BM's leader line + `*English title*` | file layout | spec §1 |
| 5 | — | BM's *Handa mayaṁ …* leader line added as the first unit, with full table (BM run-together spacing restored, hyphenation as in Thanissaro) | leader lines included (bhikkhu, 2026-10-01) | BM 3.1–3.11; Thanissaro |
| all | non-canonical tags (`1s`, `3p`, `pers`, `indec`, `part`, `grdv`, `fut pass part`, `dvandva`, `imperative/optative` …) | canonical tags (`ptp`, `1st sg …`, `dem pron`, `card`/`ord` …) | tag rules | spec §4 |
| all | prose or Sanskrit etymologies (`√ikṣ`, `√grah`, `√hiṁs`, `ūrdhva`, `adhas`, "desid of √gup", bare lemmas for nouns) | DPD constructions and roots; "no root in DPD" where DPD gives none | DPD wins | DPD |
| all | compounds without member rows | whole-compound row + ↳ member rows | compound rule | spec §4 |
| all | Literal/Faithful without trailing spaces; Faithful lines echoing BM's English (02, 03, 07) | two trailing spaces; Faithful lines redrafted from the Pāli and DPD | file layout; BM licence precaution | spec §1, §3 |
| all | *monks* | *bhikkhus* | key terms | spec §3 |
| all | later identical lines written out in full | repeat note | repeats | spec §6 |

### 01_reflection_on_the_four_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20, 74, 149, 195 | **[Paṭisaṅkhā]** yoniso … | **Paṭisaṅkhā** yoniso … | leader brackets removed | spec §2 |
| — | `### Robes`, `### Almsfood`, `### Lodging`, `### Medicinal Requisites` | removed | English headings are stray | spec §1, §7 |
| 204 | *gilāna-paccaya-bhesajja-parikkhāraṁ* "requisite of medicine for the support of the sick" | dvanda "support for the sick and medicinal requisites"; Faithful line to match | DPD reads it as a dvanda | DPD gilānapaccayabhesajjaparikkhāra (cmp *gilānapaccaya ca bhesajjaparikkhāra ca*) |
| 69 | *maṇḍanāya* (fem dat sg) | (nt dat sg) | gender | DPD maṇḍana |
| end | last row duplicated after the table; no citation | duplicate removed; *MN 2* | coverage; citation | BM *M.I.10* |

### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20, 133 | — / `### [Feminine Recitation Form]` | rubrics *(Men chant)*, *(Women chant)* | BM rubrics; English heading is stray | spec §7; BM 3.2 |
| 131, 229 | no citation | *AN 5.57* | citation | BM *A.III.71* |
| all | *-dhammomhi*, *kammassakomhi* tagged "(masc nom sg / comp)", *amhi* from √hū | compound rows with members; *amhi* = 1st sg pres of √as | grammar | DPD amhi (√as) |
| all | *sabbehi … piyehi manāpehi* (abl pl) | (instr pl) with *nānābhāvo / vinābhāvo* | case with words of separation | grammar; DPD nānābhāva "separation (from)" |

### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 180 | **'Kathambhūtassa** … | **Kathambhūtassa** … | opening quotation mark removed (punctuation, not elision) | spec §2 (apostrophe only for elision) |
| all | √ikṣ | √ikkh | Sanskrit root | DPD abhiṇha |
| 191 ff. | *kacci … na upavadati* rendered "Does … reproach me?" | "I hope … find no fault" | *kacci* = I hope; *na* was untranslated | DPD kacci |
| 234 | *uttari-manussa-dhammā* (abl/gen) | (masc abl sg comp) with note: *uttari* governs the ablative | grammar | DPD uttarimanussadhamma |
| end | no citation | *AN 10.48* | citation | BM *A.V.87* |

### 04_caturappamanna_obhasana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 3 | — | English title *Radiating the Four Immeasurables* | file layout | spec §1 |
| 19 | **[Mettā-sahagatena]** cetasā … | **Mettā-sahagatena** cetasā … | leader brackets removed | spec §2 |
| all | *cetasā* (nt instr sg) and qualifiers (nt/masc) | (masc instr sg) | gender of *cetas* | DPD cetas (masc) |
| 43–47 | *dutiyaṁ / tatiyaṁ / catutthaṁ* (fem acc sg) | (ord nt acc sg), used adverbially | the feminine of *catuttha* is *catutthī* | DPD catuttha |
| end | no citation | *DN 13* | citation | BM *D.I.251* |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 261 | *gilāna-paccayabhesajja-parikkhāro* | dvanda, as in 01 | see 01 | DPD |
| all | *n'eva*, *purāṇañca*, *navañca*, *cā'ti*, *abyāpajjha-paramatāyā'ti* followed by extra rows for their parts | one row per written word | coverage | spec §4 |
| end | no citation | *MN 2* | citation | BM *M.I.10* |

### 06_reflection_on_the_off_putting_qualities_of_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | *dhātu-mattam-ev'etaṁ* as rows *dhātu-mattam / eva / etaṁ* | rows *dhātu-mattam- / ev' / etaṁ* | coverage | spec §4 |
| all | *yat / tat* rows for *yad / tad* | *yad / tad* | coverage | spec §4 |
| 49 ff. | "Now, all these robes are not unrepulsive in themselves" | "None of these robes is repulsive" | double negative misrendered *ajigucchanīyāni* | DPD ajigucchanīya |
| 224, 250 | *gilāna-paccaya-bhesajja-parikkhāro* | dvanda, as in 01 | see 01 | DPD |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 3 | — | English title *Spreading Loving-Kindness* | file layout | spec §1 |
| 18 | **[Ahaṁ sukhito homi]** niddukkho … | **Ahaṁ sukhito homi** niddukkho … | leader brackets removed | spec §2 |
| 23 ff. | *homi*, *pariharāmi* "(pres act 1s sg imperative/optative)" | (1st sg pres act indic) with note "present tense, used here as an aspiration" | the form is indicative | DPD hoti; query 13 |
| end | unit with Pāli line *M.I.288; A.V.88*, Literal, Faithful and table | removed; citation *MN 41; AN 10.48* | stray text; citation | BM 3.7 (PTS→SC conversion: inference) |

### 08_reflection_on_the_unconditioned.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| end | no citation | *Ud 8.3* | citation | SuttaCentral |

### 09_reflection_on_the_thirty_two_parts.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 20 | **[Ayaṁ kho]** me kāyo … | **Ayaṁ kho** me kāyo … | leader brackets removed | spec §2 |
| 67–150 | — (the list of the 32 parts was missing) | six lines *kesā lomā …* to *… muttaṁ matthaluṅgan'ti*, with Literal, Faithful and tables; divided into the traditional groups (BM gives no line division) | missing passage | BM 3.9; DPD |
| 172 | second *tacapariyanto …* written out in full | repeat note | repeats | spec §6 |
| end | no citation | *MN 10* | citation | BM *M.I.57* |

### 10_sabba_patti_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 3 | — | English title *Verses on Sharing Merit with All Beings* | file layout | spec §1 |
| 172 | *nivedayuṁ* (3rd pl opt act) | (3rd pl aor act indic) with note "aorist form, used here as a wish" | the form is aorist | DPD nivedayi; query 13 |
| 269 | *sijjhataṁ* (3rd pl imp pass) | (3rd sg pres mid imperat), agreeing with *āsā* | number and voice | DPD sijjhati |
| 160 | *bhavābhave* (bhava + a-bhava) | members *bhava + ā + bhava* | construction | DPD bhavābhava 1 |

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 3 | — | English title *Verses of Dedication and Resolve* | file layout | spec §1 |
| 20 | **[Iminā puññakammena]** upajjhāyā … | **Iminā puññakammena** upajjhāyā … | leader brackets removed | spec §2 |
| 271 | **[Dasapuññānubhāvena mārokāsaṁ labhantu mā]** | brackets removed, line kept | no brackets in a Pāli line; BM marks the line as optional (query 14) | spec §2; BM 3.11 note |
| 37 | *ācariyūpakārā* (comp) | (sandhi) *ācariyā + upakārā* | DPD deconstruction | DPD |
| 40 | *mātāpitā* (masc nom pl dvandva) | (masc nom pl comp) with members | compound rule | DPD mātāpitā |
| 206 | *viriyamhinā* "[viriya + iminā / asmā]" | (sandhi) *viriyaṁ + iminā* with *-h-*; marked "not in DPD (inference)" | unverified against DPD | — |
| 155 | *sulabhe* "(opt/pres act 1s sg)" | (1st sg mid opt) with prefix *su-* | tags | grammar |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 02_five_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 50 | me [enclitic form of amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 81 | kammaṁ [√kar (to do/make) + -ma] | [√kar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 156 | me [enclitic form of amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 187 | kammaṁ [√kar + -ma] | [√kar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 45 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 61 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 79 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 80 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 100 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 122 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 146 | kammaṁ [√kar + -ma] | [√kar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 169 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 205 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 206 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 232 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 04_caturappamanna_obhasana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 60 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 99 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 148 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 187 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 236 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 275 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 324 | cetasā [citta / cetas] | [√cit + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_recollection_after_using_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 187 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 06_reflection_on_the_off_putting_qualities_of_the_requisites.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 14 | eva [emphatic particle, sandhi: eva + etaṁ -> ev'etaṁ] | [eva] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 15 | etaṁ [base e / eta] | [eta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 58 | pana [conjunction] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 88 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 92 | eva [emphatic particle] | [eva] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 93 | etaṁ [base e / eta] | [eta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 136 | pana [conjunction, sandhi: pana + ayaṁ -> panāyaṁ] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 166 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 170 | eva [emphatic particle] | [eva] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 171 | etaṁ [base e / eta] | [eta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 214 | pana [conjunction] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 244 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 248 | eva [emphatic particle] | [eva] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 249 | etaṁ [base e / eta] | [eta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 292 | pana [conjunction] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 102 | kammaṁ [√kar + -ma] | [√kar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 08_reflection_on_the_unconditioned.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 64 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 09_reflection_on_the_thirty_two_parts.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 12 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 57 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 10_sabba_patti_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 26 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 88 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 95 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 204 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 230 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 289 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 168 | dukkhassa [dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 197 | puggalā [puggala] | [puggala, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 274 | dhamme [√dhar + -a > dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 14_verses_on_friends.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 95 | yathā [yathā] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 16_the_guardian_meditations.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 243 | pāṇīnaṁ [pāṇa + in + ānaṁ] | [pa + √an + a + ī] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 17_yan_dani_me_katam_punnam.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 174 | satthu [satthu] | [√sās + tar] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 247 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 36 | sambuddho [sam + √budh + ta] | [saṁ + √budh + ta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 292 | dhamme [√dhar + ma + e] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 487 | yathā [from pronominal base *ya* + thā] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 49 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 59 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 69 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 79 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 89 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 99 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 109 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 119 | sammā [√sam + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 148 | kho [enclitic particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 305 | vācāya [abl sg of vācā, from √vac + -ā] | [√vac + ā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 318 | vācāya [abl sg of vācā, from √vac + -ā] | [√vac + ā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 975 | kāyena [ins sg of kāya] | [√ci + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 1021 | dukkhassa [gen sg of dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 20_mettanisamsa_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 98 | manussānaṁ [manussa, √man (to think) + -ussa] | [manu + ssa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 21_mulaka_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 127 | 'ti [sandhi form of *iti*] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 241 | 'ti [sandhi form of *iti*] | [iti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 03_ten_subjects_for_frequent_recollection.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | dhammā [√dhar + -a > dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 235 | dhammā [√dhar + -a] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 04_caturappamanna_obhasana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 58 | lokaṁ [√lok + -a > loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 146 | lokaṁ [√lok + -a > loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 234 | lokaṁ [√lok + -a > loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 322 | lokaṁ [√lok + -a > loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 07_mettapharana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 37 | hontu [√hū + -a- + -ntu] | [√hū + a + ntu] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 41 | hontu [√hū + -a- + -ntu] | [√hū + a + ntu] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 45 | hontu [√hū + -a- + -ntu] | [√hū + a + ntu] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 49 | hontu [√hū + -a- + -ntu] | [√hū + a + ntu] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 11_uddissanadhitthana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 92 | hontu [√hū + -ntu] | [√hū + a + ntu] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 154 | dhammā [√dhar + -a] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 217 | dhammo [√dhar + -a] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 233 | saṅgho [saṁ- + √han + -a > saṅgha] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 12_the_teaching_on_striving_according_to_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | svākkhāto [su- + ā- + √khā + -ta > svākkhāta] | [su + ā + √khā + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 14 | dhammo [√dhar + -a > dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 187 | dukkhaṁ [du- + kha > dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 317 | satthā [√sās + -tar > satthar] | [√sās + tar] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 13_dedication_of_merit_to_the_devas_and_others.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 184 | dhammo [√dhar + -a > dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 208 | saṅgho [saṁ- + √han + -a > saṅgha] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 224 | hitāya [√dhā + -ta > hita] | [√dhā + ita] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 15_reflection_on_impermanence.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | saṅkhārā [saṁ- + √kar + -a > saṅkhāra] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 12 | aniccā [a- + √i + -tya > nicca > anicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 24 | saṅkhārā [saṁ- + √kar + -a > saṅkhāra] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 25 | dukkhā [du- + √kha + -a > dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 38 | anattā [an- + attan > anattā] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 226 | aniccā [a- + √i + -tya > nicca > anicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 228 | saṅkhārā [saṁ- + √kar + -a > saṅkhāra] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 17_yan_dani_me_katam_punnam.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | puññaṁ [√puññ + -a > puñña] | [√puṇ + ya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 234 | buddho [√budh + -ta > buddha] | [√budh + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 18_dhamma_garav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 169 | dhammo [√dhar + ma + o] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 225 | dhammo [√dhar + ma + o] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 257 | dhammo [√dhar + ma + o] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 268 | dhammo [√dhar + ma + o] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 280 | dhammo [√dhar + ma + o] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 393 | anuttaro [an + uttara + o] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 19_the_teaching_on_the_noble_eightfold_path.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 15 | bhaṇāmase [√bhaṇ + -ā- + -mase] | [√bhaṇ + a + mase] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 686 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 725 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 764 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 803 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 20_mettanisamsa_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | bhaṇāmase [√bhaṇ (to speak/recite) + -āmase] | [√bhaṇ + a + mase] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 21_mulaka_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | bhaṇāmase [√bhaṇ + -ā- + -mase] | [√bhaṇ + a + mase] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 27 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 38 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 49 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 60 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 71 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 82 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 93 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 104 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 115 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 126 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 141 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 152 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 163 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 174 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 185 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 196 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 207 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 218 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 229 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 240 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 02_five_subjects_for_frequent_recollection.md | 51 | piyehi [√pī (to please/delight) + -ya] | [√pī + a] | DPD lemma / construction | DPD |
| 02_five_subjects_for_frequent_recollection.md | 100 | evaṁ [pronominal adv] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_five_subjects_for_frequent_recollection.md | 157 | piyehi [√pī + -ya] | [√pī + a] | DPD lemma / construction | DPD |
| 02_five_subjects_for_frequent_recollection.md | 206 | evaṁ [pronominal adv] | [eva + aṁ] | DPD lemma / construction | DPD |
| 03_ten_subjects_for_frequent_recollection.md | 123 | piyehi [√pī + -ya > piya] | [√pī + a] | DPD lemma / construction | DPD |
| 05_recollection_after_using_the_requisites.md | 11 | mayā [asma] | [ahaṁ] | DPD lemma / construction | DPD |
| 05_recollection_after_using_the_requisites.md | 80 | mayā [asma] | [ahaṁ] | DPD lemma / construction | DPD |
| 05_recollection_after_using_the_requisites.md | 206 | mayā [asma] | [ahaṁ] | DPD lemma / construction | DPD |
| 05_recollection_after_using_the_requisites.md | 266 | mayā [asma] | [ahaṁ] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 31 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 72 | imaṁ [base ima] | [ima] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 109 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 150 | imaṁ [base ima] | [ima] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 187 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 228 | imaṁ [base ima] | [ima] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 265 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 06_reflection_on_the_off_putting_qualities_of_the_requisites.md | 306 | imaṁ [base ima] | [ima] | DPD lemma / construction | DPD |
| 07_mettapharana.md | 10 | ahaṁ [amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 10_sabba_patti_dana_gatha.md | 214 | mayā [amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 10 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 13 | mayā [amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 379 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 382 | amhākaṁ [amha] | [amha + ākaṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 410 | mayaṁ [amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 12_the_teaching_on_striving_according_to_dhamma.md | 440 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 24 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 39 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 53 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 110 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 124 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 138 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 14_verses_on_friends.md | 150 | yo [yasa-stem] | [ya] | DPD lemma / construction | DPD |
| 17_yan_dani_me_katam_punnam.md | 258 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 11 | ca [pronominal particle] | [ca] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 23 | ca [pronominal particle] | [ca] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 34 | yo [from pronominal base *ya*] | [ya] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 55 | sabbe [from pronominal stem *sabba*] | [sabba] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 67 | ca [pronominal particle] | [ca] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 223 | na [negative particle] | [na] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 227 | ca [pronominal particle] | [ca] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 302 | na [negative particle] | [na] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 314 | na [negative particle] | [na] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 325 | na [negative particle] | [na] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 423 | yo [from pronominal base *ya*] | [ya] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 424 | ca [pronominal particle] | [ca] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 477 | na [negative particle] | [na] | DPD lemma / construction | DPD |
| 18_dhamma_garav_adi_gatha.md | 528 | evaṁ [from pronominal base *e* + vaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 12 | handa [indeclinable particle] | [handa] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 29 | ariyo [√ar + -iya] | [ariya] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 134 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 216 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 279 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 359 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 426 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 439 | idha [indeclinable adverb] | [ima + dha] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 441 | ariyo [√ar + -iya] | [ariya] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 475 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 488 | idha [indeclinable adverb] | [ima + dha] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 643 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 656 | idha [indeclinable adverb] | [ima + dha] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 832 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 845 | idha [indeclinable adverb] | [ima + dha] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 936 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 949 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 962 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 1009 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 1022 | ca [indeclinable conjunction] | [ca] | DPD lemma / construction | DPD |
| 19_the_teaching_on_the_noble_eightfold_path.md | 1080 | ariyo [√ar + -iya] | [ariya] | DPD lemma / construction | DPD |
| 20_mettanisamsa_sutta.md | 11 | handa [particle] | [handa] | DPD lemma / construction | DPD |
| 20_mettanisamsa_sutta.md | 12 | mayaṁ [base: amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 11 | mayaṁ [*asma*] | [ahaṁ] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 26 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 37 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 48 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 59 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 70 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 81 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 92 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 103 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 114 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 125 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 140 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 151 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 162 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 173 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 184 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 195 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 206 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 217 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 228 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |
| 21_mulaka_sutta.md | 239 | sabbe [*sabba*] | [sabba] | DPD lemma / construction | DPD |

