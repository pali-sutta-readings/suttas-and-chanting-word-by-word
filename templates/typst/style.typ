// Page, fonts, sizes and headings for the A5 chant books.
// Adapted from pali-exercises/exercises/style.typ; docs/book-build.md
// describes the PDF build.

// ============================================================================
// TYPOGRAPHY CONFIGURATION
// ============================================================================

// Every font list ends in "Noto Sans Math": it is used only for glyphs the
// main font lacks, chiefly ↳ (U+21B3) in member rows.
#let document-style = (
  // Font families
  fonts: (
    body: ("Crimson", "Noto Sans Math"),     // Body text, Pāli lines, headings
    sans: ("Noto Sans", "Noto Sans Math"),   // Tag groups, table header, running header
  ),

  // Font sizes
  sizes: (
    body: 10.5pt,
    pali: 11.5pt,        // The bold Pāli line of a unit
    heading1: 17pt,      // Chant titles (and part titles in a book in parts)
    heading2: 14pt,      // Chant titles in a book in parts; About sub-headings
    heading3: 11.5pt,    // Pāli headings inside a chant
    table: 9pt,          // Word tables
    tags: 7.5pt,         // Tag groups, e.g. (masc nom sg)
    small: 8.5pt,        // Running header, page numbers, citations
  ),

  // Line spacing (leading)
  leading: (
    body: 0.8em,
    unit-head: 0.4em,    // The Pāli line and renderings of a unit
    table: 0.9em,
  ),

  // Paragraph spacing
  spacing: (
    after-paragraph: 0.8em,
    before-heading1: 0pt,       // Chant titles start a new page
    after-heading1: 0.5em,
    before-heading2: 1.4em,
    after-heading2: 0.6em,
    before-unit: 1.6em,
    after-pali: 1.2em,            // Between the Pāli line and its renderings
    after-unit-head: 1.4em,     // Between the renderings and the word table
  ),

  // Colors
  colors: (
    text: black,
    link: rgb("#1a5fb4"),    // URL links; covers do not use document-setup
    rule: luma(170),
    header-fill: luma(238),
  ),

  // Page settings
  page: (
    paper: "a5",
    margin: (inside: 17mm, outside: 14mm, top: 18mm, bottom: 18mm),
  ),
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

// The chant titles are the outlined headings at levels 1 to chant-level:
// 1, or 2 for a book in parts (09), where level 1 is the part.
#let is-chant-title(h, chant-level) = h.outlined and h.level <= chant-level

#let document-setup(
  title: none,
  lang: "en",
  region: "GB",
  chant-level: 1,
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
    lang: lang,
    region: region,
  )

  set par(
    justify: true,
    leading: document-style.leading.body,
    spacing: document-style.spacing.after-paragraph,
  )

  // URL links are blue and underlined. The cover is built by cover.typ, which
  // imports document-style but does not call document-setup, so it keeps its
  // own design.
  show link: it => text(fill: document-style.colors.link, underline(it))

  set block(
    spacing: document-style.spacing.after-paragraph,
  )

  // ============================================================================
  // PAGE CONFIGURATION WITH RUNNING HEADERS
  // ============================================================================

  // Verso pages carry the book title, recto pages the current chant title.
  // A page on which a chant starts has no header.
  set page(
    paper: document-style.page.paper,
    margin: document-style.page.margin,
    numbering: "1",

    header: context {
      let page-num = here().page()
      let titles = query(heading).filter(h => is-chant-title(h, chant-level))
      if titles.any(h => h.location().page() == page-num) {
        return none
      }
      let before = titles.filter(h => h.location().page() < page-num)
      if before.len() == 0 {
        return none
      }

      set text(font: document-style.fonts.sans, size: document-style.sizes.small)
      if calc.odd(page-num) {
        align(right, remove-newlines(before.last().body))
      } else {
        align(left, title)
      }
    },

    footer: context {
      set align(center)
      set text(size: document-style.sizes.small)
      counter(page).display()
    },
  )

  // ============================================================================
  // HEADING STYLING
  // ============================================================================

  // Headings are styled by role, not level: a part title (book 09 only) has
  // a page of its own, a chant title starts a new page, and the rest are
  // sections (About sub-headings, Pāli headings inside a chant).
  show heading: it => {
    set par(justify: false)
    if it.outlined and it.level < chant-level {
      pagebreak(weak: true)
      v(25%)
      align(center, text(size: document-style.sizes.heading1 * 1.3, it.body))
      pagebreak()
    } else if is-chant-title(it, chant-level) {
      pagebreak(weak: true)
      set text(size: document-style.sizes.heading1, weight: "regular")
      block(
        above: document-style.spacing.before-heading1,
        below: document-style.spacing.after-heading1,
        it.body
      )
    } else if it.level <= 2 {
      set text(size: document-style.sizes.heading2, weight: "regular")
      block(
        above: document-style.spacing.before-heading2,
        below: document-style.spacing.after-heading2,
        sticky: true,
        it.body
      )
    } else {
      set text(size: document-style.sizes.heading3, weight: "regular", style: "italic")
      block(
        above: document-style.spacing.before-heading2,
        below: document-style.spacing.after-heading2,
        sticky: true,
        it.body
      )
    }
  }

  body
}
