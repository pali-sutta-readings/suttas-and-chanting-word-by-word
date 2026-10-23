"""The PDF pipeline on a fixture book in parts: assemble.py, then pandoc with
templates/pandoc/chant.lua and book.typst, then typst. Skipped when pandoc
or typst is not installed."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import assemble
from chantlib import books

FIXTURES = Path(__file__).resolve().parent / "fixtures"

METADATA = """title: "Test Chants"
subtitle: "Pariyatti-pāṭha"
lang: en-GB
pali-title-first: false
series-line: "Pāli with word-by-word English"
texts:
  - folder: 01_one
    heading: "Part One"
  - folder: 02_two
    heading: "Part Two"
sources:
  - "Source One"
rights: "Free distribution only."
cover-image: ""
about: 00_about.md
author: ""
publisher: ""
"""


@unittest.skipUnless(shutil.which("pandoc") and shutil.which("typst"), "needs pandoc and typst")
class PdfTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # A scratch typst root with the templates, the cover data and the
        # assembled book at the paths that book.typst expects.
        cls.tmp = Path(tempfile.mkdtemp())
        bks = cls.tmp / "books"
        for folder, fixture in (("01_one", "good.md"), ("02_two", "good-vinaya.md")):
            (bks / "test" / folder).mkdir(parents=True)
            shutil.copy(FIXTURES / fixture, bks / "test" / folder / "01_text.md")
        (bks / "test" / "metadata.txt").write_text(METADATA)
        (bks / "test" / "00_about.md").write_text(
            "# About This Book {.unnumbered}\n\n## Licence {.unnumbered .unlisted}\n\n*Built {today}.*\n")
        shutil.copytree(ROOT / "templates", cls.tmp / "templates")
        covers = cls.tmp / "build" / "covers"
        covers.mkdir(parents=True)
        (covers / "test.json").write_text(json.dumps(
            assemble.cover_data(books.load_book("test", bks)), ensure_ascii=False))
        out = cls.tmp / "build" / "tmp"
        assemble.assemble("test", out, bks, covers, today="2026-01-02")
        cls.typ = out / "test.typ"
        subprocess.run(
            ["pandoc", "--defaults", str(out / "test.pandoc.json"), "-t", "typst",
             "--template", str(cls.tmp / "templates/pandoc/book.typst"),
             "--lua-filter", str(cls.tmp / "templates/pandoc/chant.lua"),
             "-o", str(cls.typ)],
            check=True, cwd=cls.tmp)
        cls.src = cls.typ.read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_divs_become_function_calls(self):
        for call in ("#unit[", "#unit-head[", "#pali[", "#literal[", "#faithful[",
                     "#en-title[", "#citation[", "#instruction["):
            self.assertIn(call, self.src)
        self.assertNotIn("#block[", self.src)
        self.assertNotIn("#figure(", self.src)

    def test_word_table(self):
        self.assertIn("#word-table(", self.src)
        self.assertIn("header: ([Word], [Analysis & Meaning],)", self.src)
        # Tag groups are styled text, words are plain bold: no raw text left.
        self.assertIn("#tags[", self.src)
        body = self.src[self.src.index("#counter(page).update(1)"):]
        self.assertNotIn("`", body)
        # Member rows keep their ↳ and are flagged.
        self.assertRegex(self.src, r"\(\[↳ #strong\[[^]]+\]\], \[.*\], true\),")
        self.assertRegex(self.src, r"\(\[#strong\[[^]]+\]\], \[.*\], false\),")

    def test_titles_and_contents(self):
        self.assertIn("#toc-en[", self.src)
        self.assertNotIn(" #toc-en[", self.src)
        self.assertIn('#let book = json("/build/covers/test.json")', self.src)
        self.assertIn("chant-level: 2,", self.src)
        self.assertIn('lang: "en",', self.src)
        self.assertIn('region: "GB",', self.src)
        # The contents page comes after the About text, before the first part.
        about = self.src.index("[About This Book]")
        contents = self.src.index("#contents-page(depth: 2)")
        part = self.src.index("= Part One")
        self.assertLess(about, contents)
        self.assertLess(contents, part)

    def test_typst_compiles(self):
        pdf = self.tmp / "test.pdf"
        r = subprocess.run(
            ["typst", "compile", "--root", str(self.tmp), "--font-path", str(ROOT / "fonts"),
             "--ignore-system-fonts", str(self.typ), str(pdf)],
            capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("warning", r.stderr)
        self.assertTrue(pdf.read_bytes().startswith(b"%PDF"))

    def test_cover_compiles_standalone(self):
        png = self.tmp / "cover.png"
        r = subprocess.run(
            ["typst", "compile", "--root", str(self.tmp), "--font-path", str(ROOT / "fonts"),
             "--ignore-system-fonts", "--input", "cover-data=/build/covers/test.json",
             "--format", "png", "--ppi", "30",
             str(self.tmp / "templates/typst/cover.typ"), str(png)],
            capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(png.read_bytes().startswith(b"\x89PNG"))


if __name__ == "__main__":
    unittest.main()
