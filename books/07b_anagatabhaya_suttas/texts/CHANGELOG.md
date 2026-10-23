# Changelog: 07b_anagatabhaya_suttas

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 03_tatiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 63, 145, 270, 747 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |
| 814 | *bhavissati* √bhū + issa + ti | √bhū + a + issa > bhavissa + ti | DPD future-stem construction | DPD bhavissati 1 |

### 04_catutthaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 63, 208 | *bhavissanti* √bhū + issa + nti | √bhū + a + issa > bhavissa + nti | DPD future-stem construction | DPD bhavissati 1 |
| 467, 585, 624 | *viharissanti* vi + √har + a > hara + issa + nti | vi + √har + a + issa > harissa + nti | DPD future-stem construction | DPD viharissati |

### 05_saddhammappatirupakasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25, 50 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 61, 80 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |

### 06_kimilasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25, 44 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 55, 72 | *bhagavantaṁ* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |


## 2026-10-05 — session S19c (cross-file index, from 07b_anagatabhaya_suttas)

Step-9 alignment after 07b was completed: each word now has the DPD analysis in every file.

### 05_saddhammappatirupakasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 496 | saṁvattanti **[saṁ + √vatt > vatta + nti]** | **[saṁ + √vatt + a + nti]** | align with project notation (same DPD construction) | DPD saṁvattati |
| 600 | saṁvattanti **[saṁ + √vatt > vatta + nti]** | **[saṁ + √vatt + a + nti]** | align with project notation (same DPD construction) | DPD saṁvattati |
| 619 | saṁvattanti **[saṁ + √vatt > vatta + nti]** | **[saṁ + √vatt + a + nti]** | align with project notation (same DPD construction) | DPD saṁvattati |
| 713 | saṁvattantī'ti **[saṁ + √vatt > vatta + nti]** | **[saṁ + √vatt + a + nti]** | align with project notation (same DPD construction) | DPD saṁvattati |

## 2026-10-05 — session S19c (05–06)

Both files were in pre-spec form and were redrafted in full from SuttaCentral (SN 16.13, AN 7.59; `reference-pali-supplement.md`), with every row checked against the local DPD (release 26 Sept 2026). The Pāli of 06 matches SuttaCentral letter for letter; 05 matches except for the closing *Terasamaṁ. Kassapavaggo paṭhamo.*, which is not chanted and is left out (convention since S18). The Pāli text itself was already complete in both old files. Draft sources: `_tools/drafts/07b/c5.py`, `g5*.py`, `g6a.py`.

### 05_saddhammappatirupakasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Saddhammappatīrūpakasutta` (long *ī*), no English title | `# Saddhammappatirūpaka-sutta` + *The Discourse on the Counterfeit of the True Dhamma* | spelling; spec §1 | SC sn16.13, DPD |
| all | 28 long units; `---` lines; no citation; curly quotation marks | 49 units at clause boundaries; 5 repeat notes; citation *SN 16.13*; quotation marks removed, `'ti` kept | spec §1, §2, §5, §6 | SC sn16.13 |
| all | non-canonical tags (`pr`, `enclitic`, `compound`, `neg`, `conj`, `num`, `particle`, `part`, `grd`, `inst`, `ppp`) | canonical tags | spec §4 | — |
| all | compounds without member rows (*jetavana*, *anāthapiṇḍika*, *mahākassapa*, *sikkhāpada*, *saddhamma*, *saddhammappatirūpaka*, *jātarūpa*, *jātarūpappatirūpaka*, the four *-dhātu*, *moghapurisa*); *appatara*, *bahutara* tagged as compounds | member rows added; *appatara*, *bahutara* as comparatives [appa + tara], [√bah + u + tara] | spec §4 | DPD |
| all | bare-lemma etymologies (*kassapa*, *bhikkhu*, *satthu*, *sikkhā*, *bhikkhunī*); *saddhamma* [sant + dhamma] | roots or "no root in DPD"; [sat + dhamma], ↳ *sad* `(ind comp)` [√as + a > sa + nta > sat] | DPD | DPD sat, satthar, bhikkhunī |
| 213 ff. | *saddhammappatirūpakaṁ*, *jātarūpappatirūpakaṁ* | `(nt nom sg comp)` with note: DPD gives masc, but the *-aṁ* form is the subject of *uppajjati* | grammar | DPD |
| 116 ff. | *aññāya* | `(fem dat sg)` "in final knowledge" | grammar | DPD aññā 2 |
| all | *khome*, *evañcetaṁ*, *yenetarahi*, *idheva*, *ādikeneva*, *evameva*, *ceva* as single words | `(sandhi)` rows with each part's tags | spec §4 | DPD |
| 257 ff. | *seyyathāpi* `(ind)` | `(sandhi)` [*se* + *yathā* + *api*] | DPD gives it as sandhi | DPD seyyathāpi |
| all | *ādikeneva* "from the very beginning"; *okkamaniyā* "leading to decline" | "in just one go" (DPD *ādikena* "with the first attempt"); "detrimental" | meaning | DPD ādikena, okkamaniya |
| all | loose Faithful lines; *ceva*, *kho*, *tāva* not rendered | Faithful lines checked against Pāli and DPD only; particles rendered ("indeed both", "does not yet come about") | spec §3; spot check | grammar |

