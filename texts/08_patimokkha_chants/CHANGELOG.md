# Changelog: 08_patimokkha_chants

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 03_sil_uddesa_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 30 | *bhagavatā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |
| 176 | *sikkhissāma* √sikkh + issa + ma | √sikkh + a + issa > sikkhissa + ma | DPD future-stem construction (present stem sikkha) | DPD sikkhati 1 |

### 05_samanera_sikkha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |


## 2026-10-11 — queries 58–60 (bhikkhu)

### 03_sil_uddesa_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| citation | *DN 2:42.1; DN 33:3.3.6* | *DN 2:42.1; DN 33:3.3.6; MN 6:2.1* | MN 6:2.1 is the exhortation word for word; BM's references kept (query 58) | SC mn6:2.1 |

Query 59: 05's fifth precept keeps DPD's reading in the Faithful line, with the commentarial reading in the row note (no change). Query 60: the English titles of 02, 03 and 05 are accepted (no change).

## 2026-10-11 — session S21 (08_patimokkha_chants, all 5 files)

All five files were in pre-spec form and were redrafted from BM 8.1–8.5 (pp. 205–213) with `b.py`. Draft sources: `_tools/drafts/08/`. Pāli identical to BM after normalisation (`compare`; `nc.py` for 02). Every row checked against DPD (local database, release of 26 Sept 2026). Common to all files: `---` lines and `[cite: 1]` tags removed; *English title* line added; BM's *Handa mayaṁ …* leader line added as the first unit (01–04); ↳ member rows added to every compound; tags put in canonical form (`pres act imperat`, `instr`, `dem pron`, `card`; non-canonical `neg`, `conj`, `indef pron`, `num`, `pers`, `fpp`, `compound`, `in cmpd`, `quote marker` removed); BM citations converted to SuttaCentral IDs; repeated lines given the repeat note.

### 01_ovada_patimokkha_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | — | *Verses on the Training Code*; leader line *Handa mayaṁ ovāda-pāṭimokkha-gāthāyo bhaṇāmase* | spec §1; leader lines included | BM 8.1 |
| citation | none | *Dhp 183–185* | spec §5 | BM; SC dhp183–185 |
| kusalassūpasampadā | [kusala + gen sg (-assa) + upa-saṁ-√pad + ā] | comp row [kusalassa + upasampadā], members *kusalassa*, *upasampadā* [upa + saṁ + √pad + ā] | DPD compound | DPD |
| sacitta-pariyodapanaṁ | [sa + citta + pari-ava-√dā + a + ana] | [sacitta + pariyodapana]; *pariyodapanaṁ* [pari + y + ava + √dā > dape + ana] | DPD construction | DPD |
| buddhāna | no note | note: *-ṁ* dropped for the metre | grammar | DPD |
| tapo | `(nt nom sg)` [√tap + as] | `(masc nom sg)`; *paramaṁ* `(adj nt nom sg)` with a note | DPD *tapas* masc | DPD |
| tītikkhā | [√tij + sa + ā] | [√tij + tij + sa > titikkha + ā] | DPD desiderative | DPD |
| nibbānaṁ | [ni-√vā + ana] | [nī + √vā > bā + ana] | DPD | DPD nibbāna 2 |
| pabbajito | `(masc nom sg pp)` [pa-√vaj + ita] | `(masc nom sg)` [pa + √vaj > baj + ita] | DPD pabbajita 1 (noun) | DPD |
| parūpaghātī | `(masc nom sg)` [para + upa-√han + in] | `(adj masc nom sg comp)` [para + upaghātī], *upaghātī* [upa + √ghaṭ > ghāṭ + ī] | wrong root (√han); DPD √ghaṭ | DPD |
| samaṇo hoti | Faithful "nor is one a renunciant who harms another" with no note | note on *hoti*: the *na* of the line before carries over; SC reads *na samaṇo* | BM and Thanissaro both omit *na*; BM kept | BM; Thanissaro; SC dhp184 |
| samaṇo | [√sam + ana] | [√sam + aṇa] | DPD | DPD |
| viheṭhayanto | `(masc nom sg prp act)` | `(prp masc nom sg)` [vi + √heṭh + aya + nta] | tag order | spec §4 |
| anūpaghāto | [an- + upa-√han + ta] | [na > an + upa + √ghaṭ > ghāṭ + a] | wrong root | DPD anūpaghāta |
| pāṭimokkhe | `(nt loc sg)` [pa-ati-√muc + a] | `(masc loc sg)` [pāṭimokkha, no root in DPD] | invented root; DPD masc | DPD |
| mattaññutā | [matta + √ñā + ū + tā] | comp row, members *matta* [√mā + ta], *ññutā* [√ñā + ū + tā] | compound | DPD |
| bhattasmiṁ | Faithful "moderation in eating" | "knowing the right amount in food" | *ca* rendered; Faithful checked against Pāli | grammar |
| pantañca | `(nt nom/acc sg)` [panta + ca] | `(sandhi)` [pa + anta; + ca] | sandhi row | spec |
| sayan'āsanaṁ | [√sī + ana + √ās + ana] | comp row [sayana + āsana] with members | compound | DPD |
| adhicitte | [adhi + citta] | [adhi + √cit + ta] | DPD | DPD |
| āyogo | [ā-√yuj + a] | [ā + √yuj + e > yoje > yoge + a] | DPD | DPD |
| 2nd *Etaṁ buddhāna sāsanaṁ* | full table | repeat note | spec §6 | spec |

