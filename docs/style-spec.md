# Style Specification

This is the rulebook for every text in `books/` (the `NN_name.md` files in each book's `texts/` folder, or in its part folders). When a file breaks a rule here, the file is corrected, not the rule. If a rule seems wrong for a particular text, keep the file as it is, note the case, and ask the maintainer. The maintainer's dated decisions, and where they were made, are listed in `docs/decisions.md`.

Sections 1–11 apply to every book. Section 12 gives the rules that differ for the Vinaya formulae (09a–09e) and for the *Mahāsatipaṭṭhānasutta* (10).

**Machine-readable blocks.** `scripts/lint.py` (through `scripts/chantlib/spec.py`) reads four fenced blocks from this file: `tags` (§5), `repeat-note` (§8), `rubrics` and `english-stopwords` (§9). Edit those lists only here, so that the rules and the checks never drift apart. Keep each block's info string as it is, one entry per line. Per-book switches (the DN 22 behaviour in §12.2) are not in this file: they are the `options` in each book's `books/<book>/metadata.txt`.

## 1. File layout

Every text file has exactly this shape. Nothing else may appear in the file.

```text
# Pāli title of the chant

*English title*

### Optional Pāli section heading

**Pāli line exactly as chanted**

**Literal:** literal English in Pāli word order  
**Faithful:** natural English rendering  

| Word | Analysis & Meaning |
| :--- | :--- |
| **`pāli_word`** | `(tags)` meaning, meaning; **[etymology]** |

*SuttaCentral ID*
```

- The `#` title is in Pāli with diacritics. The `*English title*` line comes straight after it. The book's table of contents is built from the `#` titles.
- Exception: where the *Bhikkhu Manual* (BM) gives a chant only an English name and the maintainer has chosen to keep it, the `#` title is that English name and there is no `*English title*` line: 04a/01 *Invitation for Paritta Chanting*, 04a/02 *Invitation to the Devas*, 04b/10 *Verses on Respect* (2026-10-04, queries 24 and 36).
- `###` section headings are allowed only in Pāli (e.g. *Paṭhamo vāro*). An English heading is stray text. (Book 10 also allows a number and an English gloss, §12.2.)
- The **Literal:** and **Faithful:** lines each end with two spaces, so that they print on separate lines.
- The citation line goes directly under the last unit of the passage it covers.
- No `---` separator lines between units. `lint.py --fix` removes them (2026-10-01).
- File names are `NN_name.md`, numbered in book order. They live in `books/<book>/texts/`, or, for a book in parts (09), in `books/<book>/NN_<part>/`. Each text folder also has a `CHANGELOG.md` (§11), which is never built into a book. The untouched source texts (`00_original_*`) live in `sources/originals/`, never in `books/`.
- A text is cited by its legacy short ID, *folder/file number*: 07a/04 is `books/07a_suttas/texts/04_*.md`. For the Vinaya book, 09a–09e are its parts 01–05: 09c/06 is `books/09_vinaya_formulae/03_vinaya_notes_other_procedures/06_*.md`. The changelogs use these IDs, so they are kept for new entries too.

A *unit* is one Pāli line with its Literal and Faithful lines and its word table (or repeat note, §8).

## 2. The Pāli line

| Rule | Detail |
| :--- | :--- |
| Source | The *Bhikkhu Manual* text, with BM's spelling, sandhi and hyphenation. If the chant is not in BM, use the *Community Chanting Book* (Amaravati); if it is not there either, Ṭhānissaro Bhikkhu's *Chanting Guide* (2026-10-23). If it is in none of these, use SuttaCentral's Mahāsaṅgīti text, from the Simsapa app (`GET /sutta.json?uid=<code>/pli/ms`; 2026-10-26, replacing `sources/reference-pali-supplement.md`). Book 10 uses SuttaCentral only (§12.2); the Vinaya formulae use BM only (§12.1). Sources and their locations: `sources/UPSTREAM.txt`. |
| Niggahīta | Always **ṁ** (U+1E41). Never ṃ, ŋ or m with a combining dot. |
| Apostrophe | ASCII `'` for elision (*sabb'ītiyo*). The build turns it into a typographic apostrophe. |
| Leader brackets | Removed. BM's *[Yo so] bhagavā* becomes *Yo so bhagavā*. The words stay; only the brackets go. |
| Leader lines | BM's *Handa mayaṁ … bhaṇāmase* leader lines are included as the first unit of their chant, with a full table, and are not marked as the leader's (2026-10-01). *bhaṇāmase* is one word, also where BM spaces it *bhaṇāma se* (2026-10-04). |
| Repetition | `(×3)` at the end of the line, with the multiplication sign ×. No other form (x3, 3 times, three times). |
| Alternatives | Kept as BM prints them, with a slash: *te/me*, *dāso/dāsī*, *vandanto/vandantī*. (The Vinaya formulae turn them into variants, §12.1.) |
| Line division | Follow BM's line and verse division. Long prose may be divided at natural phrase boundaries, without dropping or reordering any words. |
| `…pe…` elisions | Where a source abbreviates with *pe*, the file gives the passage in full, as it is chanted. |
| Misprints | A plain misprint in the source is corrected, with the source's reading logged in the changelog (e.g. BM *Pathamaṁ*, *appativattiyaṁ* → *Paṭhamaṁ*, *appaṭivattiyaṁ*, 07a/01, query 48). A doubtful case keeps the source's reading and is put to the maintainer. A word the source omitted by mistake may be restored on the maintainer's decision (07a *upāyupādānā*, query 51). |
| Nothing else | No English, digits, square brackets or other parentheses in the Pāli line. |

## 3. Literal and Faithful lines

**Literal:** keeps the Pāli word order and represents every Pāli word in the line. Words that English needs but the Pāli does not have go in square brackets: *water-carrying full [rivers]*.

**Faithful:** a clear, accurate, natural English rendering in the register of Theravāda monastic usage.

- The Faithful line must not add meaning the Pāli does not have, and must not leave any out.
- Verb mood must be rendered: an imperative or optative is a wish or command (*may…*, *let…*, *should…*), not a statement.
- **Read as a wish.** Some forms that are not imperative or optative are used as wishes in chants. In each case the row keeps the form's true tag and adds a note, and the Faithful line says *may…* (2026-10-04):
  - a present indicative or aorist form used as a wish (*homi*, *pariharāmi*, *nivedayuṁ*) is decided case by case; where it is read as a wish, the note is `[present tense, used here as an aspiration]` or `[aorist form, used here as a wish]` (query 13);
  - a blessing line with no finite verb, whose participles or adjectives describe the person blessed (*So attha-laddho sukhito / viruḷho buddha-sāsane*), gets the note `[participle, read here as a wish]` (query 27);
  - a blessing line whose only verb is an absolutive with no main verb (04b/09 *Hantvā tesaṁ upaddave*) keeps `(abs)` with the note `[absolutive with no main verb, read here as a wish]` (query 35).
- **Never copy published English.** The Faithful line is checked against the Pāli and DPD, **not** against the English of BM, Ṭhānissaro or any other published translation, and does not reproduce their phrasing. (BM's licence is CC BY-NC-ND; this is a precaution, not legal advice.) The one exception is the Vinaya formulae, whose Faithful line is BM's English by decision (§12.1).
- Spelling is British (*honour*, *fulfilment*, *practise* as a verb).
- Keep key terms the same across all files: **Buddha, Dhamma, Saṅgha** capitalised when they mean the Triple Gem; *dhammas* / *qualities* lower case otherwise; *Nibbāna*, *Tathāgata*, *bhikkhus*, *devas* left in Pāli. When a term is rendered differently in two files, choose one rendering and log the change.
- A line that continues a sentence from the line before may begin in lower case, or may repeat the sense of the whole sentence. Either is fine, but stay consistent within a text.
- Where a word has a commentarial reading that differs from DPD's, the Faithful line follows DPD and the row note may give the commentarial reading (08/05, query 59).

## 4. The word table

| Rule | Detail |
| :--- | :--- |
| Header | Exactly `| Word | Analysis & Meaning |` then `| :--- | :--- |`. |
| Row format | `| **`word`** | `(tags)` meaning; **[etymology]** |`. Bold and backticks around the word; backticks and parentheses around the tags; a semicolon before the bold, square-bracketed etymology. |
| Order | One row per word, in the order the words appear in the Pāli line. |
| Coverage | The row words, read in order, must spell out the whole Pāli line. Member rows (↳, below) are not counted. A compound written with hyphens is one row (`sabba-rogo`). A word split by sandhi gets a row for each written part, with the joining mark kept (`bhavatv-` and `antarāyo`); an apostrophe form is one row (`sabb'ītiyo`). A hyphenated sandhi form (*dutiyam-pi*, *me-v-atthi*) is one `(sandhi)` row. Lint enforces coverage. |
| Case of the word | Lower case, even where the Pāli line has a capital. |
| Meaning | The sense in this line first, then other senses if useful. Several senses separated by commas. |
| Compounds | See below. |
| Notes | When the tag needs explaining (a sandhi form, an unusual ending, agreement), put a short note in square brackets before the meaning: `` `(3rd sg pres act imperat)` [sandhi of *bhavatu* before *a-*] may there be ``; `[agrees with *pattaṁ*]`. Notes give DPD's meaning, grammar or construction. |

**Compounds** (2026-10-01, for novice students). Every compound (two or more independent words joined, hyphenated or not: *sāvakasaṅgho*, *saṁvega-parikittana-pāṭhañca*) gets:

1. one row for the whole compound, tagged with `comp`, with its overall meaning, and the members as its etymology (`[sāvaka + saṅgha]`);
2. then one member row per part, each starting `| ↳ **`member`** |`. Earlier members take their stem form and a compound-member tag (`(masc comp)`, `(adj comp)`, `(ind comp)`; `(prefix)` for *sa-*). The last member takes the form in the line and the whole compound's tags without `comp`. Each member row gives its own root.

Not compounds:

- words with an ordinary prefix only (*supaṭipanno*, *abhipūjayāmi*);
- words with the preverb *antara-* (*antaradhāna*, *antaradhāyati*, *antaradhāpeti*, *anantaradhāna*), although DPD labels them "comp". They are single rows with the construction `[antara + dhāna]` etc. (2026-10-05, query 57).

The members of a compound are those DPD gives (its `construction`, or the Simsapa deconstructor split for forms DPD has no headword for); they are never split by rules of our own. A member that is itself a compound (*mahāpathe* in *catumahāpathe*) has, so far, no sub-member rows; this was left open (query D16). Lint warns when a `comp` row has no member rows.

**Reuse settled rows.** A word that already has a settled row elsewhere is analysed the same way unless its grammar in this line differs: look it up with `scripts/index.py rows <word>`. A Pāli line identical to a settled line in another file is copied, not re-analysed (`scripts/index.py overlaps`).

## 5. Tags

Allowed tokens (lint accepts nothing else). Combine them with spaces. Use `/` between alternatives within a group (`dat/gen`), and ` / ` between alternative whole groups: `` `(fem nom pl)` / `(ind)` ``.

```tags
masc
fem
nt
nom
acc
instr
dat
abl
gen
loc
voc
sg
pl
1st
2nd
3rd
pres
aor
fut
perf
cond
act
mid
pass
indic
imperat
opt
caus
denom
pp
prp
ptp
abs
inf
ind
adv
adj
pron
rel
dem
interr
card
ord
prefix
sandhi
interj
comp
```

Canonical order and examples:

| Word class | Order | Example |
| :--- | :--- | :--- |
| Noun, adjective | gender case number | `(masc nom pl)`, `(adj fem acc sg)` |
| Participle | participle-type gender case number | `(pp nt nom sg)`, `(prp masc nom sg)`, `(ptp masc nom sg)` |
| Finite verb | person number tense voice mood | `(3rd pl pres act indic)`, `(3rd sg pres act imperat)`, `(1st sg act opt)`, `(3rd sg aor act indic)` |
| Causative / passive verb | as above, with `caus` or `pass` before the voice | `(3rd sg pres caus act indic)`, `(3rd sg pres pass indic)` |
| Personal pronoun | person number case | `(2nd sg dat)`, `(1st pl gen)` |
| Other pronoun | pron-type gender case number | `(rel pron masc nom sg)`, `(dem pron nt acc sg)` |
| Numeral | card/ord gender case number | `(card masc nom pl)` |
| Indeclinable | single token | `(ind)`, `(adv)`, `(abs)`, `(inf)`, `(interj)` |
| Compound member (stem form, no ending) | gender or class, then `comp` | `(masc comp)`, `(adj comp)` |
| Whole compound, inflected | as for its word class, then `comp` | `(masc nom sg comp)` |

- `comp` means "compound" (2026-10-01). It replaces the earlier `cmpd`, `compound`, `in cmpd` and `in compound`.
- Never use `masc/fem/nt`, `TBD`, or a tag left blank.
- A word that is genuinely ambiguous in its line gets both readings: `(dat/gen)`.
- Adjectives that DPD classes as adjectives are tagged `adj`, including the qualities of the Triple Gem (*anuttaro*, *svākkhāto*: `(adj masc nom sg)`; session S22).
- *bhante* addressing the Saṅgha or several people is `(masc voc pl)`; addressing one person, `(masc voc sg)`.

**Auto-fixed synonyms.** `lint.py --fix` maps these, because each has only one meaning: `cmpd`, `compound`, `in cmpd`, `in compound` → `comp`; `inst`, `ins` → `instr`; `ppp` → `pp`; `ppr` → `prp`; `indcl` → `ind`. Other non-canonical tokens (`part`, `particle`, `ptcl`, `conj`, `neg`, `imp`, `pers`, `num`, `in`) are ambiguous or need the word class decided, so they are fixed by hand.

**Who assigns tags.** Scripts never assign grammar labels. `scripts/simsapa.py check` compares a row's labels with DPD's parses of the form and lists a mismatch for review, but never writes one. Scripts fetch DPD data through Simsapa, and the labels are chosen for the word as it stands in the line, following the `pali-word-analysis` skill (`.claude/skills/pali-word-analysis/SKILL.md`).

## 6. Etymology

- Inside bold square brackets: `**[pa + √i + ta]**`.
- Roots are **Pāli** roots in DPD's form, with the sign √ (U+221A): `√i`, `√bhū`, `√hū`, `√ñā`, `√kar`. Never Sanskrit forms (no `√śvas`, `√kṛ`); the letters ś ṣ ṛ ṝ ḹ never appear. Never LaTeX (`\sqrt{}`).
- Show the construction as DPD gives it: prefix + root + suffix + ending, e.g. `**[pp of peti, pa + √i + ta]**`, `**[√bhaj > bhag + a + vant]**`. For compounds: the members, `**[sabba + roga]**`, with roots for the members where useful.
- A DPD `construction` may give several analyses (one per line); the row follows one of them. Some rows use a shortened form of DPD's chain (*pajānāti* `[pa + √ñā > jānā + ti]`, DPD's asterisks dropped); whether to keep these or always give DPD's full chain was left open (query D17).
- Indeclinables, pronouns, cardinals and prefixes, for which DPD gives no root, may give the bare lemma (`**[ca]**`, `**[ta]**`, `**[ima]**`). Lint does not warn about these when the tags mark them as `ind`, `adv`, `interj`, `pron`, `dem`, `rel`, `interr`, `card`, `prefix` or a personal pronoun.
- A noun or adjective that DPD gives without a root is written `**[karuṇā, no root in DPD]**`. Other nouns and adjectives need a root or construction.
- **DPD is the authority**, consulted through the Simsapa app's localhost API (`scripts/simsapa.py`; `docs/simsapa-localhost-api-search-endpoints.md`). When a root or construction differs from DPD, DPD wins and the change is logged with "DPD" as the reference.
- A traditional (commentarial or folk) explanation that is not a historical derivation is marked `(trad.)`, after DPD's analysis if there is one: `**[su + kha (trad.)]**`; 04a *omāty-*: DPD *omāti*, with *oṁ + iti* marked `(trad.)` (query 25).

## 7. Citations

- The SuttaCentral text ID, in italics, on its own line: `*AN 11.15*`, `*Dhp 109*`, `*Kp 7*`, `*Snp 1.8*`, `*DN 16:1.6–1.12*` (a segment range when the text is an extract).
- Vinaya texts use SuttaCentral's short display form: `*Kd 1:23.5*`, `*Bu NP 1*`, `*Bu Pc 58*`, `*Pvr 14*` (also `Bi …`), not `*Pli Tv Kd 1:23.5*` (2026-10-04, query 37).
- Commentarial sources have no SuttaCentral ID; they keep BM's form: `*DhpA.I.198*`, `*Sp.III.643–644*`, `*Kv.122*` (Kaṅkhāvitaraṇī). So does *Vinaya Mukha*.
- BM's PTS references (*A.I.294*, *Vin.IV.120*) are mapped to SuttaCentral IDs (*AN 3.155*). An uncertain mapping keeps BM's form and is put to the maintainer.
- Several sources on one line are separated by `; `: `*DN 2:42.1; DN 33:3.3.6; MN 6:2.1*`.

## 8. Repeated lines

The first occurrence of a line in a text gets the full table. Every later identical occurrence in the same text keeps its Pāli line and its Literal and Faithful lines, and replaces the table with this note (the exact words, in italics):

```repeat-note
Word analysis as at the first occurrence of this line.
```

- Lines that differ by even one word (*sabba-buddhānubhāvena* / *sabba-dhammānubhāvena*) are not repeats and get their own table.
- Repeats are counted within one file only, except in book 10, where they are counted across files (§12.2).
- An identical line whose words have different grammar in the second place gets its own full table (2026-10-05, query 56). Example: 07b/03 *okkamane pubbaṅgamā paviveke nikkhittadhurā*, masc nom pl for the elders, then fem nom sg agreeing with *janatā*. Lint's repeat WARN on such a line is expected and explained.

## 9. English outside the Literal and Faithful lines and the tables

Only these: the `*English title*` line under the `#` title, citation lines, the repeat note, and the rubrics below. Books 09 and 10 also allow instruction lines, variant cues and heading glosses (§12).

Rubrics are written in italics on their own line, with the parentheses, exactly as listed:

- *(Optional)* marks a line that BM prints in brackets as optional; it goes on its own line directly above that line (2026-10-04, query 14).
- In 04a/02 the six rubrics from *(Before royal ceremonies)* to *(Or, at the monastery, conclude with)* replace BM's section letters A–F and say when each section is chanted (BM 4.2.2; 2026-10-04, query 23).
- In 06/10, *(For the dead)* and *(For the living)* say which verses are chanted for whom (BM 6.10; 2026-10-04, query 46).

A rubric not on the list is stray English. If it is genuinely needed for chanting, add it to this list and log that. BM's explanatory notes (e.g. "This part is sometimes chanted on its own") are not rubrics and are left out (query 26).

```rubrics
(a.m.)
(p.m.)
(Bowing)
(Bow three times)
(Solo introduction)
(Leader)
(All)
(Men chant)
(Women chant)
(After bowing three times, with hands joined in añjali, recite the following)
(Optional)
(Before royal ceremonies)
(Before the shorter set of parittas; omitted before the longer set)
(Before the longer set of parittas; omitted before the shorter set)
(Always chanted)
(To conclude; always used outside the monastery)
(Or, at the monastery, conclude with)
(For the dead)
(For the living)
```

Anything else in English is stray: instalment labels, "Part 2", explanatory notes, translator's remarks, "Here is the translation", English section headings, page numbers, `[cite: n]` tags, code fences.

Words that lint treats as English when they appear in a Pāli line or heading. `compare.py` also uses them to drop English lines from the reference texts.

```english-stopwords
the
and
of
is
with
for
this
that
by
from
times
repeat
bow
bowing
chant
chanted
chanting
leader
verse
verses
part
instalment
installment
section
note
see
line
page
men
women
to
in
an
it
at
as
be
on
or
into
here
following
translation
literal
faithful
word
table
continued
was
were
his
her
they
who
which
what
when
all
```

## 10. Characters

- Unicode NFC (precomposed letters).
- The Pāli alphabet: a ā i ī u ū e o k kh g gh ṅ c ch j jh ñ ṭ ṭh ḍ ḍh ṇ t th d dh n p ph b bh m y r l ḷ v s h ṁ.
- No tone marks (꜓ ꜕ ꜖, from the Amaravati chanting book), no tabs, no non-breaking spaces inside Pāli words.

## 11. The changelog

One `CHANGELOG.md` per text folder (`books/<book>/texts/`, or each part folder of a book in parts). It is never built into a book. Every change to a text gets an entry. Newest entry at the top:

```text
## 2026-10-02 — session 3 (05_anumodanas)

### 01_yatha_vari_vaha_pura.md
| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 28 | [pp. of para + √i + ta + ānaṁ] | [pp of peti, pa + √i + ta] | wrong prefix | DPD peta |
| 213 | (fem nom sg) / (ind) | (fem nom pl) | agrees with plural bhavantu | grammar |
```

- The heading is the date, a short name for the change set, and the files or folder in brackets. (Legacy entries name the session, "session S22".)
- Line numbers refer to the file after the change.
- "Reference" names the authority: `DPD <headword>`, a spec section, a source (`BM 6.10`, `SC mn6:2.1`), or the maintainer's decision (`query 57`).
- A change repeated in many rows may be given once, under an "All files" heading.
- Mechanical fixes made by `lint.py --fix` are logged as one line per file ("safe fixes applied"), not row by row.
- Change types used in books 09 and 10: *misprint* (the source's reading in Was), *elision filled*, *new rendering*, *copied from 0x/file.md*, *list as variants*, *DPD*, *query Vn* / *query Dn*.

## 12. Book-specific rules

### 12.1 Vinaya formulae (09a–09e)

These files give the Pāli formulae of the Vinaya sections of the *Bhikkhu Manual* (requisites, the Rains and the Kaṭhina, other procedures, offences, the Uposatha), for bhikkhus who already use them. BM remains the guide to the procedures. Sections 1–11 apply, with these differences.

**Layout.**

```text
# Title

*English title*

> Instruction line: who speaks to whom, when, short setup

**Pāli line exactly as said**

**Literal:** literal English in Pāli word order  
**Faithful:** BM's English rendering  

| Word | Analysis & Meaning |
| :--- | :--- |
| **`pāli_word`** | `(tags)` meaning, meaning; **[etymology]** |

**Variant:** situation: *old* → *new*  

| Word | Analysis & Meaning |
| :--- | :--- |
| **`new`** | `(tags)` meaning; **[etymology]** |

*Citation*
```

- One file per procedure, numbered in BM order. BM's text for each folder is in `sources/originals/<folder>/00_original_*.md`, never edited.
- The `#` title is Pāli where BM gives a Pāli name; otherwise BM's English heading, kept (V3). Several files may share a Pāli title (*Vikappana*, *Pavāraṇā*); the English title tells them apart.
- The citation goes directly under the last unit or variant it covers.
- Sections of BM that only explain and have no formula are left out; they stay in the originals (V5). Everything with a formula is included: bhikkhu formulae, Thai lay requests, forms "from a nun", disrobing.

**Source and Pāli line.** BM only: no cross-check against Ṭhānissaro or SuttaCentral. Leader brackets are removed with the words kept, and `> Leader:` goes above: BM's *[Tisaraṇa-gamanaṁ niṭṭhitaṁ]* → *Tisaraṇa-gamanaṁ niṭṭhitaṁ*. BM's elisions (*Namo tassa…*, *…pe…*, *gilāno…*) are written out in full from BM's own wording, and logged. BM's display continuation lines (indented) are joined into one Pāli line. No numbering *(1)* or italics in the Pāli line. Long prose is divided preferably where BM's English sentences end.

**Instruction lines.** `> text` on its own line, directly above the formula it introduces. Only who speaks to whom, when or in what situation, and short setup before the act, in BM's words where possible (lint warns above 45 words). Dialogue turns get one each: `> Junior bhikkhu:`, `> Senior bhikkhu:`, `> Leader:`, `> All:`, `> The Ācariya:` (BM's **JB**/**SB** written out). Rules, reasons, lists, cross-references, links and HTML are dropped; the original keeps them.

**Faithful = BM's English.** Copy BM's wording; drop its quotation marks and italics; keep its bracketed glosses ("(of offences)").

- Fill BM's ellipses from BM's own wording (*… these robes …* → *I share these robes with you.*), and log it. Accepted under BM's licence (V1).
- Fix only obvious English typos (*acknowedges*), logged.
- Where BM gives no English, write a new rendering from the Pāli, logged as *new rendering*.
- Divide the Pāli prose so that each Faithful line is a whole BM sentence. Where BM's English covers two lines, give the whole sentence on the first and `(continued)` on the second.
- A suspected BM mistranslation is kept and put to the maintainer.
- Units copied from 01–08 keep that file's Faithful line, so a BM sentence may be split across lines (logged).

**Literal line and tables.** New work, under the same rules as 01–08: DPD on every row, compound member rows. The closing *'ti* is rendered "thus" in the Literal line. Compound members that BM writes apart are tagged `(x comp)` with a note (lint WARN, expected).

**Variant blocks.** After the base formula, one block per BM substitution:

- Cue: `**Variant:** ` + the situation in a few words (BM's) + `: ` + pairs `*old* → *new*`, separated by `; `, ending with two spaces. An omission is written `*bhante* → (omit)` and has no table.
- Table: rows for the new words only, in order. Where the change alters the grammar of a word that stays (agreement), put that word on both sides (`*imaṁ saṅghāṭiṁ* → *imaṁ pattaṁ*`), and give rows for the whole right side, with a note `[agrees with *pattaṁ*]`.
- A variant may build on an earlier one (*imāni* → *etāni* after *imaṁ* → *imāni*). Lint checks that each old word occurs in an earlier Pāli line or variant, and that the table covers exactly the new words (or the whole right side).
- BM's item lists (*uttarā-saṅgaṁ*, *pattaṁ* … for *saṅghāṭiṁ*) become one variant per item. "Substitute as in … above" is written out again: each file stands alone.
- A substitution that changes more than three words, or the syntax, is given as a full formula (a normal unit) introduced by an instruction line (*If confessing a single offence:*).
- BM's slash alternatives (*Āma bhante / Āma ayye*; *dhamma- / vinaya-kathā*; *We/I*) become base + variants (V6). So do men's and women's forms, and BM's bracketed optional words (base with the words, plus an omission variant).
- Variants come directly after the formula they change.

**Placeholder names** (*Uttaro*, *Tisso*, *Amaro*) are plain in the Pāli line. Their row has the tags the grammar requires, the note, the name, and `[proper name]`; the name's meaning is not given (V2):

`| **`uttarassa`** | `(masc dat sg)` [example name; substitute the actual name] to Uttaro; **[proper name]** |`

**Speaker forms.** Senior/junior and singular/plural address (*bhante*/*āvuso*, *hara*/*haratha*) follow BM's base formula; the other form is a variant.

**Misprints.** Fix only what is plainly a misprint (*sanghe* → *saṅghe*, *āyasamato* → *āyasmato*, *paṭigghaṅhātu* → *paṭiggaṇhātu*), with BM's reading in the changelog. If in doubt, keep BM and ask (*visajjehi* / *vissajjehi*: BM kept, V7).

**Overlaps with 01–08.** A unit whose Pāli line equals a settled 01–08 line after normalisation is copied verbatim (Pāli, Literal, Faithful, rows), with the source file cited in the changelog. Where only words recur, reuse their settled rows (`scripts/index.py rows`) and adapt them to the line.

**Pāli check.** `make compare` checks the files against the originals in `sources/originals/`. Every difference must be a filled elision, a logged misprint fix, or a fault to correct. Variant cues are checked by hand against BM's substitution lines.

**Citations.** As §7: Vinaya by SuttaCentral short form, commentaries in BM's form.

**Book.** One book, *Vinaya Formulae* (Pāli subtitle *Vinaya-pāṭha*), in five parts, 09a–09e, with BM's English part headings only (V4).

### 12.2 Mahāsatipaṭṭhānasutta (10)

A study text, read rather than chanted, for novices: every compound keeps its member rows. Sections 1–11 apply, with these differences. The book's `metadata.txt` switches on the DN 22 behaviour with these `options`: `heading-gloss`, `heading-numbers`, `repeat-across-files`, `dpd-variant-rows`.

**Layout.**

```text
# Pāli title

*English title*

### 1.1 Kāyānupassanāānāpānapabba

*English gloss*

**Pāli unit exactly as in SuttaCentral**

**Literal:** literal English in Pāli word order  
**Faithful:** natural English rendering  

| Word | Analysis & Meaning |
| :--- | :--- |
| **`pāli_word`** | `(tags)` [short note] meaning, meaning; **[etymology]** |

**Variant:** second stage: *old* → *new*  

| Word | Analysis & Meaning |
| :--- | :--- |
| **`new`** | `(tags)` meaning; **[etymology]** |

*DN 22:2.1–2.15*
```

- One file per SuttaCentral section, in SC order; SC 7–10 (the nine charnel grounds) are one file: 19 files (D1).
- The `#` title is the section's Pāli name, without a number, as in the split files; *Nigamana* for the conclusion (D4).
- **Headings** (`heading-numbers`, `heading-gloss`; D2). Each SuttaCentral heading in the section becomes `### <SC number without its final dot> <SC heading, verbatim>` (`### 1.1 Kāyānupassanāānāpānapabba`), with an `*English gloss*` line beneath (lint warns if it is missing). Glosses follow the pattern "*Contemplation of the body: the section on …*" (D8); sub-heading glosses in the definitions are plain: *Exposition of the truth of …*. Digits and glosses in headings are allowed in book 10 only.

**Source and Pāli line.** SuttaCentral's Mahāsaṅgīti text only (no BM, no Ṭhānissaro): `sources/originals/10_Mahasatipatthanasutta/00_original_Mahāsatipaṭṭhānasutta.txt`, which equals SC's root text (`dn22/pli/ms`, read from the Simsapa app with `GET /sutta.json`) word for word once its 12 *Variant:* notes and first line are dropped. Its variant readings come from `GET /sutta_bilara.json`.

- The line keeps SC's spelling, sandhi, word-joining, capitals, commas, full stops, question marks, colons and dashes.
- Quotation marks ‘ “ ” are dropped; ’ marking an elided *iti* becomes ASCII `'` (*assasāmī'ti*, *bhikkhavo'ti*), as in 01–09 (D3).
- **Units.** One sentence per unit. A long sentence is divided at clause boundaries (*Katame cattāro?* alone, then one unit per *satipaṭṭhāna*), without dropping or reordering words (D7).
- *…pe…* and “…” are written out in full from the discourse's own wording, and logged; an uncertain expansion is put to the maintainer.

**Literal and Faithful.** Literal: render mood (optative *should…*, *may…*, *would…*; imperative *let…*). Faithful: a new rendering from the Pāli, checked against DPD, never against or taken from published English (Sujato, Ṭhānissaro, Ñāṇamoli, Walshe …). Key terms as in 01–08, except *satipaṭṭhāna* = "establishment(s) of mindfulness".

**Key renderings** (D6; they bind every new or changed unit in book 10):

| Pāli | Faithful | Basis |
| :--- | :--- | :--- |
| *ekāyano maggo* | the direct path (Literal: one-way path) | DPD *ekāyana* |
| *satipaṭṭhānā* | establishments of mindfulness | maintainer |
| *kāye kāyānupassī viharati* (*vedanāsu …*, *citte …*, *dhammesu …*) | dwells contemplating the body as a body (feelings as feelings, the mind as mind, dhammas as dhammas) | 03/19; DPD |
| *ātāpī sampajāno satimā* | ardent, clearly comprehending and mindful | 03/19 |
| *vineyya loke abhijjhādomanassaṁ* | having put away covetousness and distress concerning the world (*vineyya* = abs, DPD *vineyya 1*) | 03/19; DPD |
| *pajānāti*; *sikkhati* | understands; trains (thus) | 07a/04 |
| *ñāyassa adhigamāya* | for the finding of the way | DPD |
| *samudaya-/vaya-dhammānupassī* | contemplating the nature of arising / of vanishing | DPD |
| *ñāṇamattāya paṭissatimattāya* | to the extent of bare knowing and continuous mindfulness | DPD |
| *anissito* | independent | DPD *anissita 1* |

Other settled renderings: the hindrances are sensual desire, ill will, dullness and drowsiness, restlessness and uneasiness, doubt (DPD); *dukkha* in the definitions of the truths is "pain"; *amacca* "advisers"; *pana* "moreover, and so, but" (DPD; D14); *kaṅkehi* "by kaṅka crows" (D9); *sampajānakārī* as drafted (D12).

**Word table.**

- A word joined by sandhi in SC (*satova*, *Evampi*) is one row, analysed by its parts in the note or etymology (`[sandhi of *sato* + *eva*]`). Members of SC-spelled compounds keep SC's form: elided first members with `'` (*pañc'*, *rūp'*), doubled *kkhandho*.
- **Notes.** A short bracketed note before the meaning, from DPD only (meaning, grammar, construction), never from a commentary: `[agrees with *kāye*]`, `[sandhi of *sato* + *eva*]`, `[abs of *vineti*: having removed]`. As many as a novice needs; usually at most one per unit.
- Variant rows are checked against DPD like any other row (`dpd-variant-rows`).

**Repeated lines** (`repeat-across-files`). The first occurrence of a line in book 10, in file order, gets the full table; a later word-identical line, in the same file or a later one, gets the repeat note. The refrain *Iti ajjhattaṁ vā kāye kāyānupassī viharati …* is written out in full wherever it occurs (expanded from *…pe…*); the *vedanāsu*, *citte* and *dhammesu* refrains are new lines with their own tables.

**Lists that change** (the variant method of §12.1). The first item is given in full; each later item gets a cue and a table for the changed words only: `**Variant:** <one-line English cue>: *old* → *new*; *old* → *new*  ` (two trailing spaces). Agreement changes put the kept word on both sides and give rows for the whole right side, with a note. A change of more than three words, or of syntax, is a full unit (D13: the *vicikicchā* items stay full units). Used for: the nine charnel-ground stages (the ninth also a variant, D11); the five hindrances, five aggregates, six sense bases and seven awakening factors where only the item changes; the *loke piyarūpaṁ* lists (SC 19–20); "seven years … half a month" (SC 22; D15).

**Checking variant lists.** `compare` checks only the Pāli lines, not the words inside variant cues, so each list is checked by rebuilding it:

1. Start from the base unit's Pāli line. For each variant in order, apply its `*old* → *new*` pairs to the current line (a variant may build on the one before), giving the full Pāli of that item.
2. Expand the elisions (“…”, *…pe…*) in SC's root text (`GET /sutta.json?uid=dn22/pli/ms`) from the discourse's own wording, in the same way as the files do.
3. Normalise both sides (`text.norm_line`: NFC, ṁ, Pāli letters only) and compare the rebuilt items, in order, with the segments for that list. Every item must match word for word.

The legacy project did this with one-off scripts for files 16, 17 and 19; all matched.

**Overlaps with 01–09.** A unit whose Pāli equals a settled 01–09 line after normalisation copies that line's Literal, Faithful and rows verbatim, with two adaptations: row words take SC's spelling (*sato'va* → *satova*, *kāya-saṅkhāraṁ* → *kāyasaṅkhāraṁ*), and *satipaṭṭhāna* is rendered "establishment(s) of mindfulness". Copy a line only where it is also a clause boundary in SC's text. The source file is cited in the changelog; 01–09 are never edited for this. In copied units, quotation marks in the Faithful line are double (D10). Where only words recur, reuse their settled rows (`scripts/index.py rows`).

**Citations.** One per file, under its last unit or variant: the italic SC segment range of the section, headings excluded: *DN 22:1.1–1.13*; the charnel-ground file *DN 22:7.1–10.11*.

**Book.** English title first: *The Great Discourse on the Establishments of Mindfulness*, Pāli subtitle *Mahāsatipaṭṭhānasutta*. Its About page names SuttaCentral's Mahāsaṅgīti edition, DPD, and CC BY-NC 4.0 for the English (D5).
