# Changelog: 06_funeral_chants

## 2026-10-11 — session S22 (final: whole-tree index alignment)

Whole-tree `index` (01–08): etymologies aligned to DPD constructions (*bhagavant*, future stems, *appamāda*, *bahiddhā*, *cetas*), and Triple Gem quality adjectives tagged `adj` as DPD classes them. Draft sources in `_tools/drafts/` changed to match.

### 01_dhamma_sangani_matika.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 372, 376 | *bahiddhā* √bah + i + dhā + a | √bah + i + dhā | DPD construction (indeclinable) | DPD bahiddhā 1 |

### 10_pamsukula.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 72 | *marissare* √mar + issa +  | √mar + a + issa > marissa +  | DPD future-stem construction (present stem mara) | DPD marati |


## 2026-10-11 — session S21 step 9 (cross-file index, from 08_patimokkha_chants)

### 08_patthana_matika_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 54 | ↳ pacchā [pacchā] | [paccha + ā] | DPD construction | DPD pacchā 1 |

## 2026-10-05 — session S18b (step 9: index alignment for 07a)

Etymologies aligned across the checked subfolders (01–07a) to the DPD constructions used in 07a (S12–S18b), from the `index` report. Same lemma, same analysis in every file; homonyms, sandhi rows and bare-lemma variants were left.

### 09_vipassana_bhumi_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 644 | virāga [vi + √raj > rāg + a] | [vi + √raj > rag > rāg + a] | align with DPD construction | DPD virāga |

## 2026-10-04 — session S11 (06_funeral_chants 09–10, step 9)

Files 09 and 10 were in pre-spec form (`---` separator lines; English `###` headings in 10; no `*English title*`; no ↳ member rows; BM-style citation in 09, none in 10; 09's dependent-origination passage as two single units, with one table row standing for nine compounds (`saṅkhāra-nirodhā ... jāti-nirodhā`, "Refer to preceding noun breakdowns"); invented or Sanskrit-style roots). Both were redrafted from BM 6.9–6.10; both are exact against BM (similarity 1.000 on BM's passage). Lint: safe fixes applied.

### 09_vipassana_bhumi_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | `#` only | + *The Recitation of the Grounds of Insight* | spec §1 | — |
| headings | `### Pañcakkhandhā`, `### Dvādasāyatanāni`, `### Aṭṭhārasa Dhātuyo`, `### Bāvīsat'indriyāni`, `### Cattāri Ariyasaccāni`, `### Paṭiccasamuppāda` | removed | not in BM; they repeated the chanted label lines | BM 6.9 |
| line division | dependent origination in 2 units (arising, cessation) | 12 + 12 units, at BM's capitalised line starts | spec §2 | BM |
| compounds | no member rows; *-paccayā* tagged with the gender of the first member (`fem abl sg cmpd`) | whole row + ↳ members; *-paccayā* `(masc abl sg comp)` (*paccaya* is masc) | spec §4; grammar | DPD paccaya |
| etymologies | *√vid + anā + khandha*, *√ghā + ana + vi-√ñā*, *upa-√ikkhi*, *vīra + ya*, *dvādasana*, *an-āññāta*, *āññātāvin*, *√sadd*, *√gandh*, *upa-ā-√dā*, *√bhū + a* and others | DPD constructions (*√gandh* → *√ghā + na*; *viriya* √vīr + iya; *upādāna* upa + √ādā + ana; *aññātāvī* ā + √ñā + tāvī; *jivhā, itthi, purisa, kevala, nāma*: no root in DPD) | DPD | DPD |
| tags | `(num card nom pl)`, `(3rd pers pl pres act)`, `(ind ptcl cmpd)`, `(elided repetitive ablative compounds)` | canonical tags; *aṭṭhārasa* `(card fem nom pl)`; *avijjāya* `(fem gen sg)` | spec §4 | — |
| *tv-eva*, *evam-etassa* | `(ind ptcl cmpd)`, `(ind + masc/nt gen sg dem pron)` | `(sandhi)` rows with both words' tags | spec §4, Known risks | — |
| Faithful lines | close to BM's English; American spelling (*odor*, *vigor*, *aging*) | rewritten from the Pāli; British spelling; *gandha* "smell"; *bhava* "becoming"; *saṅkhārā* "volitional formations" as in 06/03 | spec §3 | — |
| *sukh'-*, *dukkh'indriyaṁ* Literal | *Bodily-pleasure-faculty bodily-pain-faculty* | *[bodily-]pleasure-faculty [bodily-]pain-faculty* (Faithful keeps "bodily", the Abhidhamma sense) | spot check | DPD sukhindriya |
| citation | *M.III.15f; M.III.280f; M.III.62; M.III.249f; S.II.1f* | *MN 109; MN 148; MN 115; MN 141; SN 12.1* | spec §5 | SC (PTS page mapping; lists checked in the SC texts) |

