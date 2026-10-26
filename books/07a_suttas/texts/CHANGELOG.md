# Changelog: 07a_suttas

## 2026-10-26 — DPD check corrections (07)

Rows corrected after the first full `make dpd-check` review (docs/legacy-migration.md, "DPD check review"). Only the etymology changed; the Pāli, renderings and tags are unchanged. Lint: 0 ERROR, 0 STRAY, 0 WARN in the changed files, as before; `simsapa.py check`: the corrected rows match DPD; `index.py`: no conflicts.

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 2102 | ↳ *asita* [asita, form not in DPD] | [na > a + √sit + a] | DPD has *asita* (adj, black; dark-coloured) | DPD asita 3.1 |

## 2026-10-23 — layout fixes (no change to the wording)

Blank lines and final newlines added where the layout differed from the style spec, so that `scripts/draft.py extract` gives each file back; found by the round-trip check (docs/legacy-migration.md, "Layout findings"). Maintainer's decision, 2026-10-23. Lint and compare results unchanged.

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 120 | no blank line before *Evaṁ me sutaṁ* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 1435 | no blank line before *Idam-avoca bhagavā.* | blank line | style spec §1 layout | maintainer, 2026-10-23 |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 120 | no blank line before *Evaṁ me sutaṁ* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 1000 | no blank line before *Idam-avoca bhagavā.* | blank line | style spec §1 layout | maintainer, 2026-10-23 |
| 1026 | no blank line before *Imasmiñca pana veyyākaraṇasmiṁ …* | blank line | style spec §1 layout | maintainer, 2026-10-23 |

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 01_dhammacakkappavattana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 139, 158, 1184, 1539 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 1200 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 1260, 1276 | *bhagavatā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 140, 159, 1442 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 1458 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 140, 160, 1007 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 1021 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 05_dhaj_agga_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24, 44, 69, 590, 934 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 59, 745, 760, 775, 790, 820 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 172, 368, 461 | *bhavissati* √bhū + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |
| 637 | *bhagavā-ti* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 682 | *bhagavatā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 619 | *anuttaro* `(masc nom sg)` | `(adj masc nom sg)` | DPD adj; aligned with 04a/13, 07a/05 | DPD anuttara |

### 06_girimananda_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25, 70, 129 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 81, 98 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 1783 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24, 102, 136, 395, 568 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 71, 206 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 147, 191, 223, 273, 558 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 448, 482 | *bhagavantānaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 467, 486 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |
| 498 | *ācikkhissāmi* ā + √cikkh + issā + mi | ā + √cikkh + a + issa > cikkhissa + mi | DPD future-stem construction (present stem cikkha) | DPD ācikkhati 1 |
| 512, 773 | *kittayissāmi* √kitt + aya + issā + mi | √kitt + aya + issa + mi | future suffix is -issa- | grammar |
| 544 | *bhāsissāmīti* √bhās + issā + mi | √bhās + a + issa > bhāsissa + mi | DPD future-stem construction | DPD bhāsissati |
| 544 | *bhāsissāmīti* bhāsissa + mi] | bhāsissa + mi; iti] | iti joined in the form, as in 07a/08 | grammar |

### 08_bhikkhu_aparihaniya_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25, 44, 100, 446 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 75 | *bhāsissāmīti* √bhās + issa + mi | √bhās + a + issa > bhāsissa + mi | DPD future-stem construction | DPD bhāsissati |
| 90, 460 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 130, 331 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |
| 160 | *sannipatissanti* saṁ + ni + √pat + issa + nti | saṁ + ni + √pat + a + issa > patissa + nti | DPD future-stem construction (present stem pata) | DPD sannipatati |
| 175, 270 | *karissanti* √kar + issa +  | √kar + o + issa > karissa +  | DPD future-stem construction | DPD karissati 1 |
| 215 | *vattissanti* √vatt + issa + nti | √vatt + a + issa > vattissa + nti | DPD future-stem construction (present stem vatta) | DPD vattati 1 |
| 267 | *sakkarissanti* sat + √kar + issa + nti | sat + √kar + o + issa > karissa + nti | DPD future-stem construction | DPD karissati 1, sakkaroti |

### 09_gotami_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24, 49, 92, 422 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 60, 79 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 105, 438 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 10_saraniya_dhamma_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24, 44, 71, 529 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 61, 543 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 11_nakulapitusutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25, 54, 152, 164, 474, 557 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 65, 86, 317, 485, 501, 640 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 135, 304, 411 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 273 | *bhavissatī'ti* √bhū > bhava + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |
| 438, 458, 619 | *bhagavatā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 750 | *bhāsissāmī'ti* √bhās + issa + mi | √bhās + a + issa > bhāsissa + mi | DPD future-stem construction | DPD bhāsissati |

### 12_itivuttaka_49_ditthigatasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13, 365 | *bhagavatā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 275 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |


## 2026-10-05 — session S20 (cross-file index, from 07c_bhikkhuaparihaniyadhamma)

Step-9 alignment after 07c was completed: each word now has the DPD analysis in every file.

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1401 | vimuccati `(3rd sg pres act indic)` [passive in sense] is released, is freed; **[vi + √muc > mucca + ti]** | `(3rd sg pres pass indic)` is released, is freed; **[vi + √muc + ya > mucca + ti]** | DPD: pass of vimuñcati | DPD vimuccati |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 966 | vimuccati `(3rd sg pres act indic)` [passive in sense] is released, is freed; **[vi + √muc > mucca + ti]** | `(3rd sg pres pass indic)` is released, is freed; **[vi + √muc + ya > mucca + ti]** | DPD: pass of vimuñcati | DPD vimuccati |

### 08_bhikkhu_aparihaniya_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 208 | yathāpaññattesu `(pp nt loc pl comp)` | `(adj nt loc pl comp)` | DPD: adj | DPD yathāpaññatta |
| 210 | paññattesu `(pp nt loc pl)` laid down | `(adj nt loc pl)` [pp *paññatta* as the last member] laid down | last member takes the compound's word class (adj) | DPD yathāpaññatta; spec §4 |
| 283 | maññissanti **[√man > mañña + issa + nti]** | **[√man + ya > mañña + issa + nti]** | DPD construction | DPD maññati |
| 422 | sandississanti `(3rd pl fut act indic)` will be seen (in), will be found (in); **[saṁ + √dis > dissa + issa + nti]** | `(3rd pl fut pass indic)` will be seen (in), will be found (in); **[saṁ + √dis + ya > dissa + issa + nti]** | DPD: pass of sampassati | DPD sandissati |


## 2026-10-05 — session S19c (cross-file index, from 07b_anagatabhaya_suttas)

Step-9 alignment after 07b was completed: each word now has the DPD analysis in every file.

### 01_dhammacakkappavattana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1086 | yato `(rel pron masc abl sg)` [used as a conjunction] | `(ind)` [abl of *ya*, used as a conjunction] | DPD: ind, adv | DPD yato 1 |
| 1086 | yato **[ya]** | **[ya + to]** | align with DPD construction | DPD yato 1 |

### 05_dhaj_agga_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 747 | sāvaka **[√su + aka]** | **[√su > sāv + aka]** | align with DPD construction | DPD sāvaka |
| 762 | sāvaka **[√su + aka]** | **[√su > sāv + aka]** | align with DPD construction | DPD sāvaka |
| 777 | sāvaka **[√su + aka]** | **[√su > sāv + aka]** | align with DPD construction | DPD sāvaka |
| 792 | sāvaka **[√su + aka]** | **[√su > sāv + aka]** | align with DPD construction | DPD sāvaka |
| 822 | sāvaka **[√su + aka]** | **[√su > sāv + aka]** | align with DPD construction | DPD sāvaka |

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 165 | seyyathāpi `(ind)` just as, just like; **[se + yathā + api]** | `(sandhi)` [*se* (pron) + *yathā* (adv) + *api* (ind)] just as, just like; **[se; yathā; api]** | DPD gives it as sandhi | DPD seyyathāpi |
| 453 | seyyathāpi `(ind)` just as, just like; **[se + yathā + api]** | `(sandhi)` [*se* (pron) + *yathā* (adv) + *api* (ind)] just as, just like; **[se; yathā; api]** | DPD gives it as sandhi | DPD seyyathāpi |
| 487 | seyyathāpi `(ind)` just as, just like; **[se + yathā + api]** | `(sandhi)` [*se* (pron) + *yathā* (adv) + *api* (ind)] just as, just like; **[se; yathā; api]** | DPD gives it as sandhi | DPD seyyathāpi |

