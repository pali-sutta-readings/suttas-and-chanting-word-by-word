#!/usr/bin/env python3
"""Rebuild the guide's flashcard figures as high-resolution PNGs.

The author's screenshots in the Word original are 96-dpi screen captures.
At the sizes this book prints them they work out at 154-186 ppi, which is
soft on paper and worse on screen. Upscaling adds no detail, so this
script redraws the same cards instead: white card, green (or navy) border,
red dot, and black sans-serif text with the author's bold and underline
emphasis. Positions are in the source screenshots' pixels; the images are
drawn SCALE times larger, which brings them to 460-760 ppi at the widths
they print in the PDF and EPUB (2.8 in for single cards, 4.61 in for
spreads).

The typeface is Noto Sans, the house sans (fonts/Noto_Sans/), which is
close to the Segoe UI of the original screenshots.

Needs Pillow:  python3 -m pip install pillow
Run from the repo root:

    python3 books/11_learning_the_word_by_word_meaning/images/make_figures.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
IMAGES = Path(__file__).resolve().parent
FONT_DIR = ROOT / "fonts" / "Noto_Sans"

SCALE = 3  # output pixels per source pixel: 3 x 96 dpi = 288 dpi source scale

GREEN = (78, 167, 46)  # #4EA72E, the Word green of the card borders
LIGHT_GREEN = (147, 196, 125)  # #93C47D, the lighter border of figure 07
NAVY = (4, 36, 51)  # #042433, the dot outline and figure 03's borders
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FONT_SIZE = 34  # the large cards, in source pixels
FONT_SIZE_07 = 21  # figure 07 is a smaller screenshot

# Run kinds for a line: "t" regular, "b" bold, "u" underline,
# "bu" bold + underline, "blank" an underlined blank of a given width,
# "gap" an exact width of white space.
FIGURES = {
    "01": dict(
        size=(521, 342),
        cards=[(0, 0, 520, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[("c", 215, 158, 302, 182, [("t", "Yathā")])],
    ),
    "02": dict(
        size=(520, 342),
        cards=[(0, 0, 519, 341, GREEN, 3)],
        dots=[],
        lines=[("c", 205, 158, 311, 182, [("t", "Just as")])],
    ),
    "03": dict(
        size=(839, 241),
        cards=[
            (0, 0, 365, 240, NAVY, 3),
            (474, 0, 838, 240, NAVY, 3),
        ],
        dots=[(26, 25, 40, 38, NAVY, 4)],
        lines=[
            ("c", 128, 107, 234, 132, [("t", "Just as")]),
            ("c", 614, 107, 701, 132, [("t", "Yathā")]),
        ],
    ),
    "04": dict(
        size=(1160, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1159, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("l", 94, 135, 423, 166,
             [("bu", "Yathā"), ("t", " vāri-vahā pūrā")]),
            ("l", 101, 180, 418, 211, [("t", "paripūrenti sāgaraṁ")]),
            ("l", 694, 135, 1102, 162,
             [("bu", "Just as"), ("t", " rivers full of water")]),
            ("l", 709, 180, 1089, 211, [("t", "entirely fill up the ocean")]),
        ],
    ),
    "05": dict(
        size=(1160, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1159, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("l", 55, 135, 462, 162,
             [("bu", "Just as"), ("t", " rivers full of water")]),
            ("l", 69, 180, 449, 211, [("t", "entirely fill up the ocean")]),
            ("l", 733, 135, 1062, 166,
             [("bu", "Yathā"), ("t", " vāri-vahā pūrā")]),
            ("l", 741, 180, 1057, 211, [("t", "paripūrenti sāgaraṁ")]),
        ],
    ),
    "06": dict(
        size=(1160, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1159, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("l", 107, 90, 410, 121,
             [("blank", 69), ("gap", 9), ("t", "vāri-vahā pūrā")]),
            ("l", 101, 135, 418, 166, [("t", "paripūrenti sāgaraṁ")]),
            ("c", 197, 225, 322, 256, [("t", "(Just as)")]),
            ("c", 850, 90, 946, 117, [("bu", "Yathā")]),
            ("l", 694, 180, 1102, 207,
             [("bu", "Just as"), ("t", " rivers full of water")]),
            ("l", 709, 225, 1089, 256, [("t", "entirely fill up the ocean")]),
        ],
    ),
    "07": dict(
        size=(709, 247),
        cards=[
            (5, 5, 321, 240, LIGHT_GREEN, 3),
            (389, 5, 705, 240, LIGHT_GREEN, 3),
        ],
        dots=[(29, 22, 31, 32, BLACK, 1)],
        lines=[
            ("l", 52, 109, 272, 129,
             [("blank", 61), ("gap", 8), ("t", "rivers, when full,")]),
            ("l", 48, 138, 277, 159, [("t", "entirely fill up the ocean")]),
            ("c", 510, 54, 584, 72, [("bu", "Just as")]),
            ("l", 445, 112, 647, 132,
             [("bu", "Yathā"), ("t", " vāri-vahā pūrā")]),
            ("l", 452, 141, 642, 162, [("t", "paripūrenti sāgaraṁ")]),
        ],
    ),
    "08": dict(
        size=(1161, 771),
        cards=[
            (0, 0, 520, 341, GREEN, 3),
            (640, 0, 1160, 341, GREEN, 3),
            (0, 429, 520, 770, GREEN, 3),
            (640, 429, 1160, 770, GREEN, 3),
        ],
        dots=[(33, 39, 46, 53, NAVY, 4), (33, 468, 46, 53, NAVY, 4)],
        lines=[
            ("c", 193, 158, 328, 189,
             [("t", "sāgar"), ("u", "a"), ("bu", "ṁ")]),
            ("c", 798, 158, 998, 185,
             [("bu", "to"), ("t", " the ocean")]),
            ("c", 158, 587, 359, 614,
             [("bu", "to"), ("t", " the ocean")]),
            ("c", 832, 587, 968, 618,
             [("t", "sāgar"), ("u", "a"), ("bu", "ṁ")]),
        ],
    ),
    "09": dict(
        size=(1161, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1160, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("c", 97, 91, 421, 122, [("t", "Yathā vāri-vahā pūrā")]),
            ("c", 145, 136, 378, 167,
             [("t", "paripūrenti"), ("gap", 11), ("blank", 52)]),
            ("c", 147, 226, 370, 257,
             [("u", "("), ("bu", "to"), ("t", " the ocean)")]),
            ("c", 832, 158, 966, 189,
             [("t", "sāgar"), ("u", "a"), ("bu", "ṁ")]),
        ],
    ),
    "10": dict(
        size=(1161, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1160, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("c", 97, 91, 421, 122, [("t", "Yathā vāri-vahā pūrā")]),
            ("c", 145, 136, 378, 167,
             [("t", "paripūrenti"), ("gap", 11), ("blank", 52)]),
            ("c", 147, 226, 370, 257,
             [("u", "("), ("bu", "to"), ("t", " the ocean)")]),
            ("c", 832, 113, 966, 144,
             [("t", "sāgar"), ("u", "a"), ("bu", "ṁ")]),
            ("c", 802, 203, 996, 234, [("t", "(accusative)")]),
        ],
    ),
    "11": dict(
        size=(1161, 764),
        cards=[
            (0, 0, 520, 341, GREEN, 3),
            (640, 0, 1160, 341, GREEN, 3),
            (0, 422, 520, 763, GREEN, 3),
            (640, 422, 1160, 763, GREEN, 3),
        ],
        dots=[(33, 39, 46, 53, NAVY, 4), (33, 461, 46, 53, NAVY, 4)],
        lines=[
            ("c", 171, 158, 350, 189,
             [("t", "paripūre"), ("u", "n"), ("bu", "ti")]),
            ("c", 740, 158, 1057, 189,
             [("bu", "(they)"), ("t", " entirely fill up")]),
            ("c", 100, 580, 418, 611,
             [("bu", "(they)"), ("t", " entirely fill up")]),
            ("c", 811, 580, 990, 611,
             [("t", "paripūre"), ("u", "n"), ("bu", "ti")]),
        ],
    ),
    "12": dict(
        size=(1161, 342),
        cards=[(0, 0, 520, 341, GREEN, 3), (640, 0, 1160, 341, GREEN, 3)],
        dots=[(33, 39, 46, 53, NAVY, 4)],
        lines=[
            ("c", 171, 113, 350, 144,
             [("t", "paripūre"), ("u", "n"), ("bu", "ti")]),
            ("c", 180, 203, 337, 235, [("u", "("), ("t", "sāgaraṁ)")]),
            ("c", 740, 113, 1057, 144,
             [("bu", "(they)"), ("t", " entirely fill up")]),
            ("c", 810, 203, 989, 234, [("t", "(the ocean)")]),
        ],
    ),
    "13": dict(
        size=(1161, 764),
        cards=[
            (0, 0, 520, 341, GREEN, 3),
            (640, 0, 1160, 341, GREEN, 3),
            (0, 422, 520, 763, GREEN, 3),
            (640, 422, 1160, 763, GREEN, 3),
        ],
        dots=[(33, 39, 46, 53, NAVY, 4), (33, 461, 46, 53, NAVY, 4)],
        lines=[
            ("l", 97, 136, 421, 167, [("t", "Yathā vāri-vahā pūrā")]),
            ("l", 95, 181, 424, 212,
             [("b", "paripūrenti"), ("t", " sāgaraṁ")]),
            ("l", 698, 136, 1099, 160,
             [("t", "Just as rivers full of water")]),
            ("l", 700, 181, 1097, 212,
             [("b", "entirely fill up"), ("t", " the ocean")]),
            ("l", 59, 557, 460, 582,
             [("t", "Just as rivers full of water")]),
            ("l", 60, 602, 458, 633,
             [("b", "entirely fill up"), ("t", " the ocean")]),
            ("l", 736, 557, 1060, 588, [("t", "Yathā vāri-vahā pūrā")]),
            ("l", 734, 602, 1064, 633,
             [("b", "paripūrenti"), ("t", " sāgaraṁ")]),
        ],
    ),
}


def font(bold, size):
    name = "NotoSans-Bold.ttf" if bold else "NotoSans-Regular.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), max(1, round(size * SCALE)))


def line_mask(runs, size):
    """Draw one line of text into an 'L' mask, cropped to its ink."""
    reg, bold = font(False, size), font(True, size)
    ascent, descent = reg.getmetrics()
    pad = 4 * SCALE

    widths = []
    for kind, value in runs:
        if kind in ("blank", "gap"):
            widths.append(value * SCALE)
        else:
            widths.append(
                (bold if kind in ("b", "bu") else reg).getlength(value))

    width = int(round(sum(widths))) + 2 * pad
    height = ascent + descent + 2 * pad
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)

    baseline = pad + ascent
    x = float(pad)
    for (kind, value), run_width in zip(runs, widths):
        if kind in ("blank", "u", "bu"):
            draw.rectangle(
                [round(x), baseline + 2 * SCALE,
                 round(x + run_width) - 1, baseline + 2 * SCALE + SCALE - 1],
                fill=255)
        if kind not in ("blank", "gap"):
            draw.text((x, baseline), value,
                      font=bold if kind in ("b", "bu") else reg,
                      fill=255, anchor="ls")
        x += run_width
    return mask.crop(mask.getbbox())


def dot_patch(width, height, colour, stroke_width):
    """An anti-aliased circle, drawn large and reduced."""
    ss = 8
    big = Image.new("RGB", (width * ss, height * ss), WHITE)
    draw = ImageDraw.Draw(big)
    draw.ellipse([0, 0, width * ss - 1, height * ss - 1],
                 fill=RED, outline=colour, width=stroke_width * ss)
    return big.resize((width, height), Image.LANCZOS)


def render(name):
    spec = FIGURES[name]
    width_in = 2.8 if name in ("01", "02") else 4.61
    w, h = spec["size"]
    page = Image.new("RGB", (w * SCALE, h * SCALE), WHITE)
    draw = ImageDraw.Draw(page)

    for x0, y0, x1, y1, colour, width in spec["cards"]:
        draw.rectangle([x0 * SCALE, y0 * SCALE, x1 * SCALE, y1 * SCALE],
                       outline=colour, width=width * SCALE)

    for x, y, dw, dh, colour, stroke in spec["dots"]:
        page.paste(dot_patch(dw * SCALE, dh * SCALE, colour, stroke),
                   (x * SCALE, y * SCALE))

    size = FONT_SIZE_07 if name == "07" else FONT_SIZE
    for align, x0, y0, x1, y1, runs in spec["lines"]:
        mask = line_mask(runs, size)
        if align == "c":
            x = round((x0 + x1) / 2 * SCALE - mask.width / 2)
        else:
            x = x0 * SCALE
        y = round((y0 + y1) / 2 * SCALE - mask.height / 2)
        page.paste(BLACK, (x, y), mask)

    out = IMAGES / f"{name}.png"
    page.save(out, optimize=True)
    return out, page.size, page.width / width_in


def main():
    for name in FIGURES:
        out, size, ppi = render(name)
        print(f"{out.name}: {size[0]}x{size[1]} px, {ppi:.0f} ppi at its "
              f"printed width ({SCALE}x the source screenshot)")


if __name__ == "__main__":
    main()