### 02_sacca_kiriya_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | — | *Verses of the Act of Truth*; leader line *Handa mayaṁ sacca-kiriyā-gāthāyo bhaṇāmase* | spec §1 | BM 8.2 |
| all rows | unchecked analyses | rows of 04a/16 (checked S6b), with *me* for *te/me* | same verses; one analysis | 04a/16 |
| sacca-vajjena | members given as ordinary rows before the compound (coverage error) | comp row followed by ↳ *sacca*, *vajjena* | spec §4 | spec |
| buddho | `(masc nom sg pp)` | `(masc nom sg)` | noun | DPD |
| sotthi | `(fem/nt nom sg)` [su + atthi] | `(fem nom sg)` [su > so + √as + ti] | as 04a/16 | DPD |
| 2nd and 3rd *Etena sacca-vajjena …* | full tables | repeat note | spec §6 | spec |
| Faithful *Etena …* | "may safety be mine always" | "may I be safe at all times" | as 04a/16 | 04a/16 |

### 03_sil_uddesa_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | — | *Passage for the Recitation of Virtue*; leader line *Handa mayaṁ sīl'uddesa-pāṭhaṁ bhaṇāmase* | spec §1 | BM 8.3 |
| citation | none | *DN 2:42.1; DN 33:3.3.6* | BM's D.I.63; D.III.266f converted (PTS pages via SC reference data) | SC |
| bhāsitam | no note | note: *-ṁ* written *m* before a vowel | BM spelling | spec |
| jānatā | [√ñā + nā + nta] | [√ñā + nā > jānā + nta] | DPD | DPD |
| sampanna-sīlā (twice) | `(masc voc pl)` (1st), `(masc nom pl)` (2nd) [saṁ-√pad + na + sīla] | `(adj masc nom pl comp)` with members | predicate of *viharatha* / *viharissāma*, not vocative; DPD adj | DPD *sampannasīla* |
| sampanna-pāṭimokkhā (twice) | `(masc voc pl)` (1st), `(masc nom pl)` (2nd) [… pati-√muc + a] | `(adj masc nom pl comp)` [sampanna + pāṭimokkha] | as above; invented root | DPD |
| pāṭimokkha-saṁvara-saṁvutā (twice) | `(masc voc pl pp)` / `(masc nom pl pp)` | `(adj masc nom pl comp)` [pāṭimokkha + saṁvara + saṁvuta], members | DPD adj; nominative | DPD |
| ācāra-gocara-sampannā | `(masc voc pl pp)` (1st), `(masc nom pl pp)` (2nd) | `(adj masc nom pl comp)` [ācāragocara (ācāra + gocara) + sampanna] | DPD adj; nominative (S21 spot check) | DPD |
| viharatha | `(2nd pl pres imp act)` | `(2nd pl pres act imperat)` | tag form | spec §4 |
| vajjesu | [√vajj + a] | [√vajj + ya > vajja] | DPD vajja 2.1 | DPD |
| bhaya-dassāvī | [bhaya + √dis > dassa + āvīn] | comp row [bhaya + dassāvī]; note on the *-ī* nom pl | DPD | DPD |
| sikkhāpadesū'ti | `(nt loc pl + ind)` [sikkhā + pada + iti] | comp row with members and *'ti* noted as joined by sandhi | spec | spec |
| Tasmā-tiha / amhehi | two rows, coverage error | one `(sandhi)` row *tasmā-tih'amhehi* | coverage | DPD *tasmātiha* |
| sikkhitabbaṁ | `(nt nom sg fpp)` | `(ptp nt nom sg)` | canonical tag | spec |
| no | `(1st ins pl)` [amha > no] | `(1st pl dat/gen)` [ahaṁ], note: agent of *sikkhitabbaṁ* | DPD forms of *no* | DPD |
| Faithful | "consummate", "train yourselves" | own renderings | not echoing Thanissaro | spec §3 |
| 2nd *ācāra-gocara-sampannā*, *Aṇu-mattesu …* | full tables | repeat note | spec §6 | spec |

