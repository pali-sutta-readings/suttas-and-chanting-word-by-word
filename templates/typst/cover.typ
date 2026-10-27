// The generated A5 book cover (docs/book-build.md). Its data is
// build/covers/<book>.json, written by `scripts/assemble.py --cover-data`
// from books/<book>/metadata.txt.
//
// Compiled on its own, it renders the cover of the book named by the
// cover-data input (the EPUB cover PNG):
//
//   typst compile --root . --font-path fonts --ignore-system-fonts \
//     --input cover-data=/build/covers/<book>.json \
//     templates/typst/cover.typ build/covers/<book>.png --format png --ppi 300
//
// The PDF imports cover-page() for its first page.
//
// The design is the title page of the Pāli Sutta Readings videos
// (pali-sutta-readings.github.io): a dark page with a faint Dhamma wheel, and
// a green band across its middle with the title in Abhaya Libre X.

#import "style.typ": document-style

#let default-accent = "#16423c"
#let page-fill = rgb("#282d3f")
#let text-fill = luma(95%)

// data: title, subtitle, pali-title-first, series-line, accent (may be ""),
// site-url (printed under the series line).
// The Pāli one of title and subtitle is the title when pali-title-first is
// true, else the subtitle; the Pāli subtitle is set in italic. The accent is
// the colour of the band.
#let cover-page(data) = {
  let accent = rgb(if data.at("accent", default: "") != "" { data.accent } else { default-accent })
  let pali-first = data.at("pali-title-first", default: false)
  let title-font = ("Abhaya Libre X", ..document-style.fonts.body)
  let title-size = data.at("title-size", default: 30) * 1pt
  let sans = document-style.fonts.sans

  // The wheel and the band are both centred on the page, so the title sits
  // across the middle of the wheel.
  page(paper: "a5", margin: 0pt, header: none, footer: none, numbering: none,
       fill: page-fill,
       background: place(center + horizon,
         image("assets/dhamma-wheel-white-5.png", width: 125%)))[
    #set par(justify: false)
    #set align(center)
    #set text(font: sans, fill: text-fill)

    #place(center + horizon,
      block(width: 100%, inset: (x: 12mm, y: 11mm),
            fill: accent.transparentize(10%),
            stroke: (y: 0.5pt + luma(35%)))[
        #block(text(font: title-font, size: title-size, weight: "bold",
          lang: if pali-first { "pi" } else { "en" }, data.title))

        #if data.at("subtitle", default: "") != "" {
          v(2mm)
          block(text(size: 13pt,
            style: if pali-first { "normal" } else { "italic" },
            lang: if pali-first { "en" } else { "pi" },
            data.subtitle))
        }
      ])

    #place(bottom + center, dy: -12mm, stack(spacing: 3mm,
      text(size: 8.5pt, tracking: 0.12em, fill: text-fill,
        upper(data.at("series-line", default: ""))),
      text(size: 8pt, fill: text-fill, data.at("site-url", default: ""))))
  ]
}

#if "cover-data" in sys.inputs {
  set document(title: json(sys.inputs.at("cover-data")).title)
  cover-page(json(sys.inputs.at("cover-data")))
}