### 12_itivuttaka_49_ditthigatasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 161 | yato `(rel pron masc abl sg)` [used as a conjunction] | `(ind)` [abl of *ya*, used as a conjunction] | DPD: ind, adv | DPD yato 1 |
| 161 | yato **[ya]** | **[ya + to]** | align with DPD construction | DPD yato 1 |

## 2026-10-05 — session S18b (step 9: index alignment for 07a)

Etymologies aligned across the checked subfolders (01–07a) to the DPD constructions used in 07a (S12–S18b), from the `index` report. Same lemma, same analysis in every file; homonyms, sandhi rows and bare-lemma variants were left.

### 01_dhammacakkappavattana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | anuttaraṁ [na + ud + tara] | [na > an + ud + tara] | align with DPD construction | DPD anuttaraṁ |
| 34 | anuttaraṁ [na + ud + tara] | [na > an + ud + tara] | align with DPD construction | DPD anuttaraṁ |
| 254 | abhiññāya [abhi + √ñā + ā] | [abhi + √ñā + ya] | align with DPD construction | DPD abhiññāya |
| 1072 | anuttaraṁ [na + ud + tara] | [na > an + ud + tara] | align with DPD construction | DPD anuttaraṁ |
| 1292 | anuttaraṁ [na + ud + tara] | [na > an + ud + tara] | align with DPD construction | DPD anuttaraṁ |

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 31 | vād' [√vad + a] | [√vad > vād + a] | align with DPD construction | DPD vād' |
| 174 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 186 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 232 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 289 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 335 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 392 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 438 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 495 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 524 | hontu [√hū > ho + antu] | [√hū > ho + ntu] | align with DPD construction | DPD hontu |
| 541 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 571 | hontu [√hū > ho + antu] | [√hū > ho + ntu] | align with DPD construction | DPD hontu |
| 597 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 643 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 690 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 705 | bhante [√bhū + a + nta + e] | [√bhū > bhava + nta + e] | align with DPD construction | DPD bhante |
| 730 | bhante [√bhū + a + nta + e] | [√bhū > bhava + nta + e] | align with DPD construction | DPD bhante |
| 773 | bhante [√bhū + a + nta + e] | [√bhū > bhava + nta + e] | align with DPD construction | DPD bhante |
| 785 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 800 | bhante [√bhū + a + nta + e] | [√bhū > bhava + nta + e] | align with DPD construction | DPD bhante |
| 847 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 906 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 921 | bhante [√bhū + a + nta + e] | [√bhū > bhava + nta + e] | align with DPD construction | DPD bhante |
| 968 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 1026 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 1042 | ajjhattaṁ [adhi > ajjh + atta] | [adhi > adhy > ajjh + atta] | align with DPD construction | DPD ajjhattaṁ |
| 1229 | keci [ka + ci] | [ka + e + ci] | align with DPD construction | DPD keci |
| 1354 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 1400 | virāgā [vi + √raj > rāg + a] | [vi + √raj > rag > rāg + a] | align with DPD construction | DPD virāgā |
| 1485 | anupādāya [na > an + upa + ā + √dā + ya] | [na > an + upa + √ādā + ya] | align with DPD construction | DPD anupādāya |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 172 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 183 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 195 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 662 | bhikkhave [√bhikkh + u] | [√bhikkh + u + ave] | align with DPD construction | DPD bhikkhave |
| 965 | virāgā [vi + √raj > rāg + a] | [vi + √raj > rag > rāg + a] | align with DPD construction | DPD virāgā |
| 1047 | anupādāya [na > an + upa + ā + √dā + ya] | [na > an + upa + √ādā + ya] | align with DPD construction | DPD anupādāya |

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 720 | eke `(card masc nom pl)` [eka] | `(adj masc nom pl)` [eka, no root in DPD] | DPD: adj only; as 07a/12 | DPD eka |
| 1617 | kāyikā [√ci > kay + a + ika] | [√ci > ki > kay + a + ika] | align with DPD construction | DPD kāyikā |

## 2026-10-05 — session S18b (07a_suttas 11)

07a/11 held the Pāli of SN 22.1 only. Its Pāli was checked against `reference-pali-supplement.md` (SuttaCentral *SN 22.1*) and the whole chant drafted to the spec: Literal, Faithful and word table for every unit, from the local DPD (release of 26 Sept 2026). The doctrinal section (five aggregates, twice) was generated from one table per aggregate.