### 10_pamsukula.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| title | `#` only | + *Verses for the Rag-Robe Offering* | spec §1 | — |
| headings | `### Verses on Mortality`, `### Reflection on Uncertainty`, `### Reflection on the Body` | removed | English headings are stray (spec §7) | — |
| rows | written fresh | rows shared with 03/15 (*Aniccā vata*, *Addhuvaṁ jīvitaṁ*, Dhp 41 words) copied from there | consistency | 03_reflections/15 |
| *Tath'evāhaṁ* | split into *Tath'eva* + *āhaṁ* (coverage error) | one `(sandhi)` row: *tathā + eva + ahaṁ* | coverage | spec §4 |
| *maranti*, *mariṁsu*, *marissare*, *marissāmi* | `(pres act 3p pl)` etc. | `(3rd pl pres act indic)`, `(3rd pl aor act indic)`, `(3rd pl fut mid indic)`, `(1st sg fut act indic)` | spec §4 | DPD marati |
| *chuḍḍho* | [√chuḍḍh + -ta] | [√chaḍḍ > chuḍḍ + ta] | DPD | DPD chuḍḍha |
| *maritabbaṁ* | `(fut pass part …)` [√mar + itabba] | `(ptp nt nom sg)` [√mar > mara + itabba]; Faithful "I must inevitably die" | spot check | DPD maritabba |
| *Addhuvaṁ jīvitaṁ* Faithful | Life is impermanent | Life is not lasting (keeps *addhuva* distinct from *aniyata* "uncertain") | spot check | DPD addhuva |
| *Maraṇapariyosānaṁ me jīvitaṁ* Faithful | My life bounder end in death | my life ends in death | garbled | — |
| citations | none | *DN 16:6.10.10–13; SN 1.11:5.3–6*, *DhpA.III.170*, *Dhp 41* | spec §5 | BM; SC |
| rubrics | — | *(For the dead)* before *Aniccā vata …*; *(For the living)* before *Aciraṁ vat'ayaṁ kāyo*; added to spec §7; no `(×3)` (BM: "often" repeated) | query 46, bhikkhu 2026-10-04 | BM 6.10 |

### Step 9 (index alignment, 06 against 01–05)
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 01 l.35 | *adukkham* [na > a + dukkha; √dukkh + a] | [na > a + √dukkh + a] | index | DPD adukkha |
| 03 l.66 | *ajjhattaṁ* [adhi > ajjh + atta] | [adhi > adhy > ajjh + atta] | index | DPD ajjhatta |
| 05 l.98 | ↳ *bhū* [√bhū] | [√bhū + ū] | index | DPD bhū |
| — | *samaye* [saṁ + √i > ay + a] kept (DPD form); 04a/20 aligned to it | — | index | DPD samaya |
| — | left: *mahā* [√mah + a] (DPD maha) vs [√mah + nta + ā] elsewhere (DPD mahant), both DPD; *bahiddhā* adj vs ind; *paritta* (limited) vs *paritta* (protection), different lemmas | — | homonyms | DPD |

## 2026-10-04 — session S10 (06_funeral_chants 01–08)

Files 01–08 were in pre-spec form (no English titles; 01 split each mātikā phrase into its own unit, 66 units; 08 had a `### Tika Paṭṭhāna` heading taken from BM's citation; BM's citations analysed as Pāli lines with Literal and Faithful lines; member rows given before the compound, or none; tags such as `masc nom pl adj`, `ind part`, `comp/sandhi`, `masc/nt`; invented or Sanskrit-style etymologies such as *mātrā*, *√kus + ala*, *√kiles*, *du + √kha*). All eight were redrafted from BM 6.1–6.8 with DPD lookups (local DPD, release of 26 Sept 2026). `lint --fix` safe fixes were applied first. All eight files are now identical to BM after normalisation.