### 06_kimilasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Kimila Sutta`, no English title | `# Kimila-sutta` + *The Discourse to Kimila* | spec §1 | style-spec |
| all | 10 long units (seven reverence items in one line); no citation | 31 units; 5 repeat notes; citation *AN 7.59*; quotation marks removed | spec §2, §5, §6 | SC an7.59 |
| all | tags `inst`, `absolute` | canonical tags; locative absolute as a note | spec §4 | — |
| all | compounds without member rows (*niculavana*, *tathāgata*, *saddhamma*, *ciraṭṭhitika*); *parinibbute* [pp. of √vā + pari- + ni- + -ta] | member rows; [pari + nī + √vā > vu > bu + ta] | spec §4; DPD | DPD |
| all | reverence lines differ from 05's | shared with 05 (same rows, generator `c5.py`) | consistency | — |
| all | Faithful omitted *kho* in the frame lines | "Then indeed …", "Seated to one side indeed …" | emphatic particle (spot check) | grammar |

## 2026-10-05 — session S19b (03–04)

Both files were in pre-spec form and were redrafted in full from SuttaCentral (AN 5.79, AN 5.80; `reference-pali-supplement.md`), with every row checked against the local DPD (release 26 Sept 2026). The Pāli of both files now matches SuttaCentral word for word (normalised comparison, ratio 1.000). Spot check: 1 of 10 units with an error (fixed: *kho* not rendered, 04).

### 03_tatiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Tatiyaanāgatabhayasutta`, no English title | `# Tatiya-anāgatabhaya-sutta` + *The Third Discourse on Future Dangers* | spec §1 | style-spec |
| 1st and 2nd dangers | second cycle missing (*Te abhāvitakāyā samānā … aññe upasampādessanti / aññesaṁ nissayaṁ dassanti. Tepi na sakkhissanti … Tepi bhavissanti …*) | restored | incomplete text (old file similarity 0.942) | SC an5.79:2.6–2.8, 3.5–3.7 |
| all | 38 long units; no citation; curly quotation marks | 84 units divided at clause boundaries; 39 repeat notes; citation *AN 5.79*; quotation marks removed, `'ti` | spec §2, §5, §6 | SC an5.79 |
| all | "monks", "realization", "recognized"; BM-free but loose Faithful lines | *bhikkhus*; British spelling; Faithful lines checked against Pāli and DPD only; implied subjects bracketed in Literal lines | spec §3 | DPD |
| all | non-canonical tags (`bahubbīhi`, `part`, `desid`, `fut pass part`, `prp act` order, finite verbs without mood) | canonical tags | spec §4 | — |
| all | compounds without member rows (*anāgatabhaya*, *abhāvitakāya* etc., *dhammasandosa*, *vinayasandosa*, *abhidhammakathā*, *vedallakathā*, *kaṇhadhamma*, *suttanta*, *tathāgatabhāsita*, *gambhīrattha*, *lokuttara*, *suññatāppaṭisaṁyutta*, *cittakkhara*, *cittabyañjana*, *sāvakabhāsita*, *pubbaṅgama*, *nikkhittadhura*, *diṭṭhānugati*) | whole row + ↳ member rows, following DPD's constructions | spec §4 | DPD |
| all | *anāgatamaddhānaṁ* `(masc acc sg)` [anāgatam + addhānaṁ] | `(nt acc sg comp)` accusative of time, [anāgata + [m] + addhāna] | DPD | DPD anāgatamaddhānaṁ |
| all | *pañcimāni* as one word [pañca + imāni]; *tepi*, *sāpi* as one word | `(sandhi)` rows with each part's tags | spec §4 | DPD |
| all | non-DPD constructions (*vinetuṁ* [vi- + √nī + tuṁ], *dassanti* [√dā + ssanti], *asamuppanna* [… √pad + ta], *paṭibujjhitabba* [paṭi + √budh + ya + tabba]) | DPD constructions | DPD | DPD |
| 571, 652 | *aññā* | `(fem dat sg)` irregular dative "for understanding, final knowledge" | grammar | DPD aññā 2 |
| 604 | *kāveyyā* | `(adj masc nom pl)` with note: DPD lists *kāveyya* as nt noun "poetry" | grammar | DPD kāveyya |
| 750–840 | *okkamane pubbaṅgamā paviveke nikkhittadhurā* | written out twice with full tables: masc nom pl (elders), then fem nom sg (agreeing with *janatā*); lint's repeat WARN left deliberately | grammar | — |
| 757 | *okkamane* | "in backsliding" (DPD okkamana 2) | meaning | DPD okkamana 2 |

