// The functions that templates/pandoc/chant.lua calls for the classed divs
// written by scripts/assemble.py (docs/book-build.md), plus the word table,
// the contents page and the blank verso.

#import "style.typ": document-style, document-setup

#let fonts = document-style.fonts
#let sizes = document-style.sizes
#let colors = document-style.colors

// ============================================================================
// TITLES AND CONTENTS
// ============================================================================

// A chant title is "Pāli title #toc-en[— English title]": the English part
// shows in the contents only, not in the heading or the running header.
#let in-outline = state("in-outline", false)
#let toc-en(body) = context if in-outline.get() [ #body]

#let contents-page(depth: 1) = page(header: none, {
  block(below: 1.5em, text(size: sizes.heading1)[Contents])
  show outline: it => {
    in-outline.update(true)
    it
    in-outline.update(false)
  }
  show outline.entry: set par(justify: false)
  show outline.entry.where(level: 1): set block(above: 0.9em)
  outline(title: none, depth: depth, indent: 1.2em)
})

#let blank-page() = page(header: none, footer: none)[]

// ============================================================================
// UNIT ELEMENTS
// ============================================================================

// A unit: its Pāli line and renderings (unit-head), then its word table or
// repeat note, and any variant cues with their tables.
#let unit(body) = block(above: document-style.spacing.before-unit, below: 0pt, body)

// The head of a unit stays on the same page as the start of its table.
// Inside it, the gap between the Pāli line and the renderings is a little
// wider than the leading, so that a wrapped line is not read as the next one.
// The wider gap at the end sets the renderings apart from the word table.
#let unit-head(body) = {
  set par(leading: document-style.leading.unit-head)
  block(sticky: true, breakable: false,
    below: document-style.spacing.after-unit-head, body)
}

#let pali(body) = block(below: document-style.spacing.after-pali,
  text(lang: "pi", weight: "bold", size: sizes.pali, body))

// The literal and faithful renderings. The wider space above sets them apart
// from each other; the gap from the Pāli line is after-pali (1.2em), which is
// wider still, so that gap does not change. They are indented under the
// Pāli line, wrapped lines too, and a little smaller than the body text.
#let rendering(body) = {
  set par(justify: false, spacing: 0.6em)
  set text(size: sizes.rendering)
  block(above: 0.9em, below: 0.6em,
    inset: (left: document-style.spacing.rendering-indent), body)
}
#let literal(body) = rendering(body)
#let faithful(body) = rendering(body)

#let repeat-note(body) = block(above: 0.4em, text(size: sizes.small, body))

#let citation(body) = block(above: 0.6em, below: 0.4em,
  align(right, text(size: sizes.small, body)))

// A book figure (a prose book's screenshot): centred, with room above and
// below. The image itself carries its width as a percentage of the text.
#let figure-block(body) = {
  set align(center)
  block(above: 1em, below: 1em, body)
}

// Keep a short unit and its table on one page (prose books).
#let keep-block(body) = block(breakable: false, body)

// A list of links: ragged right, so long addresses do not stretch the line.
#let resources(body) = {
  set par(justify: false)
  // Tight items, in a slightly smaller size: the entries wrap, so at body
  // size the list runs onto a page of its own.
  set list(spacing: 0.45em)
  set text(size: 0.9em)
  body
}

#let rubric(body) = block(above: 0.8em, below: 0.6em, body)

// The English title under a chant title (pandoc's subtitle div).
#let en-title(body) = block(above: 0em, below: 1.2em, text(size: sizes.body * 1.1, body))

// Book 10: the English gloss under a numbered heading.
#let gloss(body) = block(above: -0.2em, below: 0.9em, body)

// Vinaya instruction lines and variant cues (style spec §12.1).
#let instruction(body) = block(
  above: 1em, below: 0.6em, inset: (left: 0.7em),
  stroke: (left: 1.5pt + colors.rule),
  emph(body))

#let variant(body) = block(above: 0.9em, below: 0.4em, sticky: true, body)

// ============================================================================
// WORD TABLE
// ============================================================================

// A tag group, e.g. (masc nom sg).
#let tags(body) = text(font: fonts.sans, size: sizes.tags, body)

// rows: (word, analysis, member) triples; member rows start with ↳ and are
// indented. The header repeats when a table breaks across pages. The table
// has no cell borders: the shaded header row alone separates it.
#let word-table(header: (), rows: ()) = {
  set text(size: sizes.table)
  set par(justify: false, leading: document-style.leading.table)
  table(
    columns: (auto, 1fr),
    stroke: none,
    inset: (x: 4pt, y: 3.5pt),
    fill: (_, y) => if y == 0 { colors.header-fill },
    table.header(..header.map(h => text(font: fonts.sans, size: sizes.tags, h))),
    ..rows.map(((word, analysis, member)) => (
      if member { pad(left: 0.6em, word) } else { word },
      analysis,
    )).flatten(),
  )
}