### All files 01–08
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| titles | `#` title only | `#` Pāli title from BM + `*English title*` (*The Matrix of the Enumeration of Phenomena*, *The Enumeration of Phenomena*, *The Analysis*, *The Discussion of Elements*, *The Designation of Persons*, *The Points of Controversy*, *The Pairs*, *The Recitation of the Matrix of Conditional Relations*) | spec §1 | — |
| citations | *Dhammasaṅganī 1f* (none in 01), *Dhammasaṅganī 56*, *Vibhaṅga 1*, *Dhātukathā 1* (missing in 04), *Puggalapaññatti 1*, *Kathāvatthu 1*, *Yamaka 1*, *Tika Paṭṭhāna 1* (as heading) — mostly analysed as Pāli units | *Ds 1.1*, *Ds 2.1.1*, *Vb 1*, *Dt 1.1*, *Pp 1.1*, *Kv 1.1*, *Ya 1.1.1*, *Patthana 1.1* | spec §5 | SuttaCentral bilara-data (root/pli/ms/abhidhamma) |
| line division | 01: one unit per phrase (66); 04, 05, 08: one unit per pair | 01: one unit per triad, as BM prints it (22); 02, 03: long sentences divided at phrase boundaries; 04, 05, 08: BM's lines or groups of four to six items | spec §2 | BM |
| compounds | parts as rows, members before the whole row, or no members | whole-compound row, then ↳ member rows | spec §4 | style-spec |
| etymologies | *√kus + ala*, *a- + kusala*, *mātrā*, *√kiles*, *du + √kha*, *√dā* (upādinna), *√sukh* as adj without DPD form, and others | DPD constructions; *kusala, sukhuma, puggala, indriya*: "no root in DPD" | DPD | DPD |
| Faithful lines | close to BM's English (*conjoined*, *clung-to clingable*) or adding sense; American spelling (*practicing*) | rewritten from the Pāli; British spelling | spec §3 | — |
| *dhammā* | "phenomena, mental states, qualities" | "phenomena, things" (as in 01–05) | consistency | checked files |