### 04_tayana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | `[cite: 1]` after every line; file had 0 Pāli lines for the script | removed | stray text | spec §7 |
| title | — | leader line *Handa mayaṁ tāyana-gāthāyo bhaṇāmase* | BM 8.4 | BM |
| citation | none | *SN 2.8* | BM's S.I.49f | SC |
| chinda | `(2nd sg pres imperat act)` [√chid + ṁ-a] | `(2nd sg pres act imperat)` [√chid + ṁa > chinda] | tag order; DPD | DPD |
| sotaṁ | [√su + ta] | [√su > so + ta] | DPD | DPD |
| parakkamma | [pa + vi + √kam + ttvā > parakkamma] | [parā + √kam + ya] | invented construction | DPD |
| panūda | [pa + √nud + a] | `(2nd sg pres act imperat)` of *panūdati* [pa + √nud + a > nuda > nūda] | DPD *panūdati* | DPD |
| brāhmaṇa | [brahman + a] | [√brah > brāh + ma + aṇa] | DPD | DPD |
| nappahāya | `(neg abs)` | `(abs)`, note [*na* + *pahāya*] | non-canonical tag | spec |
| muni | [√man + i] | [√mun + i] | wrong root | DPD |
| n'ekattam / upapajjati | `(neg nt acc sg)`; `(3rd sg pres ind act)` | `(sandhi)` *n'ekattam-* + `(3rd sg pres act indic)` *upapajjati* | tags; DPD *nekattamupapajjati* | DPD |
| kayirā | [√kar + irā] | [√kar + o > karo + eyya > kayirā] | DPD | DPD |
| kayirāthenaṁ | `(3rd sg opt act + pron masc acc sg)` | `(sandhi)` [*kayirātha* (3rd sg mid opt) + *enaṁ* (pron nt acc sg)] | DPD sandhi; *enaṁ* "it" | DPD |
| daḷham | `(adv)` [daḷha < √dṛh + a] | `(ind)` [√dah + ta > daḍha > daḷha + aṁ] | Sanskrit root | DPD *daḷhaṁ* |
| parakkame | [para + √kam + a + e] | [parā + √kam + a > kama + e] | prefix *parā* | DPD |
| sithilo | [√sath + ilo] | [sithila, no root in DPD] | invented root | DPD |
| paribbājo | "mendicant life, renunciation" [pari + √vaj + a] | "wandering ascetic" [pari + √vaj > baj > bāj + a] | DPD agent noun | DPD |
| ākirate | `(3rd sg pres ind mid)` | `(3rd sg pres mid indic)` | tag order | spec |
| rajaṁ | `(nt acc sg)` [√raj + a] | `(masc acc sg)` [√raj + as] | DPD *rajas* masc | DPD |
| seyyo | `(adj nom sg comp)` [seyya, compar of sirī …] | `(ind)` [sirī + ya + o] | DPD *seyyo* ind; `comp` misused | DPD |
| pacchā | [paccha < √pasc] | [paccha + ā] | Sanskrit root | DPD |
| tappati | `(3rd sg pres ind pass)` | `(3rd sg pres pass indic)` with a note (SC *tapati*) | tag order; reading | DPD; SC |
| nānutappati | `(neg 3rd sg pres ind pass)` [na + anu + √tap + ya + ti] | `(3rd sg pres act indic)` [na + anu + √tapp + a > tappa + ti] | DPD *nānutappati*, √tapp, active | DPD |
| kuso | [kusa] | [kusa, no root in DPD] | spec §4 | DPD |
| duggahito | `(masc nom sg pp)` [du + √gah + ita] | `(adj masc nom sg)` [dur + √gah + ita] | DPD | DPD |
| hattham-evānukantati | one row [hasta + eva + anu + √kant …] | *hattham-* `(masc acc sg)` + *evānukantati* `(sandhi)` [eva; + anu + √kat + ṁa > kanta + ti] | Sanskrit *hasta*; wrong root | DPD |
| sāmaññaṁ | [samaṇa + -ya] | [√sam > sām + aṇa + ya] | DPD | DPD |
| dupparāmaṭṭhaṁ | [du + pari + ā + √mas + ta] | [dur + parā + √mas + ta] | wrong prefix | DPD |
| nirayāyūpakaḍḍhati | `(masc dat sg + 3rd sg pres ind act)` [ni + √i + aya …] | comp row, members *nirayāya* [nir + √i > ay + a], *upakaḍḍhati* | DPD compound verb | DPD |
| kiñci | `(indef pron nt nom sg)` [ka- + ci] | `(ind)` [ka > ki + iṁ + ci] | as checked files | DPD |
| saṅkiliṭṭhañca | [saṁ + √kiles + ta + ca] | `(sandhi)` [saṁ + √kilis + ta; + ca] | wrong root | DPD |
| saṅkassaraṁ | [saṁ + √kas + ara] | comp row [saṅkā + sara] with members | invented construction | DPD |
| brahma-cariyaṁ | `(nt nom sg compound)` | `(nt nom sg comp)` with members | spec §4 | spec |
| mahapphalan'ti | `(nt nom sg adj + quote marker)` [mahant + phala + iti] | comp row with members and *'ti* | spec | DPD |
| Faithful | several lines echoed BM's English | redrafted against the Pāli | spec §3 | spec |

