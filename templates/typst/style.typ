// ============================================================================
// LANGUAGE STRINGS
// ============================================================================

#let language-strings = (
  "contents": (
    "en": "Contents",
    "pt": "Índice",
    "it": "Indice",
    "fr": "Table des matières",
    "si": "Kazalo",
    "de": "Inhaltsverzeichnis",
    "hu": "Tartalomjegyzék",
    "es": "Índice",
    "ca": "Índex",
    "cs": "Obsah",
  ),
  "answer-key": (
    "en": "Answer Key",
    "pt": "Chave de Respostas",
    "it": "Risposte Esatte",
    "fr": "Corrigé",
    "si": "Rešitve",
    "de": "Lösungsschlüssel",
    "hu": "Megoldókulcs",
    "es": "Hoja de Respuestas",
    "ca": "Solucions",
    "cs": "Klíč odpovědí",
  ),
  "disclaimer-note-text": (
    "en": [#emph[The translation from the English text was made by Claude AI.]],
    "pt": [#emph[A tradução do texto em inglês foi feita por Claude AI.]],
    "it": [#emph[La traduzione dal testo inglese è stata realizzata da Claude AI.]],
    "fr": [#emph[La traduction du texte anglais a été réalisée par Claude AI.]],
    "si": [#emph[Prevod iz angleškega besedila je pripravil Claude AI.]],
    "de": [#emph[Die Übersetzung aus dem englischen Text wurde von Claude AI erstellt.]],
    "hu": [#emph[Az angol szöveg fordítását a Claude AI készítette.]],
    "es": [#emph[La traducción del texto en inglés fue realizada por Claude AI.]],
    "ca": [#emph[La traducció del text en anglès ha estat realitzada per Claude AI.]],
    "cs": [#emph[Překlad z anglického textu byl vytvořen pomocí Claude AI.]],
  ),
)

#let get-lang-string(key, lang) = {
  if language-strings.keys().contains(key) {
    let string-dict = language-strings.at(key)
    return string-dict.at(lang, default: string-dict.at("en"))
  }
  none
}

// ============================================================================
// TYPOGRAPHY CONFIGURATION
// ============================================================================

#let document-style = (
  // Font families
  fonts: (
    body: "Crimson",                 // Primary serif font for body text (corrected name)
    heading1: "Libertinus Serif Display", // Display serif for main headings
    heading2: "Noto Sans",           // Sans-serif for section headings
    thai-body: "Kinnari",            // Thai script for body text
    thai-heading: "Garuda",          // Thai script for headings
    chinese-body: "Noto Serif CJK HK",
  ),

  // Font sizes
  sizes: (
    body: 11pt,          // Standard reading size
    heading1: 20pt,      // 2x body size - clear hierarchy
    heading2: 14pt,      // Section headings
    heading3: 14pt,      // Subsections
    quote: 12pt,         // Same as body, distinguished by style
    small: 10pt,         // Captions, footnotes
    thai-heading: 18pt,  // Reference: Thai text in headings (functions now inherit size)
    thai-normal: 12pt,   // Reference: Thai text in body (functions now inherit size)
  ),

  // Line spacing (leading)
  leading: (
    body: 0.9em,         // ~120% line height (1.2 - 1 = 0.2, then * font-size-factor)
    header: 0.5em,       // ~100% line height for headers
    footnote: 0.8em,
  ),

  // Paragraph spacing
  spacing: (
    after-paragraph: 20pt,      // Space after body paragraphs
    before-heading1: 26pt,      // Space before major sections
    after-heading1: 30pt,       // Space after major sections (increased from 16pt)
    before-heading2: 20pt,      // Space before sections (increased from 20pt)
    after-heading2: 10pt,       // Space after sections (increased from 12pt)
    quote-indent: 36pt,         // Left indent for block quotes (0.5 inch)
    before-quote: 18pt,         // Space before quote blocks
    after-quote: 18pt,          // Space after quote blocks
    before-footnote: 4pt,     // Space before footnotes
    after-footnote: 6pt,      // Space after footnotes
  ),

  // Colors
  colors: (
    text: black,         // Pure black for high-contrast readability
  ),

  // Page settings
  page: (
    paper: "a4",
    margin: (x: 2.5cm, y: 2.5cm),
  ),

  // Image settings
  image: (
    wrap-side: right,           // Default side for wrapped images
    wrap-width: 40%,            // Default width for wrapped images
    caption-size: 10pt,         // Caption font size
    caption-spacing: 6pt,       // Space between image and caption
  )
)

// ============================================================================
// DOCUMENT SETUP FUNCTION
// ============================================================================

#let remove-newlines(content) = {
  if content == none {
    return none
  }

  // Replace linebreaks with spaces in the content
  show linebreak: " "
  content
}

#let answerkey = lower(sys.inputs.at("answerkey", default: "false")) == "true"

// Custom table of contents with Thai title
// Shows level-1 and level-2 headings only
#let table-of-contents(
  language: "en",
  after-content: none,
) = {
  set align(center)
  set text(
    font: document-style.fonts.heading1,
    size: document-style.sizes.heading1,
    weight: "regular",
  )

  [#get-lang-string("contents", language)]

  v(2em)

  set align(left)
  set text(size: document-style.sizes.body)

  // Custom outline showing only level 1 and 2
  show outline.entry.where(level: 1): it => {
    set text(
      font: document-style.fonts.heading1,
      size: document-style.sizes.heading3,
      weight: "regular"
    )
    v(0.8em, weak: false)
    block(
      width: 100%,
      {
        // Add spacing after level-1 entries
        it
      }
    )
  }

  show outline.entry.where(level: 2): it => {
    set text(
      font: document-style.fonts.body,
      size: document-style.sizes.body
    )
    block(
      inset: (left: 1.5em),
      width: 100%,
      it
    )
  }

  outline(
    title: none,
    depth: 2,
    indent: auto,
  )

  if after-content != none {
    [#after-content]
  }
}

#let document-setup(
  title: none,
  title-image: none,
  subtitle-content: none,
  language: "en",
  body
) = {
  // Set document properties
  set document(
    title: title,
  )

  // Text defaults - Crimson for body
  set text(
    font: document-style.fonts.body,
    size: document-style.sizes.body,
    fill: document-style.colors.text,
    lang: language,
  )

  // Paragraph settings - justified with generous spacing
  set par(
    justify: true,
    leading: document-style.leading.body,
    spacing: document-style.spacing.after-paragraph,
  )

  // Block spacing
  set block(
    spacing: document-style.spacing.after-paragraph,
  )

  set table(
    stroke: none,
    row-gutter: 4pt,
  )

  // URL links and in-document label links are underlined. Links with a bare
  // location destination (outline entries) keep their own formatting, so the
  // table of contents stays unadorned.
  show link: it => {
    if type(it.dest) == str or type(it.dest) == label {
      underline(offset: 2.25pt, it)
    } else {
      it
    }
  }

  // ============================================================================
  // TITLE PAGE
  // ============================================================================

  if title != none {
    set page(
      paper: document-style.page.paper,
      margin: document-style.page.margin,
      numbering: none,  // No page number on title page
      header: none,
    )

    if title-image != none {
      set align(center)
      image(title-image, width: 135mm)
      v(1.5em)
    }

    set align(center)
    set text(
      font: document-style.fonts.heading1,
      size: document-style.sizes.heading1 * 1.2,
      weight: "regular",
    )

    text(title)
    v(1em)

    if subtitle-content != none {
      block[
        #set text(size: 18pt)
        #subtitle-content
      ]
      v(1em)
    }

    // v(1.5cm)
    // line(length: 40%, stroke: 0.5pt + luma(180))
    // v(0.4cm)
    block(height: 14pt)[
      #if answerkey {
        text(
          font: document-style.fonts.body,
          size: 14pt,
          fill: rgb("#c0392b"),
          weight: "bold",
          spacing: 4pt,
          tracking: 1pt,
        )[#upper[#get-lang-string("answer-key", language)]]
      }
    ]

    // pagebreak()
    v(1em)

    [#table-of-contents(language: language)]

    [#v(1fr)]

    // No need to display the disclaimer for the original English.
    if (language != "en") {
      block[
        #set text(font: document-style.fonts.body, size: 12pt)
        #align(center)[
          #get-lang-string("disclaimer-note-text", language)
        ]
      ]

      v(10mm)
    }

    [
      #text(
        font: document-style.fonts.body,
        size: document-style.sizes.body,
      )[
          *Pāli Exercises* \
          #link("https://github.com/pali-sutta-readings/pali-exercises/releases")

          *Simsapa Dhamma Reader* \
          #link("https://github.com/simsapa/simsapa-ng/releases/") \
          See short demo video in the release notes \
          Note: Database download is approx. 700 MB

          *Digital Pāli Dictionary (integrated in Simsapa)* \
          #link("https://dpdict.net/")

          *Pāli Sutta Readings (includes chanting analysis)* \
          #link("https://pali-sutta-readings.github.io/")
      ]
    ]
  }

  // ============================================================================
  // PAGE CONFIGURATION WITH RUNNING HEADERS
  // ============================================================================

  // State to track current section for running headers
  let section-state = state("current-section", none)

  set page(
    paper: document-style.page.paper,
    margin: document-style.page.margin,
    numbering: "1",
    number-align: center,

    header: context {
      let page-num = here().page()
      let headings = query(selector(heading).before(here()))

      // Find the most recent level-1 or level-2 heading
      // let current-section = none
      // for h in headings.rev() {
      //   if h.level == 1 or h.level == 2 {
      //     current-section = h.body
      //     break
      //   }
      // }

      // Find the most recent level-1 heading
      let current-section = none
      for h in headings.rev() {
        if h.level == 1 {
          current-section = remove-newlines(h.body)
          break
        }
      }

      // Check if we're on a chapter page (page starts with level-1 heading)
      let is-chapter-page = false
      let headings-on-page = query(selector(heading.where(level: 1)).after(here()))
      if headings-on-page.len() > 0 {
        let first-heading = headings-on-page.first()
        if first-heading.location().page() == page-num {
          is-chapter-page = true
        }
      }

      // Also check if a level-1 heading is very close to the top of this page
      let all-headings = query(heading.where(level: 1))
      for h in all-headings {
        if h.location().page() == page-num {
          is-chapter-page = true
          break
        }
      }

      if is-chapter-page {
        // Chapter pages: no header
        none
      } else if current-section != none {
        set text(size: 12pt, style: "italic")

        if calc.odd(page-num) {
          // Odd pages: section on left, page number on right
          grid(
            columns: (1fr, auto),
            align: (left, right),
            current-section,
            str(page-num)
          )
        } else {
          // Even pages: page number on left, section on right
          grid(
            columns: (auto, 1fr),
            align: (left, right),
            str(page-num),
            current-section
          )
        }
      }
    },

    footer: context {
      let page-num = here().page()

      // Check if we're on a chapter page
      let is-chapter-page = false
      let all-headings = query(heading.where(level: 1))
      for h in all-headings {
        if h.location().page() == page-num {
          is-chapter-page = true
          break
        }
      }

      if is-chapter-page {
        // Chapter pages: centered page number in footer
        set align(center)
        set text(size: 10pt)
        str(page-num)
      }
    }
  )

  // ============================================================================
  // HEADING STYLING
  // ============================================================================

  // Level 1 headings - chapters, start on odd pages
  show heading.where(level: 1): it => {
    // Chapter may start on any page, expecting office paper prints

    set text(
      font: document-style.fonts.heading1,
      size: document-style.sizes.heading1,
      weight: "regular",
    )
    set align(center)
    context {
      let pos = here().position()
      // Only add spacing if not at the top of the page
      if pos.y > document-style.page.margin.y {
        v(document-style.spacing.before-heading1)
      }
    }
    block(
      below: document-style.spacing.after-heading1,
      it.body
    )
  }

  show heading.where(level: 2): it => {
    set text(
      font: document-style.fonts.heading2,
      size: document-style.sizes.heading2,
      weight: "regular",
    )
    context {
      let pos = here().position()
      // Only add spacing if not at the top of the page
      if pos.y > document-style.page.margin.y {
        v(document-style.spacing.before-heading2)
      }
    }
    it.body
    v(-0.6em)
    line(length: 100%, stroke: 0.4pt)
    v(document-style.spacing.after-heading2)
  }

  show heading.where(level: 3): it => {
    set text(
      font: document-style.fonts.body,
      size: document-style.sizes.heading3,
      weight: "regular",
      style: "italic",
    )
    block(
      above: document-style.spacing.before-heading2,
      below: document-style.spacing.after-heading2,
      it.body
    )
  }

  // ============================================================================
  // FOOTNOTE STYLING - NO SEPARATOR LINE
  // ============================================================================

  set footnote.entry(
    separator: none,  // No rule above footnotes
    indent: -0.8em, // hanging indent for numbered-list-like paragraphs
  )

  show footnote.entry: it => {
    set text(size: document-style.sizes.small)
    block(
      above: document-style.spacing.before-footnote,
      below: document-style.spacing.after-footnote,
    )[
      #set par(leading: document-style.leading.footnote)
      #pad(left: 1em, rest: 0pt)[
        #set par(first-line-indent: -1em)
        #it
      ]
    ]
  }

  body
}


// ============================================================================
// CUSTOM FORMATTING FUNCTIONS
// ============================================================================

#let fillin(space, solution) = {
  if answerkey {
    box(
      width: space,
      height: 1.5em,
      stroke: (bottom: 0.6pt + luma(160)),
      inset: (bottom: 3pt, left: 2pt),
    )[#v(0.5em) #text(fill: rgb("#c0392b"), style: "italic", size: 1em)[#solution]]
  } else {
    box(
      width: space,
      height: 1.5em,
      stroke: (bottom: 0.6pt + luma(160)),
      inset: (bottom: 3pt),
    )[]
  }
}

// helpers
#let pali(body) = emph(body)
#let B(body) = strong(body)
#let E(body) = emph(body)
#let thai(body) = text(font: "Kinnari")[#body]
#let skr(body) = text(font: "Siddhanta")[#body]
#let skrOld(body) = text(font: "Sahadeva")[#body]

#let red(body) = text(fill: rgb("#c0392b"))[#body]
#let Bred(body) = underline(offset: 2.25pt)[#text(fill: rgb("#c0392b"), weight: "bold")[#body]]

#let note(body) = block(
  width: 100%,
  inset: (x: 14pt, y: 10pt),
  radius: 3pt,
  fill: luma(245),
  stroke: 0.4pt + luma(200),
)[#text(size: 9.5pt)[#body]]

#let tblfill = (_, y) => if y == 0 { luma(235) }

// Block quote - italic, indented
#let quote-italic(content) = {
  set text(style: "italic")
  set par(justify: true, leading: document-style.leading.body)
  block(
    inset: (left: document-style.spacing.quote-indent),
    above: document-style.spacing.before-quote,
    below: document-style.spacing.after-quote,
    content
  )
}

#let quote(content) = {
  set text(style: "normal")
  set par(justify: true, leading: document-style.leading.body)
  block(
    inset: (left: document-style.spacing.quote-indent),
    above: document-style.spacing.before-quote,
    below: document-style.spacing.after-quote,
    content
  )
}

