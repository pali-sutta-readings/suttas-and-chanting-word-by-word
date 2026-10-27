# Changelog: 11_learning_the_word_by_word_meaning

Newest session first. Per file: `| Line | Was | Now | Why | Reference |` (spec §9).
This is a prose book: its text is `content/guide.md`, not a chant file. The line
numbers are those of that file as it stands after the session.

## 2026-10-27 — first edition (converted from the author's DOCX)

New book, made from
`sources/originals/11_learning_the_word_by_word_meaning/`. The DOCX was
converted with pandoc, then edited by hand. Light copy-editing only: wording,
figures, links and headings were kept as the author wrote them, and the queries
below were left for the author rather than settled here.

### Structure and layout

- The DOCX title, *Learning the Word-by-Word Meaning of the Chanting*, is the
  book's title (H1) and its cover.
- "How to use word-by-word translations" became an unnumbered preface (H2),
  "Making a Leitner Box" the chapter (H2), and its five subsections H3s.
- The DOCX repeated the running title inside the body after "…a Leitner box."
  (a pagination artefact of Word); it is not part of the text and was removed.
- The single table is the checked table from
  `books/05_anumodanas/texts/01_yatha_vari_vaha_pura.md`, as the About page
  says. It is kept on one page with `.keep`.
- The 13 screenshots are figures in reading order, renamed `01.png`–`13.png`,
  composited on white, with alt text for the EPUB. `07.png` is cropped as in
  Word. Single cards are `{width=2.8in}`, spreads `{width=100%}`.
- The figures were redrawn, not upscaled: the DOCX stores 96-dpi screenshots,
  which print at only 154–186 ppi. `images/make_figures.py` draws the same
  cards, borders, dots and emphasised text at three times the source size, in
  Noto Sans (the house sans; the DOCX used Segoe UI), so they now print at
  460–760 ppi. Text, colours and positions are the author's; only the rendering
  is new. It needs Pillow and is run by hand; the build only reads the PNGs.
- The list of six "cards reading" entries keeps the DOCX hard line breaks.
- A Resources appendix gives the full address of every link, since a printed
  page cannot follow "here" and "this".
- The cover title is 26 pt (`title-size`), because the title is long.

### content/guide.md

| Line | Was | Now | Why | Reference |
| :--- | :--- | :--- | :--- | :--- |
| 10 | `not scholarly and are` | `not scholarly, and are` | comma before the new clause | — |
| 13 | link text `https://simsapa.github.io/` | `Simsapa` | link text a reader can use on paper | — |
| 15 | `effort has been made` | `an effort has been made` | missing article | — |
| 16 | `and in general are a reliable` | `and are, in general, a reliable` | parenthetical commas | — |
| 19–21 | link text `https://pali-sutta-readings.github.io/pali-lessons/` | `Pāli Sutta Readings lessons` | link text a reader can use on paper | — |
| 34 | `such that they understand` | `so that they understand` | idiom | — |
| 38 | `In effect a SRS` | `In effect, an SRS` | punctuation; article | — |
| 44–48 | `this YouTube video`, `this article`, `Fluent Forever` | `this YouTube video from Osmosis`, `this article by Gwern`, *Fluent Forever* | name the sources for a printed page | — |
| 50–51 | `windows, android, MacOS` | `Windows, Android, macOS` | product names | — |
| 52 | `browser.)` | `browser).` | closing bracket after the full stop | — |
| 57, 86 | `and/ or` | `and/or` | spacing | — |
| 59 | `paper based SRS using a Leitner Box` | `paper-based SRS using a Leitner box` | hyphen; the term as used elsewhere | — |
| 64 | `a SRS` | `an SRS` | article (also line 376) | — |
| 71–72 | `flash cards` | `flashcards` | one word | — |
| 74 | `words/ translations` | `words/translations` | spacing | — |
| 81–83 | `You can find an example [here](…)` | `You can find an example schedule in this [Google Sheets template](…)` | link text a reader can use on paper | — |
| 123, 159 | `flash card` | `flashcard` | one word | — |
| 124 | `left hand corner` | `left-hand corner` | compound adjective | — |
| 149 | `a total of 14 cards` | `a total of 12 cards` | six words, a card in each direction | author, 2026-10-27 |
| 164 | `much much` | `much, much` | punctuation | — |
| 175 | `more useful as your brain` | `more useful, as your brain` | comma before the new clause | — |
| 176–177 | `noticing. However the` | `noticing. However, the` | comma | — |
| 227 | `the below` | `the following` | style | — |
| 228 | `English-Pali` | `English-Pāli` | spelling | — |
| 264–265 | `extra time then presenting … context that would work best` | `extra time, presenting … context would work best` | punctuation; redundant `that` | — |
| 283 | `your flashcards they are ready` | `your flashcards, they are ready` | comma splice | — |
| 309 | `making the cards, just make` | `making the cards: just make` | colon before the explanation | — |
| 313 | `level's up envelope` | `level's envelope` | typo | — |
| 315–316 | `level one`, `level two` | `Level 1`, `Level 2` | consistency with "Level 1" elsewhere | — |
| 325 | `everyday` | `every day` | adverb | — |
| 326 | `missing days the reviews will start piling up which` | `missing days, the reviews will start piling up, which` | commas | — |
| 332 | `at level 7 and having gotten it correct` | `at Level 7 and having got it right` | consistency; British usage | — |
| 333 | `nailed its meaning then … Otherwise only discard` | `nailed its meaning, then … Otherwise, only discard` | commas | — |
| 376 | `a SRS` | `an SRS` | article | — |
| 385 | `end of the project, celebrate` | `end of the project; celebrate` | semicolon between clauses | — |
| 386–387 | `flashcard making session or a reviewing session,` | `flashcard-making session or a review session,` | compound; wording | — |
| 390, 399 | `Leitner Box` | `Leitner box` | the term as used elsewhere | — |
| 398 | `etc)` | `etc.)` | closing bracket | — |
| 402 | `so only a few cards are getting added` | `so that only a few cards are added` | grammar | — |
| 404 | `reviewing the cards as they will pile up` | `reviewing the cards, as they will pile up` | comma | — |
| 406 | `get them in but just keep going` | `get them in, but just keep going` | comma | — |
| various | straight double quotes | typographic “ ” | house style; apostrophes stay ASCII and the build sets them (spec §2) | — |

The card count was queried in the first draft (six words listed, but "14 cards"):
the author confirmed the number should be 12, and the text now says so.