### 05_samanera_sikkha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | — | *The Training of Novices* | spec §1 | spec |
| citations | *Vin.I.83f*, *Vin.I.85*, *Vin.I.84* | *Kd 1:56*, *Kd 1:60*, *Kd 1:57* | spec §5 | SC pli-tv-kd1 |
| anuññāsi | `(3rd sg aor act)` [anu + √ñā + si] | `(3rd sg aor act indic)` [anu + √ñā + āsi] | DPD | DPD |
| sāmaṇerānaṁ etc. | [sāmaṇera + ānaṁ] | [√sam > sām + aṇa + era] | bare lemma for a noun | DPD |
| dasa, pañcahi, dasahi | `(num …)` | `(card …)` | canonical tag | spec |
| sikkhā-padāni | one row [sikkhā (√sikkh + ā) + pada (√pad + a) + āni] | comp row with members | spec §4 | spec |
| tesu | `(nt loc pl)` [ta + su] | `(dem pron nt loc pl)` [ta] | pronoun type | spec |
| ca | `(conj)` | `(ind)` | canonical tag | spec |
| sikkhituṁ | [√sikkh + i + tuṁ] | [√sikkh + ituṁ] | DPD | DPD |
| ten precept compounds | single rows, no members | comp rows with ↳ members (DPD constructions) | spec §4 | DPD |
| surā-meraya-majja-pamādaṭṭhānā | Faithful "wines, liquors, and intoxicants which are a basis for heedlessness" | DPD's dvanda reading in the Faithful line; the commentarial reading given in the row note | DPD | DPD |
| veramaṇī'ti | `(fem nom sg + ind)` [vi + √ram + aṇī + iti] | `(fem nom sg)` with *iti* note [vi > ve + √ram + aṇa + ī; + iti] | spec; DPD | DPD |
| aṅgehi | [aṅga + ehi] | [√añj > aṅg + a] | DPD | DPD |
| samannāgataṁ | `(masc acc sg)` [saṁ + anu + ā + √gam + ta + aṁ] | `(pp masc acc sg)` [saṁ + anu > ann + ā + √gam + ta] | DPD | DPD |
| nāsetuṁ | [√nas + e + tuṁ] | [√nas + e > nāse + tuṁ] | causative base | DPD |
| katamehi | `(pron inst pl)` [katama + ehi] | `(interr pron nt instr pl)` [ka + tama] | pronoun type | DPD |
| pāṇātipātī … bhikkhunī-dūsako | single rows | comp rows with members; *pāṇātipātī*, *adinn'ādāyī*, *abrahma-cārī*, *musā-vādī*, *majja-pāyī*, *micchā-diṭṭhiko* tagged `adj` | DPD adj | DPD |
| avaṇṇaṁ | [a + vaṇṇa + aṁ] | [na > a + √vaṇṇ + a] | DPD | DPD |
| bhikkhūnaṁ | `(masc dat pl)` | `(masc dat/gen pl)` | ambiguous form | grammar |
| alābhāya, anatthāya, anāvāsāya | [a + lābha …], [an + attha + āya], [an + āvāsa …] | [na > a + √labh > lābh + a], [na > an + √ar + tha], [na > an + ā + √vas > vās + a] | DPD | DPD |
| bhikkhū | [bhikkhu + ū] | [√bhikkh + u] | project notation | DPD |
| bhikkhūhi | `(masc inst pl)` | `(masc abl pl)` "from bhikkhus" | *bhedeti* takes the ablative | DPD *bhedeti* |
| daṇḍa-kammaṁ | one row | comp row with members | spec §4 | spec |
| Faithful *Bhikkhunī-dūsako hoti* | "corrupter of nuns" | "a violator of a bhikkhunī" | DPD *bhikkhunidūsaka* | DPD |
| 2nd–4th *Anuññāsi kho Bhagavā* | full tables | repeat note | spec §6 | spec |

## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 03_sil_uddesa_patha.md | 1 etymologies | aligned: *bhikkhave* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 01_ovada_patimokkha_gatha.md | 1 etymologies | aligned: *hoti* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 04_tayana_gatha.md | 2 etymologies | aligned: *bhiyyo*, *hoti* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 05_samanera_sikkha.md | 18 etymologies | aligned: *hoti*, *musā-vādā*, *pāṇātipātā*, *veramaṇī* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_sacca_kiriya_gatha.md | 3 etymologies | aligned: *hotu* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 02_sacca_kiriya_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 12 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 15 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 16 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 27 | sacca [sa + tya / √as + tya] | [sat + ya (√as)] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 31 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 43 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 44 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 47 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 48 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 59 | sacca [sa + tya / √as + tya] | [sat + ya (√as)] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 63 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 75 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 76 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 79 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 80 | saraṇaṁ [√sar + ana] | [√sar + aṇa] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 91 | sacca [sa + tya / √as + tya] | [sat + ya (√as)] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 95 | me [asma] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 04_tayana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 117 | seyyo [√si + īyas > seyyo] | [seyya, compar of sirī, sirī + ya] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 143 | seyyo [√si + īyas > seyyo] | [seyya, compar of sirī, sirī + ya] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 02_sacca_kiriya_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 78 | saṅgho [saṁ + √han + a / saṁ + √gha] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 03_sil_uddesa_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 13 | bhagavatā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 04_tayana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 242 | brahma-cariyaṁ [brahma + √car + ya] | [brahma + cariya (√car + iya)] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 05_samanera_sikkha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 12 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 148 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 230 | buddhassa [buddha (√budh + ta) + ssa] | [√budh + ta] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 285 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 312 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 345 | bhikkhūnaṁ [bhikkhu (√bhikkh + u) + ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 356 | bhikkhūnaṁ [bhikkhu + ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 367 | bhikkhūnaṁ [bhikkhu + ūnaṁ] | [√bhikkh + u] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 402 | bhagavā [bhaga + vant] | [√bhaj + a + vant] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 04_tayana_gatha.md | 154 | yaṁ [ya-] | [ya] | DPD lemma / construction | DPD |
| 04_tayana_gatha.md | 214 | yaṁ [ya-] | [ya] | DPD lemma / construction | DPD |
| 04_tayana_gatha.md | 229 | yaṁ [ya-] | [ya] | DPD lemma / construction | DPD |
| 04_tayana_gatha.md | 254 | taṁ [ta-] | [ta] | DPD lemma / construction | DPD |
| 05_samanera_sikkha.md | 294 | imehi [ima + ehi] | [ima] | DPD lemma / construction | DPD |
| 05_samanera_sikkha.md | 411 | imehi [ima + ehi] | [ima] | DPD lemma / construction | DPD |