### 11_nakulapitusutta.md
179 → 1997 lines; 0 → 142 Pāli units; 883 rows including ↳ member rows; 27 repeat notes (the retold dialogue and the sorrow-compound refrain). Lint after: clean. Compare against SN 22.1: 0.998 (only the colophon, below). DPD check: 48 flags, all homonyms (*atta* 1.1, *citta* 2, *vana*, *dāya*, *bhagga*), sandhi rows, *saññā'ti* read as *saññāti* "kin", and *dhammiṁ* fem acc (DPD lists masc/nt forms only); *bhesakaḷā* is not a DPD headword.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Nakulapitu-sutta`, no English title | `# Nakulapitu-sutta`, *The Discourse to Nakula's Father* | spec §1 | — |
| 3 | [Evaṁ me sutaṁ] | *Evaṁ me sutaṁ* (brackets removed; unit copied from 07a/01) | spec §2 | SN 22.1 |
| passim | Pāli only, prose paragraphs | 142 units at SuttaCentral's segments, long segments divided at clause boundaries; Literal, Faithful and table added for each | project-instructions §2 (Nakulapitu) | SN 22.1, DPD |
| passim | hyphenation and apostrophes in chant style (*Aham-asmi*, *pan'āhaṁ*) | kept | spacing artefacts only; `compare` ignores them | SN 22.1 |
| end | *Nakulapitu-suttaṁ niṭṭhitaṁ.* | kept, with its own unit (query) | chant colophon; SuttaCentral has *Paṭhamaṁ* | — |
| end | *S.III.1* | *SN 22.1* | spec §5 | SuttaCentral |
| 2 units | — | *aniccadassāvī* "who seldom sees" (DPD), not "seeing impermanence" | DPD meaning | DPD aniccadassāvī |
| row | (partial draft, not kept) ↳ *vayo* "not a headword" | [vi + √i > ay + as] (*vayas* 2 "age, stage of life") | DPD | DPD vayas |
| spot check | Faithful "and undisciplined / and well disciplined in the Dhamma of good persons:" | "and" removed (asyndetic series) | spec §3 | — |

## 2026-10-05 — session S18 (07a_suttas 08–10, 12)

None of the four chants is in BM, so 08–10 were redrafted from Thanissaro's *Chanting Guide* (lines 4495–4706) and 12 from `reference-pali-supplement.md` (SuttaCentral *Iti 49*), all in the spec format. They were checked against DPD (local db, 26 Sept 2026), and Thanissaro's readings were cross-checked against SuttaCentral's JSON (AN 6.12, AN 7.23, AN 8.53). Faithful lines were re-rendered from the Pāli. Prose is divided at clause boundaries, and each recurring refrain is its own unit, so later occurrences get the repeat note. The verses of 12 have one unit per half-verse. `compare` against a Pāli-only copy of each source passage gives 1.000, identical after normalisation, for all four files.

### 08_bhikkhu_aparihaniya_dhamma.md
370 → 464 lines; 17 → 34 Pāli units; 198 → 193 rows including ↳ member rows; 6 repeat notes. Lint before: 24 STRAY, 80 ERROR, 13 WARN; after: clean.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Bhikkhu-aparihāniya-dhamma Sutta`, *The Causes of Non-decline for Monks* | `# Bhikkhu-aparihāniya-dhamma-sutta`, *The Discourse on the Qualities that Prevent the Decline of Bhikkhus*; citation *AN 7.23* (none before) | spec §1, §5 | SuttaCentral AN 7.23 |
| passim | Pāli lines in backticks; `---` lines; numbering `[1]`–`[7]` in the Pāli; quotation marks | removed | spec §1, §2 | — |
| passim | whole paragraphs as single units | divided at the refrain *vuḍḍhiyeva … parihāni*, which is now a repeat-note unit | spec §2, §6 | Thanissaro |
| passim | pre-spec rows (no member rows, BM-style English) | all rows redrafted to spec §4 | spec | DPD |
| spot check | Faithful lines of the *Yāvakīvañ-ca* units dropped the vocative *bhikkhave* (6 lines) and *ca* (8 lines); *cira-pabbajitā* tagged `pp` (DPD: adj); *ratta* note "(abl)" | "And as long as, bhikkhus, the bhikkhus …"; `adj`; note gives DPD's compound construction | completeness; DPD cirapabbajita | DPD |

### 09_gotami_sutta.md
429 → 442 lines; 27 → 32 Pāli units; 182 rows including member rows; 1 repeat note. Lint before: 53 STRAY, 91 ERROR, 0 WARN; after: clean.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Gotamī Sutta`, no English title | `# Gotamī-sutta`, *The Discourse to Gotamī*; citation *AN 8.53* | spec §1, §5 | SuttaCentral AN 8.53 |
| passim | `[cite: 2]` after every Pāli line; `---` lines; quotation marks | removed | spec §2, §7 | — |
| 3 | opening and setting joined in one unit | *Evam-me sutaṁ,* and *Ekaṁ samayaṁ …* as two units | Thanissaro's leader portion | Thanissaro |
| passim | pre-spec rows | all rows redrafted; the 16 contrast lines generated from one table, each with its own *saṁvattanti* in the Faithful line | spec | DPD |
| spot check | Literal *N'eso dhammo* … "This not Dhamma …" | "Not this [is the] Dhamma …" (Pāli order) | spec §3 | DPD neso |

### 10_saraniya_dhamma_sutta.md
417 → 547 lines; 24 → 42 Pāli units; 219 rows including member rows; 13 repeat notes. Lint before: 24 STRAY, 72 ERROR, 0 WARN; after: clean.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Sārāṇīya-dhamma Sutta`, no English title | `# Sārāṇīya-dhamma-sutta`, *The Discourse on the Cordial Qualities*; citation *AN 6.12* | spec §1, §5 | SuttaCentral AN 6.12 |
| passim | `[cite: 1]` after every line (72); quotation marks | removed | spec §2, §7 | — |
| 5 | *Evaṁ me sutaṁ:* | *Evam-me sutaṁ,* | Thanissaro's spelling | Thanissaro |
| passim | *Puna c'aparaṁ, bhikkhave, …*, *Idha, bhikkhave, …*, *abhinandun-ti* (SuttaCentral-style commas and hyphen) | Thanissaro's text exactly, incl. *garukaraṇā* (l. 4537) and *ekībhāvāya* (ll. 4519, 4527) unhyphenated as printed | source | Thanissaro |
| passim | pre-spec rows | all rows redrafted to spec §4 | spec | DPD |
| spot check | Faithful "he does not keep such gains apart for his own use" | "he is one who uses such gains without setting them apart for himself" | the Pāli is positive (*appaṭivibhattabhogī hoti*) | DPD appaṭivibhattabhogī |

### 12_itivuttaka_49_ditthigatasutta.md
340 → 370 lines; 25 → 25 Pāli units (the pāda units of the verses joined as half-verses; long prose lines divided); 139 → 165 rows including member rows. Lint before: 0 STRAY, 84 ERROR, 2 WARN; after: clean.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Diṭṭhigatasutta`, no English title, no citation | `# Diṭṭhigata-sutta`, *The Discourse on Speculative Views*; citation *Iti 49* | spec §1, §5 | SuttaCentral Iti 49 |
| passim | prose-style rows (`(vuttaṁ + hi + etaṁ)` …), tags `pers`, `ppp`, `num`, `noun`, `dvandva`, `conj`, `part`, `neg`; *meṇussa*; no member rows | all rows redrafted to spec §4 | spec | DPD |
| passim | closing quotation marks (*passantī”ti*, *punabbhavan”ti*), dash | *passantīti*, *punabbhavanti*; dash removed | spec §2 | SuttaCentral |
| row | *bhavataṇhā* | `(fem gen sg comp)` with the note that the stem form stands for the genitive governed by *parikkhayā* | DPD lists only nom/acc/instr for this form *(inference)* | DPD |

### Remaining DPD flags (15), all explained
Sandhi rows (*kinti*, *n'etaṁ*, *ayam-pi*, *yāyaṁ*, *kathañca* ×3, *ayampi*); no-root homonyms (*pabbate*, *vane* ×2, *attā* ×2: DPD's rooted homonyms are other words); *tathārūpāya* `(adj fem instr/loc sg comp)` agreeing with fem *diṭṭhiyā* (DPD's form list gives masc/nt dat only *(inference: fem forms not listed)*); *bhavataṇhā* (above).

## 2026-10-05 — session S17 (07a_suttas 07)

### 07_maha_samaya_sutta.md
Redrafted from Thanissaro's *Chanting Guide* (BM has no Mahāsamaya; spec §2 source order) in the spec format (1584 → 2392 lines; 119 → 184 Pāli units, one per half-verse in the verses as BM prints verse elsewhere (04a/27), prose divided at sentence and clause boundaries; 664 → 961 rows incl. ↳ member rows; 46 repeat notes). Checked against DPD (local db, 26 Sept 2026). Lint before: 85 STRAY, 621 ERROR, 133 WARN; after: clean. `compare` against a Pāli-only copy of Thanissaro's passage with PDF artefacts repaired: 0.991, the five remaining differences being English fragments left in that copy.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Mahā-samaya Sutta (DN 20) — Word-by-Word Translation`; no English title | `# Mahā-samaya-sutta`, *The Discourse on the Great Meeting*; citation *DN 20* at the end | spec §1, §5 | Thanissaro |
| passim | eleven invented headings `### Paṭhama-bhāga` … `### Dvādasama-bhāga` (no *Sattama-*) | removed | not in the source | Thanissaro |
| passim | corrupt or invented Pāli, e.g. *Tatra tattrābhidhāvanti cetaso samadhānathā trāsānaṁ ujukaṁ karanti nettāni varasmiggāhāti* for *Tatra bhikkhavo samādahaṁsu …*; *Āgatāmha dhamma-samayaṁ Dakkhitāye* (no *imaṁ*, *eva*); *Satta-sahasā te yakkhā … Kāpilavatthukā*; *vepullaṁ pavanāma sabhiyo* for *Vepullassa nivesanaṁ Bhiyyo*; *prasāsati*; a line *ekanāmā ti me sutā asīti dasa eko ca*; *dasasu … loka-dhātūsu* in the narrative | whole text re-set from Thanissaro, verse by verse; similarity before 0.654 | wrong text | Thanissaro; SuttaCentral DN 20 |
| passim | SuttaCentral-style opening *Evaṁ me sutaṁ—* | Thanissaro's *Evam-me sutaṁ.* (leader brackets removed) | source; spec §2 | Thanissaro |
| — | Thanissaro PDF artefacts | repaired from SuttaCentral: *Ma so hārājā yasassi* → *Mahārājā yasassi so* (×4); *Bhi so smā-kāyo yasassi* → *Bhismā-kāyo yasassi so*; *seyyathāpi haṁ etarahi. may* → *seyyathāpi mayhaṁ etarahi*; *se. Saṅkuddho asayaṁ-va* → *Saṅkuddho asayaṁ-vase*; stray *se*, *Ā* dropped; line-break hyphens joined (*etad-ahosi*, *eta-paramāyeva*, *Ekam-antaṁ*) | conversion artefacts (project-instructions §3) | SuttaCentral DN 20 |
| passim | Thanissaro readings that differ from SuttaCentral (*Dasahi … loka-dhātūhi*, *pacceka-gāthā*, *Dakkhitāyeva*, *Inda-khīlam-ohaccam-anejā*, *Vavakkhitvāna*, *Satta-sahassā va*, *tappasāsati*, *Kinnughaṇḍu*, *Janosabho*, *Nābhasā*, *Kambal'Assatarā*, *Erāvaṇṇo*, *Abhayantadā*, *Kālakañjā*, *baliṁ senaṁ*, *Paṭhavī ca*, *Vāruṇā*, *Mettā-Karuṇā-kāyikā*, *Veṇḍū ca devā Sahalī ca*, *purakkhitā/purakkhitvā*, *Ummā-*, *Mahāsamānā*, *-padūsikā*, *Karumhā*, *Pajunno*, *āgañchuṁ*, *Pavuttha-jātim-akkhīlaṁ*, *asitātitaṁ*, *Sahassa-brahma-lokānaṁ*, *Kaṇha-senaṁ*, *bandhamatthu*, *lomam-pi*) | kept as Thanissaro prints them; rows note SuttaCentral's reading where it matters | source; *(inference: a deliberate chanting recension)* | Thanissaro; SuttaCentral |
| passim | `[cite: n]` (20), `---` lines, tags `ind adv`, `pers pron`, `num`, `acc-time`, `3rd pers sg pres act`, `ppp`; no member rows; BM/Thanissaro-style English | all rows redrafted to spec §4 with ↳ member rows; Faithful lines re-rendered from the Pāli | spec §1, §3, §4 | DPD |
| rows | *āgū*, *āgā* | `(3rd pl/sg aor act indic)` with note "DPD: imperfect of *āgā*" [ā + √gam + ā] (the tag list has no `imperf`) | DPD āgā 1 | DPD |
| rows | — | DPD forms used: *bāhaṁ* (fem, *bāhā*); *āpo* (masc, *āpas* [√āp + as]); *yasasā* (masc); *Sahalī* (masc nom pl); *vavakkhitvāna* [√vac > vavakkha + itvāna] "wishing to announce"; *payirupāsati* [… √ās …]; *khiḍḍā* [√kīḷ + ā]; *saṅgāma* [saṁ + √gam > gāme + a]; *ettha* [ima + ttha]; *kālakañjā*, *vāruṇā*, *pāyāgā*, *yāmunā*, *khemiyā*, *sucitti* with DPD's constructions; *pañca-sata* nt; *-sahassā* card nt | DPD | DPD |
| row | *baliṁ senaṁ* | *baliṁ* `(adj masc acc sg)`, read as *balī* "strong", note that the form does not agree with fem *senaṁ* (SuttaCentral *balisenaṁ*) | *(inference; query)* | DPD balī |
| row | *asayaṁ-vase* | sandhi row, "not in his own control" | *(inference; DPD asayaṁvasī)* | DPD |
| spot check | Literal "…of yakkhas him attends" (order); Faithful "a host of …" (added); *das'ettha* [eta + ttha]; ↳ *gataṁ* without `pp`; *baliṁ* fem tag; *ath'āgū* note; *ye* in the Lohitavāsī line; *pacceka* construction | fixed; whole file re-reviewed by error class (Literal order and implied subjects, Faithful additions and omitted *ca*/*te*, member word class) | spot check 3 of 10 | DPD |

## 2026-10-05 — session S16 (07a_suttas 06)

### 06_girimananda_sutta.md
Redrafted from BM 7.9 in the spec format (931 → 1884 lines; 51 → 128 Pāli units; 402 → 864 rows incl. ↳ member rows; 9 repeat notes). Checked against DPD (local db, 26 Sept 2026). Lint before: 50 STRAY, 147 ERROR, 169 WARN; after: clean. `compare` against BM 7.9: 1.000.

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Girimānanda Sutta (AN 10.60)`, no English title | `# Girimānanda-sutta`, *The Discourse to Girimānanda*; citation moved to the end as *AN 10.60* | spec §1, §5 | BM 7.9 |
| top | file began at *Katamā c'Ānanda anicca-saññā?* | BM's opening restored: *Evaṁ me sutaṁ* (copied from 07a/01) to *Katamā dasa? … ānāpānassati* (12 units) | missing start | BM 7.9 |
| end | file ended at *Passambhayaṁ cittasaṅkhāraṁ passasissāmī'ti sikkhati* (8th of 16 breathing steps) | steps 9–16 (copied from 07a/04), *Ayaṁ vuccat'Ānanda, ānāpānassati*, and BM's ending *Sace kho tvaṁ … Girimānanda-suttaṁ niṭṭhitaṁ* (8 units) restored | missing end | BM 7.9; 07a/04 |
| 3–642 | ten headings `### 1. Anicca-saññā` … `### 10. Ānāpānassati` | removed | not in BM; digits | spec §1, §7 |
| passim | `[cite: 1]` after every Faithful line; 50 `---` lines; quotation marks; tags `part`, verbs without mood (`3rd sg pres act`), `(nt nom sg adj)`; no member rows | all rows redrafted to spec §4 with ↳ member rows | spec §1, §4 | — |
| passim | long units joining BM's sentences | divided at BM's sentence and clause boundaries, no words dropped or reordered | spec §2 | BM 7.9 |
| 596–628 | *aniccānupassī-saññā* (heading, question, conclusion) | *anicchāsaññā* / *anicchā-saññā* "perception of non-desire" | wrong word; BM reading | BM 7.9; DPD anicchāsaññā |
| list | *siro-rogo*; *cakkhu anattā*; *ādīnāvānupassī*; *upāyupādānā* | *sīsa-rogo*; *cakkhuṁ*; *ādīnavānupassī*; *upādānā* as BM (later restored to *upāyupādānā*, see the last row) | BM reading; misprint | BM 7.9 |
| passim | BM hyphenation not kept (*sabba-loke*, *Sabba-kāyapaṭisaṁvedī* / *Sabbakāya-paṭisaṁvedī*, *cittasaṅkhāraṁ* / *citta-saṅkhāraṁ*, *dantarogo*) | BM's hyphenation as printed, including its inconsistencies | spec §2 | BM 7.9 |
| passim | *paṭisañcikkhati* [paṭi-saṁ-√ci + kkh + a + ti]; *byantīkaroti* [bi-anta + √kar + o + ti]; *aṭṭīyati* [√aṭṭ + īya + ti] | [pati + saṁ + √cikkh + a + ti]; [byanta > byantī + karoti; √kar]; [√add > aṭṭīya + ti] | wrong root or construction | DPD |
| passim | "monk", "hut", "volitional formations"; Faithful lines echoing BM's English | Faithful lines re-rendered from the Pāli; *bhikkhu*, "empty dwelling", "formations" (as 07a/02, 04) | spec §3 | DPD |
| row | *lohitaṁ pittaṁ* | kept as two words (BM and Thanissaro), row notes DPD's compound *lohitapitta* "haemorrhage"; Faithful "[disorders of the] blood, [of the] bile" | *(inference: BM's word division read as listed disorders)* | DPD lohitapitta |
| row | *paṭipassambheyya* (first occurrence) | kept as BM prints it; row notes DPD's *paṭippassambheyya* | BM spelling | DPD paṭippassambhati |
| spot check | *ten'upasaṅkami* [… √kam > kama + i]; *seyyathīdaṁ* and *yad-idaṁ* sandhi notes without the parts' tags; ↳ *pariṇāma* [pari + √nam > ṇāme + a] (homonym "digestion"); Faithful "improper care [of the body]"; "he" unbracketed in 8 Literal lines | [… √kam + i]; parts' tags added; [pari + √nam > ṇām + a] (pariṇāma 2 "change"); "not looking after oneself"; "[he]" | DPD; spec §3–4 | DPD upasaṅkami, seyyathīdaṁ, pariṇāma 2, visamaparihāraja |
| *ye loke …* | *upādānā* (BM 7.9) | *upāyupādānā* `(nt nom pl comp)` with ↳ *upāya* [upa + √i > ay + a], ↳ *upādānā*; Literal and Faithful "engagements and clingings" | BM omission restored (query 51, bhikkhu, 2026-10-05) | Thanissaro; SuttaCentral AN 10.60; DPD upāyupādāna |

## 2026-10-05 — session S15 (07a_suttas 05)

### 05_dhaj_agga_sutta.md
Redrafted from BM 7.8 in the spec format (617 → 1086 lines; 34 → 71 Pāli units; 279 → 519 rows incl. ↳ member rows; 6 repeat notes). Checked against DPD (local db, 26 Sept 2026).

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Dhaj'agga-sutta`, no English title | *The Discourse on the Top of the Banner* added | spec §1 | BM 7.8 |
| passim | 34 long units joining BM's sentences | divided at BM's sentence and clause boundaries (71 units), no words dropped or reordered | spec §2 line division | BM 7.8 |
| passim | `...` rows "(elided repetitive clauses) refer to preceding tables" (6 units); 34 STRAY, 198 ERROR, 42 WARN in lint (`---` lines, tags `1s`, `3s`, `pres part`, `proper name`, `abstract`, `gerund`, `fpp`, `grd`, `neg`, `cmpd`, `compound`; no member rows) | all rows redrafted to spec §4 with ↳ member rows; repeated lines get the repeat note | spec §4, §6 | DPD |
| passim | quotation marks in the Pāli lines | removed | spec §2 | — |
| 3 units | *dha’jaggaṁ* (Varuṇa line, BM misprint) | *dhaj'aggaṁ* | BM misprint (misplaced apostrophe) | BM 7.8 elsewhere; DPD dhajagga |
| passim | "monks", BM-style English in Faithful lines | Faithful lines re-rendered from the Pāli; *bhikkhus* | spec §3 | DPD |
| passim | *chambhitattaṁ* [√chambh + -ita + -tta]; *samupabbūḷho* [saṁ- + upa- + √bavh + -ta]; *mārisā* [mārisa]; *palāyī* [para- + √ay + -in]; *utrāsī* [ud- + √tras + -in]; *Pajāpatissa* [pajā + pati] | [√khambh > chambh + ita + tta]; [saṁ + upa + vi + √yūh + ta > yūḍha > yūḷha]; [mārisa, no root in DPD]; [√palā > palāya + ī]; [ud + √tras > trās + ī]; members ↳ *pajā* [pa + √jan + ā], ↳ *patissa* [√pat + i] | DPD root / construction | DPD |
| passim | *ullokayataṁ*, *anussarataṁ* `(masc gen pl pres part)`; *pahīyissati* `(fut pass 3s sg)`; *pahīyetha* `(opt pass 3s sg)` | `(prp masc dat/gen pl)` agreeing with *vo*; `(3rd sg fut pass indic)`; `(3rd sg pass mid opt)` | canonical tags; DPD | DPD |
| row | *mameva* `(1s gen sg compound)`; *mam* / *eva*; *no'pi*, *pahīyethāpi* `(compound)` | `(sandhi)` rows | sandhi, not compounds | spec §4 |
| row | *Taṁ* (Taṁ kho pana …) unexplained | `(dem pron nt nom sg)` [introducing the statement that follows] | *(inference: DPD has no indeclinable taṁ; read as the pronoun used adverbially)* | DPD taṁ |
| row | *avītarāgo* etc. [a- + vīta (vi- + √i + -ta) + rāga …] | ↳ *a* (prefix) + ↳ *vītarāgo* [vīta + rāga] | DPD compound construction (na + vītarāga) | DPD avītarāga |
| end | *S.I.218* analysed as a Pāli unit with Literal/Faithful lines | citation line *SN 11.3* | spec §5 | SuttaCentral |
| spot check | ↳ *gato* in *tathāgato* `(pp masc nom sg)`; *avīta-* members a / vīta / rāga; ↳ *khettaṁ* [√khi + tta]; *anuttaraṁ* [na + ud + tara]; *samupabbūḷho* construction shortened; *pahīyethāpi* "or"; Faithful of *Pajāpatissa / Varuṇassa / Īsānassa vā …* omitting *dhaj'aggaṁ ullokayataṁ*; *Taṁ kho pana* Faithful without *taṁ* | `(masc nom sg)`; two members na + vītarāga; [√khi > khe + tta]; [na > an + ud + tara]; full DPD construction; "too"; each line renders its own words; "Now, …" | spot check 6 of 10 | DPD |

## 2026-10-05 — session S14 (07a_suttas 04)

### 04_anapanassati_sutta.md
Redrafted from BM 7.7 in the spec format (114 → 685 lines; 8 → 52 Pāli units; 33 → 266 rows incl. ↳ member rows; 2 repeat notes). Checked against DPD (local db, 26 Sept 2026).

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Ānāpānassati-sutta`, no English title | *The Discourse on Mindfulness of Breathing* added | spec §1 | BM 7.7 |
| 3 | `### Instalment 4` | removed | stray text | spec §7 |
| top–end | file held only BM's 8 lines *Citta-paṭisaṁvedī* … *Vimocayaṁ cittaṁ passasissāmī'ti sikkhati* (BM 7.7 lines 35–42 of 51) | whole extract restored: leader line *Handa mayaṁ ānāpānassati-sutta-pāṭhaṁ bhaṇāmase*, the opening (*Ānāpānassati bhikkhave …* to *Ujuṁ kāyaṁ …*), *So sato'va …*, the four *dīghaṁ/rassaṁ* lines, tetrads 1–2 and 4, and the closing *Evaṁ bhāvitā kho …* *Mahapphalā hoti mahānisaṁsā'ti* | chant incomplete | BM 7.7; MN 118 |
| passim | `---` lines; tags `cmpd/adj`, `ind particle`, `pres part act caus`, verbs without mood; coverage fault (extra *assasissāmi*, *iti*, *passasissāmi* rows under the sandhi rows) | all rows redrafted to spec §4 with ↳ member rows | spec §1, §4 | — |
| passim | *assasissāmi* [ā-√an + issa + mi], *passasissāmi* [pa-√an + issa + mi] | [ā + √sas > sas + issa + mi], [pa + √sas > sas + issa + mi] | wrong root | DPD assasati, passasati |
| passim | *citta-paṭisaṁvedī* [citta + pati-saṁ-√vid + e + in] | ↳ *paṭisaṁvedī* [pati + saṁ + √vid > ved + ī] | DPD construction | DPD paṭisaṁvedī |
| passim | *abhippamodayaṁ* [abhi-pa-√mud + aya + nt], *vimocayaṁ* [vi-√muc + aya + nt], *samādahaṁ* [saṁ-ā-√dhā + a + nt] | [abhi + pa + √mud > modaya + nta], [vi + √muc > mocaya + nta], [saṁ + ā + √dhā > daha + nta] | DPD construction | DPD |
| passim | *sikkhati* row "trains, practices" | "trains, practises" (verb) | British spelling | spec §3 |
| end | citation missing (BM *M.III.78*) | *MN 118:15.1–22.1* | spec §5 | SuttaCentral |
| BM | BM *mayam*, *pallaṅkaṁābhujitvā*, *Ujuṁkāyaṁpaṇidhāya parimukhaṁsatiṁupaṭṭhapetvā*, *Kathaṁbhāvitā*, *Evaṁbhāvitā* | *mayaṁ*; spaces restored | spec §2; BM PDF artefacts | BM 7.7 |
| spot check | ↳ *sabba* `(adj comp)`; ↳ *anicca* `(adj comp)` "[here: impermanence]"; *rukkha-mūla-gato*, *suññāgāra-gato* etymology as three members; Faithful "or to the foot of a tree", "or to an empty dwelling" | `(pron comp)` [sabba]; `(nt comp)` impermanence; [rukkhamūla + gata], [suññāgāra + gata]; "or gone to …" | DPD pos; DPD compound structure; *gato* rendered | DPD |

## 2026-10-04 — session S13 (07a_suttas 02–03)

### 02_anatta_lakkhana_sutta.md
Redrafted from BM 7.3 in the spec format (518 → 1503 lines; 36 → 117 Pāli units; 230 → 592 rows incl. ↳ member rows; 30 repeat notes). Checked against DPD (local db, 26 Sept 2026).

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Anatta-lakkhaṇa-sutta`, no English title | English title added | spec §1 | BM 7.3 |
| top | BM's solo introduction (*Yantaṁ sattehi dukkhena* … *bhaṇāma se*, 8 lines) missing | added under *(Solo introduction)* | chant incomplete | BM 7.3 |
| passim | leader brackets *[Evaṁ me sutaṁ]*, *[Taṁ kiṁ maññatha bhikkhave]*, *[Tasmā tiha bhikkhave]*, *[Evaṁ passaṁ bhikkhave]*, *[Idam-avoca bhagavā.]* | brackets removed | spec §2 | BM 7.3 |
| 228, 264, 357, 401 | saññā, viññāṇa, the four later question-and-answer sets and the four later *Yā kāci …* paragraphs abbreviated with "…" | written out in full as BM prints them; identical lines get the repeat note | spec §2, §6 | BM 7.3 |
| 122, 210, 254 | *lbs/labbhati* | *labbhati* | stray text | BM 7.3 |
| passim | BM *viparināma-dhammaṁ* (×5) | *vipariṇāma-dhammaṁ* | BM misprint (dental for retroflex) | DPD vipariṇāma |
| passim | BM *rūpam*, *yam pana*, *diṭṭhadhammānam*, *rūpasmim pi*, *viññāṇasmim pi*, *vimuttam iti*; *bhaṇāma se* | final *ṁ*; *bhaṇāmase* | spec §2 niggahīta; BM word split (as 07a/01) | DPD |
| passim | 72 lint errors: tags `+`, `imp`; coverage faults (*evaṁmerūpaṁ*, *lbs*); no member rows | all rows redrafted to spec §4 with ↳ member rows | spec §4 | DPD |
| passim | "monks", BM-style English in Faithful lines | Faithful lines re-rendered from the Pāli; *bhikkhus* | spec §3 | DPD |
| 2 lines | *Aniccā bhante.* and *ajjhattā vā bahiddhā vā …* for *saṅkhārā* | own tables (masc pl), not repeat notes | the identical lines for *vedanā* are fem sg | grammar |
| end | citation missing | *SN 22.59; Kd 1:6.38–6.47* | spec §5 | SuttaCentral |
| row | *sutvā* (Evaṁ passaṁ …) | `(abs)` having heard; Literal and Faithful lines to match (also in 03) | bhikkhu's decision, query 50 (2026-10-05) | BM 7.3 |

### 03_aditta_pariyaya_sutta.md
Redrafted from BM 7.5 in the spec format (420 → 1065 lines; 23 → 88 Pāli units; 191 → 388 rows incl. ↳ member rows; repeat notes for the refrains). Checked against DPD (local db, 26 Sept 2026).

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| top | `# Āditta-pariyāya-sutta`, no English title | English title added | spec §1 | BM 7.5 |
| top | BM's solo introduction (*Veneyyadamanopāye* … *bhaṇāma se*, 8 lines) missing | added under *(Solo introduction)* | chant incomplete | BM 7.5 |
| passim | leader brackets *[Evaṁ me sutaṁ]*, *[Evaṁ passaṁ bhikkhave]*, *[Idam-avoca bhagavā.]*; whole bracketed sense paragraphs (ear, nose; ear, nose, body, mind) abbreviated with "…" | brackets removed; all six sense paragraphs written out as BM prints them; identical lines get the repeat note | spec §2, §6 | BM 7.5 |
| passim | long BM paragraphs as one unit | divided at phrase boundaries | spec §2 | BM 7.5 |
| passim | BM *jivhāviññāṇam*, *tam pi*, *vimuttam iti*; *pāramiṁgato*, *manosamphassepi*; *bhaṇāma se* | final *ṁ*; spaces restored; *bhaṇāmase* | spec §2; BM spacing artefacts; BM word split | DPD |
| passim | lint errors (tags, coverage, no member rows); BM-style English in Faithful lines | all rows redrafted to spec §4; Faithful lines re-rendered from the Pāli | spec §3, §4 | DPD |
| end | *S.IV.19; Vin.I.34* | *SN 35.28; Kd 1:21.1–21.4* | spec §5 | SuttaCentral |
| row | *viññūṇaṁ* | BM's *-ṇaṁ* kept, with a note (also *-saññāṇaṁ* in 02) | bhikkhu's decision, query 49 (2026-10-05): later commentarial style | BM 7.5 |

Spot check (independent subagent, 10 units across 02–03): 2 with errors, fixed (02 solo introduction *yantaṁ … anattalakkhaṇaṁ*, *vimocanaṁ* acc → nom; 03 Faithful line kept the five plurals *sokehi … upāyāsehi*); 1 debatable accepted (03 *Ciṇṇāggi…* Faithful line: "long", "sacred" removed, *araha* "worthy").

## 2026-10-04 — session S12 (07a_suttas 01)

### 01_dhammacakkappavattana_sutta.md
Redrafted from BM 7.1 in the spec format (763 → 1591 lines; 41 → 113 Pāli units; 427 → 712 rows incl. ↳ member rows; 32 repeat notes). Checked against DPD (local db, 26 Sept 2026).

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1–63 | stray opening fragment (*Atha kho bhagavā udānaṁ udānesi* … *niṭṭhitaṁ*) and heading "Complete Compiled Chant File" | removed | stray duplicate text | spec §1 |
| top | `# Dhammacakkappavattana-sutta`, no English title | English title added | spec §1 | BM 7.1 |
| top | BM's solo introduction (*Anuttaraṁ abhisambodhiṁ* … *bhaṇāma se*, 8 lines) missing | added under *(Solo introduction)* | chant incomplete | BM 7.1 |
| passim | leader brackets *[Evaṁ me sutaṁ]*, *[Idaṁ dukkhaṁ]*, *[Yāva kīvañca me bhikkhave]*, *[Pavattite ca bhagavatā]*, *[Atha kho …]* | brackets removed | spec §2 | BM 7.1 |
| 431–483 | twelve-aspect passage abbreviated with "…" and "/" | written out in full as BM prints it; *pubbe ananussutesu dhammesu* and *cakkhuṁ udapādi …* as their own units with repeat notes | spec §2, §6 | BM 7.1 |
| 640 | deva chain compressed into one line with "/" | BM's seven lines; refrain *Etaṁ bhagavatā …* after *brahmakāyikā* only, as BM and Thanissaro chant it | spec §2 | BM 7.1; Thanissaro |
| intro, 286 | BM *Pathamaṁ*, *appativattiyaṁ*, *Veyyākaraṇapāthena*, *maranampi* | *Paṭhamaṁ*, *appaṭivattiyaṁ*, *Veyyākaraṇapāṭhena*, *maraṇampi* | BM misprints (dental for retroflex; BM itself has *appaṭivattiyaṁ* later in 7.1); confirmed by the bhikkhu (query 48, 2026-10-04) | DPD |
| passim | BM *saṅgītantam*, *seyyathīdam*, *suvisuddham*, *ath'āham*; *bhaṇāma se* | final *ṁ*; *bhaṇāmase* | spec §2 niggahīta; BM word split (as 04a) | DPD |
| passim | ~200 lint errors: tags `pr n`, `ptcl`, `emphp`, `pers`, `quote`; coverage faults; no member rows; repeats written out | all rows redrafted to spec §4 with ↳ member rows | spec §4 | DPD |
| passim | BM's English echoed in Faithful lines | Faithful lines re-rendered from the Pāli | spec §3 | DPD |
| end | citation missing | *SN 56.11; Kd 1:6.17–6.31* | spec §5 | SuttaCentral |
| rows | *aṅgiko* [aṅga + ika] (as in 03/19) | [√añj > aṅg + a + ika] | DPD root; 03/19 to align at 07a step 9 | DPD aṅgika |
| rows | *appiyehi*, *piyehi* [na + √pī + a], [√pī + a] (as in 01/06) | [na > a + √pī > piy + a], [√pī > piy + a] | DPD construction; 01/06 to align at step 9 | DPD piya |

Spot check (independent subagent, 10 units): 3 with errors, fixed (*punabbhavo'ti* member rows; ↳ *bhūtaṁ* class; *imasmiṁ* tag); also *pana* rendered, "it" removed from deva-chain Faithful lines.

## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 05_dhaj_agga_sutta.md | 17 etymologies | aligned: *anuttaro*, *bhavissati*, *bhikkhave*, *bhikkhavo*, *niyyānikaṁ*, *pi*, *siyā*, *svākkhāto*, *viharati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 01_dhammacakkappavattana_sutta.md | 37 etymologies | aligned: *ariyo*, *atta*, *ayam-eva*, *aṭṭhaṅgiko*, *bhikkhave*, *dhammesu*, *diṭṭhi*, *dukkha*, *kammanto*, *katamā*, *kāmesu*, *maggo*, *pabbajitena*, *pi*, *samādhi*, *saṅkappo*, *soka*, *sukha*, *suttaṁ*, *ubho*, *viharati*, *vimutti*, *vācā*, *vāyāmo*, *ñāṇaṁ*, *ājīvo* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_anatta_lakkhana_sutta.md | 40 etymologies | aligned: *ajjhattaṁ*, *anattā*, *attā*, *bhikkhave*, *hontu*, *hoti*, *hotu*, *niccaṁ*, *pi*, *saṅkhārā*, *sukhaṁ*, *tasmā*, *vedanā*, *viharati*, *virāgā*, *ñāṇaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 06_girimananda_sutta.md | 39 etymologies | aligned: *anattā*, *aniccā*, *aṭṭhi*, *bhikkhu*, *cetaso*, *katamā*, *kāye*, *kāyo*, *lohitaṁ*, *mano*, *saṅkhārā*, *taco*, *vedanā*, *viharati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 08_bhikkhu_aparihaniya_dhamma.md | 35 etymologies | aligned: *anāgatā*, *bhavissanti*, *bhikkhave*, *dhammesu*, *iti*, *katame*, *pāṭikaṅkhā*, *therā*, *viharati*, *ye* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 03_aditta_pariyaya_sutta.md | 17 etymologies | aligned: *bhikkhave*, *brahmacariyaṁ*, *hoti*, *kāyo*, *mano*, *pi*, *sukhaṁ*, *viharati*, *virāgā*, *ñāṇaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 07_maha_samaya_sutta.md | 32 etymologies | aligned: *asubhaṁ*, *bhavissanti*, *bhikkhave*, *bhikkhavo*, *cetaso*, *devatā*, *devesu*, *disā*, *pahāya*, *pi*, *puriso*, *saraṁ*, *sāsanaṁ*, *tattha*, *viharati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 10_saraniya_dhamma_sutta.md | 20 etymologies | aligned: *ariyā*, *bhikkhave*, *bhikkhavo*, *diṭṭhi*, *hoti*, *katame*, *viharati*, *ye* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 12_itivuttaka_49_ditthigatasutta.md | 15 etymologies | aligned: *attā*, *bhedā*, *bhikkhave*, *bhikkhu*, *hoti*, *passati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 09_gotami_sutta.md | 1 etymologies | aligned: *viharati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 01_dhammacakkappavattana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 87 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 107 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 255 | sammā [saṁ- + -mā] | [sammā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 283 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 308 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 363 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 403 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 441 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 461 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 470 | vijjā [√vid + -yā] | [√vid + yā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 547 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 598 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 606 | natthi [na + √as + -ti] | [na + √as + ti] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 743 | saddo [√sad + -a] | [√sadd + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 786 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 102 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 152 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 213 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 252 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 391 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 42 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_dhaj_agga_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 32 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 81 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 147 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 237 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 296 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 461 | puññakkhettaṁ [puñña (√puṇ + ya) + khetta (√khi + tta)] | [puñña + khetta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 572 | puññakkhettaṁ [puñña (√puṇ + ya) + khetta (√khi + tta)] | [puñña + khetta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 70 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 86 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 141 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 172 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 227 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 278 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 349 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 370 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 422 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 559 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 1329 | seṭṭho [seṭṭha] | [seṭṭha, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 1381 | abbhuggato [abhi-ud-√gam + ta] | [abhi + ud + √gam + ta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 1490 | yathā [yathā] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 1523 | sāsane [sāsana] | [√sās + ana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 08_bhikkhu_aparihaniya_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | me [base `aham`] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 44 | kho [emphatic particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 62 | dhamme [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 93 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 09_gotami_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [√an + pronoun base ma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 84 | me [√an + pronoun base ma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 135 | dhamme [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 286 | dhamme [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 10_saraniya_dhamma_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [enclitic 1st pers pron] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 12_itivuttaka_49_ditthigatasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | me [at bodily pronoun base] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 81 | kho [khalu -> kho] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 106 | kho [khalu -> kho] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 159 | kho [khalu -> kho] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 203 | paṭipanno [paṭi + √pad + ta] | [pati + √pad + na] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 214 | kho [khalu -> kho] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 339 | me [at bodily pronoun base] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 01_dhammacakkappavattana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 12 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 101 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 108 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 173 | dukkho [du- + √khā + -a] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 244 | seyyathīdaṁ [seyyathā (sa- + yathā) + idaṁ] | [se + yathā + idaṁ] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 311 | dukkhaṁ [du- + √khā + -a] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 325 | jātipi [jāti + api] | [jāti (√jan + ti) + api] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 326 | dukkhā [dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 328 | jarāpi [jarā + api] | [jarā (√jar + ā) + api] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 331 | dukkhaṁ [dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 339 | sampayogo [saṁ- + pa- + √yuj + -a] | [saṁ + pa + √yuj + e + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 340 | dukkho [dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 342 | vippayogo [vi- + pa- + √yuj + -a] | [vi + pa + √yuj + e + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 347 | labhati [√labh + -a + -ti] | [√labh + a + ti] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 349 | tampi [taṁ + api] | [ta + api] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 350 | saṅkhittena [saṁ- + √khip + -ta] | [saṁ + √khip + ta + ena] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 388 | seyyathīdaṁ [seyyathā + idaṁ] | [se + yathā + idaṁ] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 458 | dukkhaṁ [dukkha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 562 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 568 | anuttaraṁ [an- + uttara] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 623 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 627 | bhagavato [bhagavant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 672 | bhagavatā [bhagavant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 688 | bhagavatā [bhagavant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 692 | anuttaraṁ [an- + uttara] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 718 | sutvā [√su + -tvā] | [√su + tvā] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 768 | loke [√lok + -a] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 787 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 02_anatta_lakkhana_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 42 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 58 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 85 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 103 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 121 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 122 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 134 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 153 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 168 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 233 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 267 | saññā [saṁ- + √ñā + ā] | [saṁ + √ñā + ā] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 280 | saṅkhārā [saṁ- + √kar + a] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 281 | anattā [an- + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 309 | viññāṇaṁ [vi- + √ñā + ana] | [vi + √ñā + aṇa] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 326 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 329 | aniccaṁ [a- + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 341 | aniccaṁ [a- + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 342 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 355 | dukkhaṁ [du- + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 370 | dukkhaṁ [du- + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 371 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 405 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 417 | saññā [saṁ- + √ñā + ā] | [saṁ + √ñā + ā] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 418 | saṅkhārā [saṁ- + √kar + a] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 419 | viññāṇaṁ [vi- + √ñā + ana] | [vi + √ñā + aṇa] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 435 | rūpaṁ [rūpa] | [√rūp + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 482 | sutvā [√su + ta + vant] | [√su + tvā] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 551 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 555 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 03_aditta_pariyaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 43 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 102 | dukkhaṁ [du + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 134 | sokehi [soka (√suc + a)] | [√suc + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 135 | paridevehi [pari-√div + a] | [pari + √dev + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 136 | dukkhehi [du + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 137 | domanassehi [du- + manas + ya] | [dur + √man + as + ya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 138 | upāyāsehi [upa-ā-√yas + a] | [upa + ā + √yas + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 235 | dukkhaṁ [du + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 290 | dukkhaṁ [du + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 368 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 372 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 05_dhaj_agga_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 15 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 33 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 50 | bhagavato [bhagavant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 52 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 328 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 329 | arahaṁ [√arah + -ant] | [√arah + ant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 332 | sugato [su + √gam + -ta] | [su + √gam + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 334 | anuttaro [an- + uttara] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 336 | satthā [√sās + -tar] | [√sās + tar] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 338 | buddho [√budh + -ta] | [√budh + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 367 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 378 | svākkhāto [su + ā- + √khā + -ta] | [su + ā + √khā + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 379 | bhagavatā [bhagavant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 380 | dhammo [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 381 | sandiṭṭhiko [saṁ- + √dis + -ta + -ika] | [saṁ + √dis + ti + ka] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 382 | akāliko [a- + kāla + -ika] | [na + √kal + a + ika] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 384 | opanayiko [upa- + √nī + -aya + -ika] | [upa + √nī + a + ika] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 385 | paccattaṁ [pati- + atta] | [pati + atta + aṁ] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 386 | veditabbo [√vid + -itabba] | [√vid + e + itabba] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 398 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 410 | saṅghaṁ [saṁ- + √han + -a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 422 | supaṭipanno [su + paṭi- + √pad + -ta] | [su + pati + √pad + na] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 423 | bhagavato [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 439 | cattāri [catu] | [catu + āri] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 444 | bhagavato [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 456 | āhuneyyo [ā- + √hu + -aneyya] | [ā + √hu + ana + eyya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 457 | pāhuneyyo [pa- + ā- + √hu + -aneyya] | [pa + ā + √hu + ana + eyya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 458 | dakkhiṇeyyo [dakkhiṇā + -eyya] | [√dakkh + iṇā + eyya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 460 | anuttaraṁ [an- + uttara] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 461 | puññakkhettaṁ [puñña + khetta] | [puñña (√puṇ + ya) + khetta (√khi + tta)] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 473 | saṅghaṁ [saṁ- + √han + -a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 488 | tathāgato [tathā + √gam + -ta] | [tathā + gata (√gam + ta) / tatha + āgata] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 491 | arahaṁ [√arah + -ant] | [√arah + ant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 512 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 515 | sugato [su + √gam + -ta] | [su + √gam + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 518 | satthā [√sās + -tar] | [√sās + tar] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 553 | buddhaṁ [√budh + -ta] | [√budh + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 558 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 571 | saṅghaṁ [saṁ- + √han + -a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 572 | puññakkhettaṁ [puñña + khetta] | [puñña (√puṇ + ya) + khetta (√khi + tta)] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 573 | anuttaraṁ [an- + uttara] | [na + ud + tara] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 587 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 06_girimananda_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 44 | aniccaṁ [an + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 46 | aniccā [an + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 49 | aniccā [an + nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 50 | viññāṇaṁ [vi + √ñā + ana] | [vi + √ñā + aṇa] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 114 | anattā [an + attan] | [na + atta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 283 | seyyathīdaṁ [seyyathā + idaṁ] | [se + yathā + idaṁ] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 571 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 07_maha_samaya_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 27 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 56 | bhagavantaṁ [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 87 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 106 | bhagavantaṁ [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 122 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 125 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 158 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 175 | bhagavantaṁ [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 230 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 281 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 352 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 423 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 562 | bhagavato [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 564 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 705 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 749 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 792 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 835 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 880 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1032 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1079 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1126 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1422 | bhikkhūnaṁ [bhikkhu] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1521 | satthā [satthar] | [√sās + tar] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1522 | sāvake [sāvaka] | [√su + aka] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 1546 | buddhassa [buddha] | [√budh + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 08_bhikkhu_aparihaniya_dhamma.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 28 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 45 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 91 | bhante [voc. of `bhadanta`] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 96 | bhagavato [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 108 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 126 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 145 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 171 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 200 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 235 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 260 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 283 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 317 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 336 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 348 | bhikkhūnaṁ [√bhikkh + -u + -ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 364 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 368 | bhagavato [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 09_gotami_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 15 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 35 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 49 | bhagavantaṁ [bhaga + -vant + -aṁ] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 70 | bhagavantaṁ [bhaga + -vant + -aṁ] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 85 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 86 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 87 | saṅkhittena [saṁ- + √khip + -ta + -ena] | [saṁ + √khip + ta + ena] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 88 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 102 | bhagavato [bhaga + -vant + -o] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 103 | dhammaṁ [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 104 | sutvā [√su + -tvā] | [√su + tvā] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 148 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 266 | dhammo [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 289 | dhammā [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 406 | dhammo [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 423 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 427 | bhagavato [bhaga + -vant + -o] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 10_saraniya_dhamma_sutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 23 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 39 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 56 | bhagavato [bhagavant + o] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 66 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 403 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 415 | bhagavato [bhagavant + o] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 12_itivuttaka_49_ditthigatasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | bhagavatā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 227 | bhagavā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 337 | bhagavatā [bhaga + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01_dhammacakkappavattana_sutta.md | 86 | evaṁ [eva + -ṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 141 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 214 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 241 | ariyo [√ar + -iya] | [ariya] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 337 | soka-parideva-dukkha-domanass'upāyāsāpi [soka + parideva + dukkha + domanassa + upāyāsa + api] | [soka (√suc + a) + parideva (pari + √dev + a) + dukkha (√dukkh + a) + domanassa (dur + √man + as + ya) + upāyāsa (upa + ā + √yas + a) + api] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 338 | appiyehi [a- + piya (√pī + -ya)] | [na + √pī + a] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 341 | piyehi [piya (√pī + -ya)] | [√pī + a] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 345 | yamp'icchaṁ [yaṁ + api + icchaṁ] | [yaṁ + api + icchaṁ (√is + a + a)] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 595 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 641 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 671 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 01_dhammacakkappavattana_sutta.md | 756 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 10 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 101 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 151 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 212 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 251 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 388 | mama [amha] | [ahaṁ] | DPD lemma / construction | DPD |
| 02_anatta_lakkhana_sutta.md | 479 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_dhaj_agga_sutta.md | 298 | evaṁ [evam] | [eva + aṁ] | DPD lemma / construction | DPD |
| 07_maha_samaya_sutta.md | 12 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 13 | evaṁ [adv.] | [eva + aṁ] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 74 | taṁ [base `ta`] | [ta] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 90 | evaṁ [adv.] | [eva + aṁ] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 122 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 189 | na [particle] | [na] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 192 | na [particle] | [na] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 255 | na [particle] | [na] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 305 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 310 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 333 | ime [base `ima`] | [ima] | DPD lemma / construction | DPD |
| 08_bhikkhu_aparihaniya_dhamma.md | 340 | ca [conjunction] | [ca] | DPD lemma / construction | DPD |
| 10_saraniya_dhamma_sutta.md | 10 | evaṁ [eva + ṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 10_saraniya_dhamma_sutta.md | 78 | ime [ima + e] | [ima] | DPD lemma / construction | DPD |
| 10_saraniya_dhamma_sutta.md | 107 | idha [i + -dha] | [ima + dha] | DPD lemma / construction | DPD |
| 10_saraniya_dhamma_sutta.md | 379 | ime [ima + e] | [ima] | DPD lemma / construction | DPD |
| 12_itivuttaka_49_ditthigatasutta.md | 80 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 12_itivuttaka_49_ditthigatasutta.md | 158 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 12_itivuttaka_49_ditthigatasutta.md | 183 | idha [idha] | [ima + dha] | DPD lemma / construction | DPD |
| 12_itivuttaka_49_ditthigatasutta.md | 213 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |

