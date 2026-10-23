# Changelog: 05_anumodanas

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 09_maha_mangala_cakka_vala.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 36 | *bhagavato* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |


## 2026-10-05 — session S19c (cross-file index, from 07b_anagatabhaya_suttas)

Step-9 alignment after 07b was completed: each word now has the DPD analysis in every file.

### 13_ariya_dhana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 14 | tathāgate `(masc loc sg)`, no member rows | `(masc loc sg comp)` + ↳ *tathā*, ↳ *gate* | compound needs member rows (spec §4) | DPD tathāgata |

## 2026-10-05 — session S18b (step 9: index alignment for 07a)

Etymologies aligned across the checked subfolders (01–07a) to the DPD constructions used in 07a (S12–S18b), from the `index` report. Same lemma, same analysis in every file; homonyms, sandhi rows and bare-lemma variants were left.

### 01_yatha_vari_vaha_pura.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 17 | paripūrenti [pari + √pūr + e + nti] | [pari + √pūr > pūre + nti] | align with DPD construction | DPD paripūrenti |

## 2026-10-04 — session S9b (05_anumodanas 04–14; spot check 01–14)

Files 04–14 were in pre-spec form (`[cite: n]` tags on every line in 09 and 11, English heading in 13, citations analysed as Pāli lines, no ↳ member rows, invented, Sanskrit-style or folk etymologies, tokens such as `pers`, `conj`, `particle`, `abbrev`, BM's English echoed in the Faithful lines). Each was redrafted from BM 5.3–5.13 with DPD lookups (local DPD, release of 26 Sept 2026). Each row below summarises a kind of change made throughout the file; the previous text is kept in `orig` and the bhikkhu's backups. Lint: 0 ERROR, 0 STRAY, 0 WARN. Compare: all identical to BM after normalisation, except 08's written-out *Bhavatu sabba-maṅgalaṁ* block (BM abbreviates it). Spot check (10 units drawn from 01–14): 1 unit with an error (11, see below), 4 debatable points, 5 clean.

### All files 04–14
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | no English title (13: English `###` heading) | `*English title*` under the Pāli title | spec §1 | — |
| all | compound parts as ordinary rows, or members after the compound | whole-compound row then ↳ member rows | spec §4 | style-spec |
| all | tags `(… pers …)`, `(… pp)` after case, `(ind conj)`, `(ind emphatic particle)`, `(abbrev)`, `(citation)` | canonical tags | spec §4 | style-spec |
| all | *su + kha*, *√puññ*, *√vaṇṇ*, *√i + u* (āyu), *√si + ri*, *√ji + a*, *vīra + a*, *√sañj + tu* and similar | DPD constructions, or "no root in DPD" where DPD gives none | DPD | DPD |
| all | Faithful lines close to BM's English; American spelling (*honor*, *splendor*) | rewritten from the Pāli; British spelling | spec §3 | — |
| citations | *A.II.35; A.III.36*, *Khp.VII.v10-13*, *AN 5.36, A.III.41*, *Vin.II.147*, *A.II.32*, *A.III.46*, *A.III.54*, *Vin.I.229* (some analysed as Pāli lines) | *AN 4.34; AN 5.32*, *Kp 7*, *AN 5.36*, *Kd 16:1.5*, *AN 4.32*, *AN 5.41*, *AN 5.47*, *DN 16:1.31* | SuttaCentral IDs | SuttaCentral; 14: BM cites the Vinaya parallel (Kd 6), whose segment ID was not confirmed, so the DN parallel is given |
| sandhi forms | split into separate rows plus a combined row (coverage) | one `(sandhi)` row with both words' tags in the note (*katam-anussaraṁ*, *v'aññā*, *petāna'pūjā*, *hitāy'assa*, *cāpi*, *idh'eva* …) | coverage | spec §4 |

### 04_aggappasada_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| virāgūpasame, puññakkhette, aggappatto | members as rows; *khetter*; *√āp* | ↳ *virāg* / *ūpasame*, *puñña* / *kkhette*, *agga* / *ppatto*; √ap | coverage; DPD | DPD |
| dadataṁ, vijānataṁ | [√dā + a + ta], [√ñā + nā + ata] | [√dā > dadā + nta], [vi + √ñā > jānā + nta] | DPD | DPD |
| agga-dhamma-samāhito | "firm in the supreme Dhamma" | "endowed with the foremost Dhamma" (DPD samāhita 2) | DPD sense | DPD |

### 05_adasi_me_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| sakhā | (masc nom pl) | (masc nom sg) | DPD form | DPD |
| dakkhiṇaṁ | [√dakkh + iṇa] | [√dakkh + iṇā] (fem *dakkhiṇā*) | DPD | DPD |
| upakappati, rattaṁ | √klip; [ratti + a] missing | √kapp; [ratti + a, no root in DPD] | Sanskrit root; DPD | DPD |
| pasutaṁ | [pa + √su + ta] "produced" | [pa + √si > su + ta] "acquired, gained (lit. pursued)" | DPD (inference: DPD has no "produced" sense) | DPD pasuta |

### 06_kala_dana_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| vippasanna-manā tassa | Faithful "With a confident and pure mind, one's offering…" | "with minds made clear — the offering of such a one becomes abundant" | *tassa* rendered | grammar |
| onā, bhāgino, dade, patiṭṭhā | *ava + √nī*, *-in*, [√dā + a + e], sg/pl | [ūna > ona + a], [√bhaj > bhāg + ī], [√dā > dada + e], fem nom pl (with *honti*) | DPD; agreement | DPD |
| mahapphalaṁ, para-lokasmiṁ | no members | ↳ *maha* / *pphalaṁ*, *para* / *lokasmiṁ* | spec §4 | style-spec |

### 07_ratanattay_anubhav_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Sata-vassā ca āyu ca | second *ca* had no row (coverage) | row added | coverage | spec §4 |
| ratanattay'ānubhāvena | members *ratana*, *ttaya*, *ānubhāvena* | *ratanattay'* [ratana + taya], *ānubhāvena* | DPD | DPD |
| sattu, vuḍḍhī, lābhaṁ, yasavā | masc nom pl; fem nom sg; masc nom sg; adj | masc nom sg [singular in a list]; fem nom pl; masc acc sg [accusative form in a list of subjects]; adjective standing for renown | DPD forms | DPD |
| vassā, tejasā | nt; nt | masc (DPD *vassa*, *tejas*) | DPD gender | DPD |

### 08_culla_mangala_cakka_vala.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Bhavatu sabba-maṅgalaṁ… | abbreviated line analysed as a unit | the full block as chanted, rows from checked 05/01 (= 04a/26); repeat notes for its three *Sabba-…nubhāvena* lines | spec §2, §6 | 05/01 |
| Sabbe te … / Āyu-vaḍḍhako … | split mid-phrase | divided at phrase boundaries, no words moved | spec §2 | — |
| te (×6) | (2nd sg gen) only | `(2nd sg gen)` / `(dem pron masc nom pl)` with note: read traditionally as "your" | genuinely ambiguous | grammar |
| verse lines | own analyses | same rows as 07 (identical lines); *āyū* noted as metrical lengthening | consistency | 07 |

### 09_maha_mangala_cakka_vala.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | `[cite: n]` on every line (lint --fix removed them) | — | stray | spec §7 |
| tuyhaṁ sabba-roga-… | *dukka* | *dukkha* | misspelling | BM 5.8 |
| all *-ānubhāvena* compounds | members as separate rows (coverage) | ↳ member rows, *ānubhāvena* as last member | spec §4 | style-spec |
| …puññādhikarassa | [√puññ + a], [adhikara] | ↳ *puññ* [√puṇ + ya], *ādhikarassa* [adhi + √kar > kār + a] ("store, accumulation" — inference; DPD gives "aspiration, resolve") | DPD | DPD adhikāra |
| dīghāyukā | — | (fem nom sg) noted as standing for "long life" (inference) | grammar | — |

### 10_vihara_dana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| paṭihanti, paṭihaññati | 3rd pl; active | 3rd sg (DPD *paṭihanati*); 3rd sg pres pass indic | DPD | DPD |
| sariṁsape | — | note: BM's spelling of *sarīsapa* | — | DPD |
| leṇatthañ, sukhatthañ, annañ, pānañ, jhāyituñ | rows written *-aṁ* (coverage) | written forms, noted *-aṁ before ca* | coverage | spec §4 |
| parinibbātayanāsavo'ti | split into rows | one sandhi row, noting SuttaCentral's *parinibbāti anāsavo* (BM kept; query) | BM first | Kd 16:1.5 |

### 11_sangaha_vatthu_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | `[cite: n]` on every line | removed (lint --fix) | stray | spec §7 |
| rathass'āṇīva | rows split | one sandhi row [*rathassa* + *āṇī* + *iva*] | coverage | spec §4 |
| saṅgahā (line 11) | nom | (masc acc pl), noted as object of *samavekkhanti* | grammar | — |
| Yasmā ca … / samavekkhanti paṇḍitā | (draft) *paṇḍitā* rendered in the line before | each Faithful line renders its own words | spot-check finding | grammar |

### 12_adiya_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| uddhaggā | adj | compound with ↳ *uddh* / *aggā*; "uplifting" | spec §4; DPD | DPD uddhagga, uddhaggika |
| Idh'eva naṁ pasaṁsanti | Faithful passive | "him they praise right here in this life" (3rd pl kept) | number kept | grammar |

### 13_ariya_dhana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| ### Verses on the Riches of a Noble One | English heading | `*Verses on Noble Wealth*` title line | spec §1 | — |
| buddhāna | gen pl | note: *-ṁ* dropped for the metre | — | DPD |

### 14_devat_adissa_dakkhina_numodana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| ādise, āsuṁ, bhojetvā | [ā- + √dis + a + e]; [√as + uṁ]; caus. of √bhuj | (3rd sg act opt) [ā + √dis + a + e]; [a + √as + uṁ]; [√bhuj > bhoje + tvā] | DPD | DPD |
| va | `(ind particle/adv)` [ind] | `(ind)` [short for *iva*] [iva] | DPD va 1.1 | DPD |
| poso, bhadrāni, sadā | [√pus + a + o], [√bhadd + ra], [sabba + dā] | [purisa > porisa > posa], [√bhad + ra], [saṁ + dā] | DPD; aligned with checked files | DPD |

### Step 9 index alignment (05 rows aligned with checked files 01–04b)
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 05 pasutaṁ | [pa + √si > su + ta] "acquired" | row of 02/04, 06, 08: [pa + √su + ta; DPD pasūta] "produced, generated" | same phrase *puññaṁ pasutaṁ*, one analysis | DPD pasūta |
| 05 rattaṁ, tiṭṭhanti | [ratti + a, no root in DPD]; [√ṭhā > tiṭṭha + ti] | [ratti + a]; [√ṭhā > tiṭṭha + nti] | same word, one analysis | 01/01, 03/10 |
| 11 bhavanti | [√bhū + a + nti] | [√bhū > bhava + nti] | same word, one analysis | 04a/09b |
| 12, 14 naṁ | [ta > na + aṁ] | [ta] | same word, one analysis | 04a/10, 04b/01 |
| 13 āhu | [a + √ah + u] | [√ah + u] | same word, one analysis | 03/14, 04a |
| (04b/01 attano) | [atta, no root in DPD] | [atta + no], to match 05/10 | same word, one analysis | DPD; logged in 04b |

## 2026-10-04 — session S9a (05_anumodanas 01–03)

Files 01–03 were in pre-spec form and were redrafted from BM 5.1–5.2 with DPD lookups (local DPD, release of 26 Sept 2026). Each row below summarises a kind of change made throughout the file; the previous text is kept in the bhikkhu's backups. Lint: 0 ERROR, 0 STRAY, 0 WARN. Spot check deferred to S9b (session limit).

### 01_yatha_vari_vaha_pura.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | no ↳ member rows; tags `(… pres imperat act)` | ↳ member rows for every compound; tags in canonical order `(… pres act imperat)` | spec §4 | style-spec |
| petānaṁ | [pp. of para + √i + ta + ānaṁ] | [pa + √i > e + ta] | wrong prefix | DPD peta |
| citation | *Khp.VII.v8* | *Kp 7* | SuttaCentral ID | SuttaCentral |
| ito, paripūrenti, dinnaṁ, sukhī, āyu, cattāro, vaṇṇo, sāgaraṁ, maṇi, antarāyo, dīgh'āyuko | invented or bare etymologies (*sukha + in*, *√ay + u*, *catu*, *√var + ṇa*, *antar + √i + a*) | DPD constructions (*√sukh + ī*, *ā + √i > ay + u*, *catu + āro*, *√var + na*, *antara + aya*) | DPD | DPD |
| khippam-eva, evam-eva | emphatic *eva* partly lost in Faithful | "quickly indeed", "even so" | emphatic particle rendered | grammar |
| Faithful lines | *fulfillment*, *honoring*, *honors*; BM-like phrasing | British spelling; rewritten from the Pāli | spec §3 | — |
| Bhavatu … bhavantu te (×3) | repeated lines written out in full | repeat notes; first-occurrence rows aligned with checked 04a/26 | spec §6; consistency | 04a/26 |

### 02_sabba_roga_vinimutto.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | no English title | *Freed from All Illness* | spec §1 | — |
| all | member rows before the compound row; tokens `pers`, `conj`, `neg`, `num`, `adj` after case | whole-compound row then ↳ members; canonical tags | spec §4 | style-spec |
| Sabb'ītiyo, Mā te bhavatv-antarāyo | rows split into *sabbā*, *ītiyo*; *bhavatu* (coverage) | written forms *sabb'ītiyo*, *bhavatv-* | coverage | spec §4 |
| veram | [vīra + a] | [√vīr > ver + a]; marked accusative object of *atikkanto* | DPD | DPD vera |
| nibbuto | [ni- + √vā + ta] | [nī + √vā > vu > bu + ta] | DPD | DPD nibbuta |
| tuvam-bhava | split *tuvaṁ*, *bhava* (coverage) | one sandhi row | coverage | spec §4 |
| apacāyino | [apa- + √ci + āya + in] | [apa + √cāy + ī] | DPD root | DPD apacāyī |
| end | *Dhp 109* analysed as a Pāli line with Literal, Faithful and table | citation line only | stray | spec §5 |
| units 5–12 | own analyses | same rows as 01 (identical lines) | consistency | 01 |

### 03_bhojana_dananumodana.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| all | *-do* compounds without ↳ rows; tags `(comp/sandhi)`, `(ind absolutive)` | ↳ member rows; `(sandhi)`, `(abs)` | spec §4 | style-spec |
| paṭibhāṇa, paṭibhāna | [paṭi + √bhā + ana] | [paṭi + √bhaṇ > bhāṇ + a] | DPD root | DPD |
| vaṇṇa, āyu, sukhañ-ca, medhāvī, yasavā, dīgh'āyu | √vaṇṇ, √ay, *su + kha*, *medhā + in*, *yasa + vant*, √dīgh | √var, ā + √i > ay, √sukh, √medh + ā + vī, yasas + vant, dīgha (no root) | DPD | DPD |
| yatthūpapajjatī'ti | [yatha + upapajjati + iti] | [yattha + upa + √pad + ya + ti + iti] | misspelt member | DPD |
| so | `(masc nom sg)` | `(dem pron masc nom sg)` | consistency with 01–04b | — |
| citation | *A.III.42* | *AN 5.37* | SuttaCentral ID | SuttaCentral |

## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 05_adasi_me_adi_gatha.md | 8 etymologies | aligned: *atthāya*, *hi*, *hitāya*, *iti*, *sakhā*, *vā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 12_adiya_sutta_gatha.md | 6 etymologies | aligned: *atthaṁ*, *brahma*, *cārino*, *iti*, *kataṁ*, *paṇḍito* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 08_culla_mangala_cakka_vala.md | 7 etymologies | aligned: *bhavantu*, *dukkha*, *hotu*, *pi*, *sukha*, *sukhaṁ*, *vaṇṇo* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 04_aggappasada_sutta_gatha.md | 8 etymologies | aligned: *aggassa*, *aggaṁ*, *iti*, *sukhaṁ*, *vaṇṇo*, *vā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 06_kala_dana_sutta_gatha.md | 8 etymologies | aligned: *hoti*, *iti*, *kāle*, *pi*, *tasmā*, *tattha*, *vā*, *ye* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 14_devat_adissa_dakkhina_numodana_gatha.md | 10 etymologies | aligned: *cārino*, *devatā*, *mātā*, *orasaṁ*, *passati*, *puttaṁ*, *pūjitā*, *tā*, *yā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 01_yatha_vari_vaha_pura.md | 7 etymologies | aligned: *bhavantu*, *cattāro*, *niccaṁ*, *sukhaṁ*, *vaṇṇo* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_sabba_roga_vinimutto.md | 3 etymologies | aligned: *niccaṁ*, *sukhaṁ*, *vaṇṇo* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 03_bhojana_dananumodana.md | 3 etymologies | aligned: *hoti*, *sukhassa*, *sukhaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 13_ariya_dhana_gatha.md | 3 etymologies | aligned: *jīvitaṁ*, *saraṁ*, *sāsanaṁ* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 01_yatha_vari_vaha_pura.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 12 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 74 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 85 | yathā [relative adverb] | [ya + thā] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 02_sabba_roga_vinimutto.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 22 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 34 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 69 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 93 | dīgha [√dīgh] | [dīgha, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 04_aggappasada_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 77 | saṅghe [sam- + √han + a] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 87 | puñña [√puññ] | [√puṇ + ya] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_adasi_me_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 11 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 13 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 27 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 113 | kho [ind] | [kho] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 134 | dīgha [√dīgh] | [dīgha, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 135 | rattaṁ [√rā + ti] | [ratti + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 203 | pasutaṁ [pa- + √su + ta] | [pa + √su + ta] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 08_culla_mangala_cakka_vala.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 21 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 32 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 107 | antarāyā [antar + √i + a] | [antara + aya] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 180 | antarāyā [antar + √i + a] | [antara + aya] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 184 | tejasā [√tij + as + ā] | [√tij + as] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 255 | sabba [pronominal adj] | [sabba] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 12_adiya_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 24 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 103 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 135 | ariya [ariya] | [ariya, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 136 | dhamme [√dhar + ma + e] | [√dhar + ma] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 149 | eva [ind] | [eva] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 13_ariya_dhana_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 45 | ariya [√ar + iya] | [ariya, no root in DPD] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 57 | saṅghe [saṁ- + √han + a + e] | [saṁ + √ghaṭ + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 69 | uju [uju] | [√uj + u] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 04_aggappasada_sutta_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 111 | puññaṁ [√puññ] | [√puṇ + ya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 05_adasi_me_adi_gatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 137 | hitāya [√hi + ta + āya] | [√dhā + ita] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 202 | puññaṁ [√puññ] | [√puṇ + ya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01_yatha_vari_vaha_pura.md | 61 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |
| 01_yatha_vari_vaha_pura.md | 116 | mā [prohibitive particle] | [mā] | DPD lemma / construction | DPD |
| 02_sabba_roga_vinimutto.md | 47 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 02_sabba_roga_vinimutto.md | 80 | mā [ind] | [mā] | DPD lemma / construction | DPD |
| 03_bhojana_dananumodana.md | 29 | so [ta pronoun base] | [ta] | DPD lemma / construction | DPD |
| 04_aggappasada_sutta_gatha.md | 11 | ve [ind] | [ve] | DPD lemma / construction | DPD |
| 04_aggappasada_sutta_gatha.md | 123 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 26 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 59 | na [ind] | [na] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 86 | na [ind] | [na] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 99 | evaṁ [ind] | [eva + aṁ] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 111 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 162 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 176 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 05_adasi_me_adi_gatha.md | 188 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 06_kala_dana_sutta_gatha.md | 53 | tassa [ta pronoun base] | [ta] | DPD lemma / construction | DPD |
| 06_kala_dana_sutta_gatha.md | 95 | na [ind] | [na] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 103 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 118 | sabbe [sabba + e] | [sabba] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 169 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 183 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 220 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 222 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 225 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 238 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 08_culla_mangala_cakka_vala.md | 240 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 12_adiya_sutta_gatha.md | 148 | idha [idha] | [ima + dha] | DPD lemma / construction | DPD |
| 12_adiya_sutta_gatha.md | 163 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 12 | yassa [ya + ssa] | [ya] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 13 | saddhā [saṁ- + √dhā + ā] | [sad + √dhā + ā] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 34 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 35 | yassa [ya + ssa] | [ya] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 59 | yassa [ya + ssa] | [ya] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 72 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 84 | taṁ [ta + aṁ] | [ta] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 95 | tassa [ta + ssa] | [ta] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 107 | ca [ind] | [ca] | DPD lemma / construction | DPD |
| 13_ariya_dhana_gatha.md | 109 | ca [ind] | [ca] | DPD lemma / construction | DPD |