### Particular decisions
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | *N'eva vipāka na …* | *vipāka* `(masc comp)` without note | note: stem form, one compound (*nevavipākanavipākadhammadhammā*) in the canon; lint WARN left | grammar | SC Ds 1.1 |
| 01 | *n'ev'ācaya-gāmino*, *nāpacaya-gāmino* | split rows | one `(sandhi)` row each, both words' tags in the note | coverage | spec §4 |
| 01 | *maggādhipatino* | — | `(masc nom pl comp)`, note on the *-ino* ending | grammar | DPD adhipati 2 |
| 02 | *phasso hoti, avikkhepo hoti* | — | kept; row note: the chant passes from the first to the last item of the canonical list; Faithful marks it with … | abridgement | SC Ds 2.1.1:1.2–13.2 |
| 02 | *atthi* with plural subject | — | `(3rd sg pres act indic)` with note | grammar | DPD atthi 1.2 |
| 03 | *abhisaññūhitvā* | — | [abhi + saṁ + √ūh + itvā; form not in DPD] | DPD lacks the form | — (unverified against DPD) |
| 03 | *dūre*, *santike* | various | `(nt loc sg)`, as in checked files | consistency | 03_reflections |
| 04 | final *asaṅgahitaṁ* | analysed as a lone item | row note: the chant closes with the last word of the list (*vippayuttena saṅgahitaṁ asaṅgahitaṁ*); Faithful marks it with … | abridgement | SC Dt 1.1:15.1 |
| 05 | *Kittāvatā puggalānaṁ puggalapaññatti* | "To what extent is there a designation of persons among individuals?" | "To what extent is there, for persons, the designation of persons?" | spot check | grammar |
| 05 | *phaleṭhito* | — | case-keeping compound: ↳ *phale* `(nt loc sg)`, ↳ *ṭhito* | grammar | DPD decon |
| 06 | *vattabbe* | — | `(ptp nt nom sg)`, eastern nominative in *-e* (DPD form list omits it) | grammar | DPD vattabba |
| 06 | *micchā* (last line) | "is wrong" after the quotation | row note and … mark the chant's abridgement of the rebuttal (*yaṁ tattha vadesi … micchā*) | abridgement | SC Kv 1.1:2.4–2.7 |
| 06 | *re* | "oh" | `(ind)`, sharp form of address | DPD re | DPD |
| 07 | all four lines | statements ("all those have wholesome roots") | rendered as the Yamaka's questions; *kusalamūlā* = "wholesome roots" (the roots themselves), not "having wholesome roots" | meaning | SC Ya 1.1.1:2.1–5.1; DPD kusalamūla |
| 08 | `### Tika Paṭṭhāna` | heading | removed (it was BM's citation) | spec §1, §5 | BM |

## 2026-10-04 — session S4 (cross-file index, from 03_reflections 12–21)

Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in their own session. Homonym-prone forms (*te, no, vo, santo, santi, sataṁ, sati, sa, sace, pāṇino*) were left unchanged.

| File | Count | Words | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 09_vipassana_bhumi_patha.md | 4 etymologies | aligned: *hoti*, *nirujjhanti*, *saṅkhārā*, *vedanā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 10_pamsukula.md | 26 etymologies | aligned: *aciraṁ*, *addhuvaṁ*, *adhisessati*, *aniccā*, *aniyataṁ*, *apeta-viññāṇo*, *avassaṁ*, *dhuvaṁ*, *jīvitaṁ*, *kaliṅgaraṁ*, *kāyo*, *maraṇaṁ*, *maritabbaṁ*, *niratthaṁ*, *nirujjhanti*, *niyataṁ*, *paṭhaviṁ*, *sattā*, *saṅkhārā*, *sukho*, *uppajjitvā*, *uppāda-vaya-dhammino*, *vūpasamo* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 02_dhammasangani.md | 7 etymologies | aligned: *cittaṁ*, *hoti*, *katame*, *pi*, *somanassa* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 01_dhamma_sangani_matika.md | 7 etymologies | aligned: *anāgatā*, *bhāvanāya*, *sukha*, *upekkhā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |
| 06_kathavatthu.md | 1 etymologies | aligned: *micchā* | same word, one analysis | DPD-checked analyses in 03_reflections 12–21 |

## 2026-10-04 — session S2 (cross-file index, from 02_evening_chanting)

Etymologies of words also analysed in 02_evening_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session. Homographs (*va*, *vā*, *no*, *arahaṁ*) were left.


### 01_dhamma_sangani_matika.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 531 | magga [√mag + a] | [√magg + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 543 | magga [√mag + a] | [√magg + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 555 | magga [√mag + a] | [√magg + a] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 05_puggalapannatti.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 133 | paṭipanno [paṭi + √pad + na] | [pati + √pad + na] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

### 10_pamsukula.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 89 | āhaṁ [ahaṁ, with sandhi lengthening] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 102 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 155 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 168 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |
| 181 | me [amha] | [ahaṁ] | align with DPD-checked analysis | DPD (see 02_evening_chanting/CHANGELOG.md) |

## 2026-10-01 — session S1 (cross-file index, from 01_morning_chanting)

Etymologies of words also analysed in 01_morning_chanting were aligned with the DPD-checked analyses made there (step 9, `index`). Only the bracketed etymology changed; tags and meanings in these files are still unchecked and will be reviewed in this subfolder's own session.


### 01_dhamma_sangani_matika.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 40 | sukhāya [su + √kha] | [√sukh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 04_dhatukatha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 70 | sampayogo [saṁ- + pa- + √yuj + -a] | [saṁ + pa + √yuj + e + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 71 | vippayogo [vi- + pa- + √yuj + -a] | [vi + pa + √yuj + e + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 09_vipassana_bhumi_patha.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 342 | cattāri [catu] | [catu + āri] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 354 | dukkhaṁ [du- + kha] | [√dukkh + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 406 | saṅkhārā [saṁ-√kar + a] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 408 | viññāṇaṁ [vi-√ñā + ana] | [vi + √ñā + aṇa] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 440 | kevalassa [kevala] | [kevala + assa] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### 10_pamsukula.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10 | aniccā [a- + nitya > nicca] | [na + ni + tya] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |
| 12 | saṅkhārā [saṁ- + √kar + -a] | [saṁ + √kar + a] | align with DPD-checked analysis | DPD (see 01_morning_chanting/CHANGELOG.md) |

### Pronouns and indeclinables (all files in this subfolder)
| File | Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 06_kathavatthu.md | 57 | evaṁ [evaṁ] | [eva + aṁ] | DPD lemma / construction | DPD |
| 10_pamsukula.md | 142 | mayā [amha] | [ahaṁ] | DPD lemma / construction | DPD |

