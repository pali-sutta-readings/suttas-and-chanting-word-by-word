# Drafting workflow

How a new sutta or chant is added to a book. The rules a text must follow are in `docs/style-spec.md`, and the checks every change goes through are in `docs/quality-process.md`. An agent follows the `draft-new-text` skill (`.claude/skills/draft-new-text/SKILL.md`), which is the step-by-step version of this page.

## The steps

1. **Get the Pāli** from the source the style spec names (§2): the *Bhikkhu Manual* (`sources/upstream/bhikkhu-manual/`), the Community Chanting Book, the *Chanting Guide*, or SuttaCentral through Simsapa (`simsapa sutta UID`). Add the text's entry to `sources/ref-map.tsv` with the `source-compare` skill.
2. **Reuse settled lines.** Build a draft holding only the `T|` and `P|` lines into a scratch file (`draft.py build`), then `python3 scripts/index.py overlaps SCRATCH.md` lists its Pāli lines that already have a table in another text. Those units are copied with `I|`, not analysed again.
3. **Get DPD's data** for the other lines: `python3 scripts/simsapa.py gloss --text "…" --text-output` (the Simsapa API must be running: the app, or `simsapa serve`). For every word it gives DPD's headwords, constructions, parses of the form and splits, and the rows other texts already use for that word.
4. **Write the rows and grammar labels** with the `pali-word-analysis` skill. No script assigns labels: DPD lists the possible readings, and the line decides.
5. **Write the Literal and Faithful lines** (style spec §3).
6. **Build the file** from the draft: `python3 scripts/draft.py build DRAFT books/<book>/texts/NN_name.md`.
7. **Check** (`docs/quality-process.md`):
   - `make lint`, to 0 ERROR and 0 STRAY;
   - `python3 scripts/compare.py diff FILE`, classified with the `source-compare` skill;
   - `python3 scripts/simsapa.py check FILE`, reviewed with the `dpd-review` skill;
   - `python3 scripts/index.py index` for consistency with the other texts;
   - a spot check of 10 units by a second agent.
8. **Log it** in the folder's `CHANGELOG.md` (style spec §11): a new text gets one entry naming its source and the results of step 7.
9. **Build** the book: `make book BOOK=<book>`.

## The draft format

A draft is a plain text file with one item per line, which `scripts/draft.py build` turns into a chant file. `draft.py extract FILE` turns any chant file back into a draft, so an existing text shows the format by example. Blank lines and lines starting with `#` are ignored.

| Line | Gives |
| :--- | :--- |
| `T|title` | the Pāli title (`# …`) |
| `E|English title` | the English title after `T`; after `H`, the heading gloss (book 10) |
| `H|heading` | a `###` heading |
| `U|rubric` | a rubric, `*(…)*` |
| `S|instruction` | a Vinaya instruction line (`> …`) |
| `P|Pāli line` | a unit: a full table, or the repeat note if the same line came earlier in the draft |
| `P!|…`, `P~|…` | force a full table, or force the repeat note |
| `L|…`, `F|…` | the unit's Literal and Faithful lines |
| `R|word|tags|meaning|etymology` | a table row; tags without parentheses, groups separated by ` / `; the meaning may start with a `[note]` |
| `M|word|tags|meaning|etymology` | a `↳` member row of the compound before it |
| `T0|` | a table header with no rows |
| `V|cue` | a `**Variant:**` cue; the `R|`/`M|` rows after it are its table |
| `C|citation` | a citation, `*…*` |
| `I|text path|Pāli line` | copy the unit of another text whose Pāli line matches (after normalisation); an error if none or more than one does |

An example, from the start of `books/01_morning_chanting/texts/02_preliminary_homage.md`:

```text
T|Pubbabhāga-namakāra
E|Preliminary Homage
P|Handa mayaṁ buddhassa bhagavato pubbabhāga-namakāraṁ karomase
L|Come now, we to [the] Buddha, [the] Blessed One, preliminary homage let us make
F|Now let us pay preliminary homage to the Buddha, the Blessed One.
R|handa|interj|come now, well then|handa
R|mayaṁ|1st pl nom|we|ahaṁ
R|buddhassa|masc dat/gen sg|to the Buddha, of the Buddha|√budh + ta
R|bhagavato|masc dat/gen sg|to the Blessed One|√bhaj > bhag + a + vant
R|pubbabhāga-namakāraṁ|masc acc sg comp|preliminary homage, homage that comes first|pubba + bhāga + namakāra
M|pubba|adj comp|prior, former|pubba, no root in DPD
M|bhāga|masc comp|part|√bhaj + a
M|namakāraṁ|masc acc sg|homage, act of veneration|nama + kāra (√kar + a)
R|karomase|1st pl pres mid imperat|let us make, let us do|√kar + o + mase
```

## The skills

| Skill | For |
| :--- | :--- |
| `draft-new-text` | the whole workflow above, step by step |
| `pali-word-analysis` | rows, grammar labels, etymologies and member rows |
| `source-compare` | the ref-map entry and the Pāli check against the source |
| `dpd-review` | the DPD check's flags and candidates, and consistency across files |

### Rules shared between skills

When a rule below changes in one skill, check the others in its row (`CLAUDE.md`, "Maintaining the skills").

| Rule | Where it lives | Skills that state it |
| :--- | :--- | :--- |
| Start `simsapa serve` if it is not running; stop it when done | `CLAUDE.md`, "DPD via Simsapa" | `draft-new-text` §0, `pali-word-analysis` §1, `dpd-review` §1, `source-compare` (Tools) |
| SuttaCentral conversions (quotation marks, `”ti` as `'ti`, closing number-word, pādas joined) | style spec §2 | `draft-new-text`, `source-compare` (expected differences) |
| Repeated lines: reuse `I|`; verse repeat of a prose line has no rows; `P!|` forces a table | style spec §8, `draft-new-text` §2 | `pali-word-analysis` §1, `dpd-review` §2 |
| Analysis questions are decided by the agent; only Pāli-text doubts are queries | `CLAUDE.md`, `pali-word-analysis` §7 | `dpd-review` §2, `draft-new-text` |
| Spot check by a separate agent only if the maintainer asks; otherwise log "not yet run" | `draft-new-text` §7, `docs/quality-process.md` §5 | `draft-new-text` |
| A text error found by a check is fixed only with approval and a changelog entry | `CLAUDE.md` | `source-compare` §5, `dpd-review` §5 |