### 04_catutthaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Catuttha Anāgatabhaya Sutta`, no English title | `# Catuttha-anāgatabhaya-sutta` + *The Fourth Discourse on Future Dangers* | spec §1 | style-spec |
| all | 32 long units; no citation; curly quotation marks | 58 units; 17 repeat notes; citation *AN 5.80*; quotation marks removed | spec §2, §5, §6 | SC an5.80 |
| all | "monks"; loose Faithful lines | *bhikkhus*; Faithful lines checked against Pāli and DPD only | spec §3 | DPD |
| all | non-canonical tags (`fpp`, `fpt`, `conj`, `impers`, `assoc`, `num`, `used as …` inside tags) | canonical tags; explanations moved to notes | spec §4 | — |
| all | compounds without member rows (*kalyāṇakāma*, *paṁsukūlikatta*, *piṇḍapātikatta*, *rukkhamūlikatta*, *araññavanapattha*, *senāsana*, *gāmanigamarājadhānī*, *cīvarahetu*, *piṇḍapātahetu*, *senāsanahetu*, *anekavihita*, *jivhagga*, *rasagga*, *bhikkhunīsikkhamānāsamaṇuddesa*, *ārāmikasamaṇuddesa*, *sannidhikāraparibhoga*, *haritagga*) | whole row + ↳ member rows; multi-level compounds follow DPD's construction (*gāmanigama + rājadhānī*, *bhikkhunī + sikkhamānā + samaṇuddesa*, *sannidhikāra + paribhoga*) | spec §4 | DPD |
| all | *gāmanigamarājadhānīsu* [gāma + nigama + rājadhānī]; *cīvarahetu* `(ind/abl sg)` | [gāmanigama + rājadhānī]; `(adv comp)` | DPD | DPD |
| all | *hīnāyāvattissanti* as one verb; *oḷārikampi*, *pathaviyāpi* as one word | `(sandhi)` rows (DPD compound verb *hīnāyāvattati* noted); *haritaggepi* as `comp` row with *pi* noted as joined by sandhi | spec §4 | DPD |
| all | *saṁsagge … sati* not marked | `(masc loc sg)` / `(prp masc loc sg)` with note "locative absolute" | grammar | DPD sati |
| 645 | *nimittaṁ* "sign" | "hint, suggestion" | meaning | DPD nimitta 8 |
| 470, 590 | Faithful omitted *kho* | "Now indeed, bhikkhus, when …" | emphatic particle (spot check) | grammar |

## 2026-10-05 — session S19a (01–02)

Both files were in pre-spec form and were redrafted in full from SuttaCentral (AN 5.77, AN 5.78; `reference-pali-supplement.md`), with every row checked against the local DPD (release 26 Sept 2026). The Pāli of both files matches SuttaCentral word for word (normalised comparison, ratio 1.000). The old files' readings were already complete; the changes below are to structure, analysis and English. Spot check: 0 of 10 units with errors.

