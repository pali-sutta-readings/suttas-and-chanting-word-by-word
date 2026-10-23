// The generated A5 book cover (docs/book-build.md). Its data is
// build/covers/<book>.json, written by `scripts/assemble.py --cover-data`
// from books/<book>/metadata.txt.
//
// Compiled on its own, it renders the cover of the book named by the
// cover-data input (the EPUB cover PNG):
//
//   typst compile --root . --input cover-data=/build/covers/<book>.json \
//     templates/typst/cover.typ build/covers/<book>.png --format png --ppi 300
//
// The PDF imports cover-page() for its first page.

#import "style.typ": document-style

#let default-accent = "#7a2e1a"

// data: title, subtitle, pali-title-first, series-line, accent (may be "").
// The Pāli one of title and subtitle is the title when pali-title-first is
// true, else the subtitle; the Pāli subtitle is set in italic.
#let cover-page(data) = {
  let accent = rgb(if data.at("accent", default: "") != "" { data.accent } else { default-accent })
  let pali-first = data.at("pali-title-first", default: false)
  let serif = document-style.fonts.body
  let sans = document-style.fonts.sans

  page(paper: "a5", margin: (x: 16mm, top: 30mm, bottom: 22mm),
       header: none, footer: none, numbering: none, fill: white)[
    #set par(justify: false)
    #set align(center)
    #set text(font: serif, fill: luma(20))

    #text(font: sans, size: 7.5pt, tracking: 0.18em, fill: accent,
      upper(data.at("series-line", default: "")))

    #v(1fr)

    #block(width: 100%, text(size: 30pt, lang: if pali-first { "pi" } else { "en" },
      data.title))

    #v(6mm)
    #box(width: 45%, grid(
      columns: (1fr, auto, 1fr),
      column-gutter: 2.5mm,
      align: horizon,
      line(length: 100%, stroke: 0.8pt + accent),
      text(size: 9pt, fill: accent)[◆],
      line(length: 100%, stroke: 0.8pt + accent),
    ))
    #v(5mm)

    #if data.at("subtitle", default: "") != "" {
      block(width: 100%, text(size: 16pt,
        style: if pali-first { "normal" } else { "italic" },
        lang: if pali-first { "en" } else { "pi" },
        data.subtitle))
    }

    #v(1.4fr)

    #box(width: 100%, line(length: 100%, stroke: 0.4pt + accent))
  ]
}

#if "cover-data" in sys.inputs {
  set document(title: json(sys.inputs.at("cover-data")).title)
  cover-page(json(sys.inputs.at("cover-data")))
}