### 01_pathamaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Paṭhamaanāgatabhayasutta`, no English title | `# Paṭhama-anāgatabhaya-sutta` + *The First Discourse on Future Dangers* | spec §1 | style-spec |
| all | `[cite: 1]` / `[cite: 1, 3]` after every line and row | removed | stray text | spec §7 |
| all | 26 long units (whole SuttaCentral segments) | 60 units, long segments divided at clause boundaries; 35 later identical lines given the repeat note | spec §2, §6 | SC an5.77 |
| all | Literal/Faithful without the two final spaces; quotation marks; "monks"; "realization" | spec form; *bhikkhus*; British spelling; Faithful lines checked against Pāli and DPD only | spec §1, §3 | DPD |
| all | non-canonical tags (`pres part`, `ind enclitic ptcl`, `1st pers pron`, `card num`, `interrog pron`, `nt nom pl compound`, `(3rd sg pres act)` without mood) | canonical tags | spec §4 | — |
| 3, 171 … | *pañcimāni*, *anāgatabhayāni*, *idaṁ … anāgatabhayaṁ* tagged nom | acc: object of *sampassamānena*; *pañcimāni* as a sandhi row | grammar | DPD pañcimāni |
| all | compounds without member rows (*anāgatabhaya*, *pahitatta*, *kālaṅkiriyā*, *katakamma*, *akatakamma*) | whole row + ↳ member rows | spec §4 | DPD |
| all | sandhi forms analysed as one word (*alameva*, *mamassa*, *handāhaṁ*, *panāhaṁ*, *panāraññe*, *caparaṁ*) | `(sandhi)` rows with each part's tags | spec §4 | DPD deconstructions (*caparaṁ* = *ca* + *paraṁ*) |
| all | invented or non-DPD constructions (*sampassamānena* [sam- + pa- + √pas + māna], *paṭisañcikkhati* [… √cit + ka + ti], *āraññika* [arañña + ika], *pattiyā* [√āp + ti]) | DPD constructions | DPD | DPD |
| 435 | *māṇavehi* "criminals/youths" | "robbers, bandits" (DPD *māṇava* 3) | meaning | DPD māṇava 3 |
| 539 | *vāḷā amanussā* "wild non-humans" | *vāḷā* noted as DPD's noun "beast of prey" qualifying *amanussā*: "savage" | meaning | DPD vāḷa |
| 109 … | *ārabhāmi* (present) | `(1st sg pres act imperat)` "let me arouse", with note | DPD lists imp 1st sg | DPD ārabhati |
| — | — | citation *AN 5.77* added | spec §5 | SC |

### 02_dutiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `# Dutiyaanāgatabhayasutta`, no English title | `# Dutiya-anāgatabhaya-sutta` + *The Second Discourse on Future Dangers* | spec §1 | style-spec |
| all | curly quotation marks in Pāli lines (“ ” ‘); `’ti` | removed; ASCII `'ti` | spec §2 | — |
| all | 42 long units | 84 units, divided at clause boundaries; 37 repeat notes | spec §2, §6 | SC an5.78 |
| all | non-canonical tags, compounds without member rows, sandhi forms analysed as one word, non-DPD constructions (as in 01) | canonical tags; ↳ member rows (*susukāḷakesa*, *araññavanapattha*, *senāsana*, *appābādha*, *appātaṅka*, *nātisīta*, *nāccuṇha*, *padhānakkhama*, *sulabhapiṇḍa*, *dullabhapiṇḍa*, *saṅgaṇikavihāra*, *ākiṇṇavihāra*, *khīrodakībhūta*, *aññamañña*, *piyacakkhu*, *aṭavisaṅkopa*, *cakkasamārūḷha*, *ekuddesa*); sandhi rows (*yenāhaṁ*, *paṭikacceva*, *jiṇṇakopi*, *byādhitopi*, *dubbhikkhepi*, *bhayepi*, *bhinnepi*) | spec §4 | DPD |
| all | *yaṁ* (in *so samayo yaṁ*) as relative pronoun | `(ind)` "when" | grammar | DPD yaṁ 3 |
| all | *sati*, *bhinne* in locative absolutes not marked | `(prp … loc sg)` / `(pp masc loc sg)` with note "locative absolute" | grammar | DPD sati 2.1 |
| all | *paggahena* "with effort" | "by handouts, by donations" | meaning in context | DPD paggaha 2 |
| all | *dhammo* (in *purā maṁ so dhammo āgacchati*) "Dhamma" | "state, condition" | meaning | DPD |
| 747 | *phāsu* (bare form) tagged as *phāsuṁ* | `(ind)` "at ease" | form | DPD phāsu 3 |
| — | — | citation *AN 5.78* added | spec §5 | SC |

## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 05_saddhammappatirupakasutta.md | 18 etymologies | aligned: *asammosāya*, *hoti*, *katame*, *tāva*, *ye*, *ṭhitiyā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 03_tatiyaanagatabhayasutta.md | 54 etymologies | aligned: *anadhigatassa*, *appattassa*, *asacchikatassa*, *bhavissanti*, *bhavissati*, *bhikkhave*, *catutthaṁ*, *cittaṁ*, *dutiyaṁ*, *pahānāya*, *pattiyā*, *paṭhamaṁ*, *sacchikiriyāya*, *tatiyaṁ*, *therā*, *vīriyaṁ*, *ye* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_dutiyaanagatabhayasutta.md | 122 etymologies | aligned: *adhigamāya*, *anadhigatassa*, *appattassa*, *asacchikatassa*, *bhikkhave*, *bhikkhu*, *catutthaṁ*, *dhammena*, *dutiyaṁ*, *hoti*, *pattiyā*, *paṭhamaṁ*, *sacchikiriyāya*, *samaggo*, *sampassamānena*, *tatiyaṁ*, *tattha*, *viharati*, *vīriyaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 04_catutthaanagatabhayasutta.md | 33 etymologies | aligned: *bhavissanti*, *bhikkhave*, *catutthaṁ*, *dutiyaṁ*, *pahānāya*, *paṭhamaṁ*, *tatiyaṁ*, *viharissanti* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 06_kimilasutta.md | 12 etymologies | aligned: *atha*, *ayaṁ*, *saddhammo*, *upāsakā*, *viharati* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 02_dutiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 791 | saṅghe [saṁ- + √han + a + e] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 849 | saṅghe [saṁ- + √han + a + e] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 03_tatiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 414 | dhamme [dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 446 | dhamme [dhamma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 556 | pacchimā [pacchima] | [pacchā + ima] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 557 | janatā [jana + tā] | [√jan + a + tā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_saddhammappatirupakasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [mām] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 42 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 66 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 84 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 112 | pana [puna] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 190 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 233 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 239 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 254 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 278 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 298 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 350 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 421 | saṅghe [saṁ + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 454 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 528 | saṅghe [saṁ + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 561 | kho [khalu] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 06_kimilasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [base `mad`] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 36 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 57 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 72 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 104 | dhamme [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 108 | saṅghe [√sañj + -a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 137 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 158 | pana [particle] | [pana] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 189 | dhamme [√dhar + -ma] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 193 | saṅghe [√sañj + -a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 222 | kho [particle] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 02_dutiyaanagatabhayasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 756 | saṅgho [saṁ- + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 779 | saṅgho [saṁ- + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 05_saddhammappatirupakasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 25 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 46 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 50 | bhagavantaṁ [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 69 | bhagavantaṁ [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 85 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 113 | bhante [bhadanta] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 176 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 193 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 219 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 236 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 264 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 281 | loke [loka] | [√lok + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 06_kimilasutta.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 23 | bhagavā [√bhaj + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 40 | bhagavā [√bhaj + -vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 43 | bhagavantaṁ [√bhaj + -vant + -aṁ] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 60 | bhagavantaṁ [√bhaj + -vant + -aṁ] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 73 | bhante [voc. of `bhadanta`] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 159 | bhante [voc. of `bhadanta`] | [voc of bhavant, √bhū + a + nta + e] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 02_dutiyaanagatabhayasutta.md | 48 | idha [idha] | [ima + dha] | DPD lemma / construction | DPD |
| 02_dutiyaanagatabhayasutta.md | 422 | yena [ya + ena] | [ya] | DPD lemma / construction | DPD |
| 02_dutiyaanagatabhayasutta.md | 612 | yena [ya + ena] | [ya] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 10 | evaṁ [evam] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 45 | yena [yad] | [ya] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 89 | yena [yad] | [ya] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 117 | yena [yad] | [ya] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 138 | evaṁ [evam] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 352 | evaṁ [evam] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 397 | idha [idha] | [ima + dha] | DPD lemma / construction | DPD |
| 05_saddhammappatirupakasutta.md | 504 | idha [idha] | [ima + dha] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 10 | evaṁ [adv.] | [eva + aṁ] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 39 | yena [base `ya`] | [ya] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 77 | yena [base `ya`] | [ya] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 81 | na [neg particle] | [na] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 92 | idha [adv.] | [ima + dha] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 142 | yena [base `ya`] | [ya] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 146 | na [neg particle] | [na] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 163 | yena [base `ya`] | [ya] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 177 | idha [adv.] | [ima + dha] | DPD lemma / construction | DPD |
| 06_kimilasutta.md | 227 | yena [base `ya`] | [ya] | DPD lemma / construction | DPD |

