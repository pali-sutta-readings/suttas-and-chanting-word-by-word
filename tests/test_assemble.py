import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import assemble
from chantlib import books
from chantlib.books import MetadataError

FIXTURES = Path(__file__).resolve().parent / "fixtures"

METADATA = """title: "Test Chants"
subtitle: "Pariyatti-pāṭha"
lang: en-GB
pali-title-first: false
texts:
{texts}
sources:
  - "Source One"
  - "Source Two"
rights: "Free distribution only."
cover-image: ""
about: about.md
author: ""
publisher: ""
"""


class AssembleTest(unittest.TestCase):
    """Assemble fixture books from a temporary books/ and texts/ tree."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.books = self.tmp / "books"
        self.texts = self.tmp / "texts"
        self.out = self.tmp / "out"
        self.covers = self.tmp / "covers"
        for folder, fixture in (("01_one", "good.md"), ("02_two", "good-vinaya.md")):
            d = self.texts / folder
            d.mkdir(parents=True)
            shutil.copy(FIXTURES / fixture, d / "01_text.md")
            (d / "CHANGELOG.md").write_text("# Changelog\n\nCHANGELOG-MARKER\n")
            (d / "00_original_x.md").write_text("ORIGINAL-MARKER\n")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def make_book(self, name, texts, **extra):
        d = self.books / name
        d.mkdir(parents=True)
        meta = METADATA.format(texts=texts)
        for k, v in extra.items():
            meta = re.sub(rf"^{k}: .*$", f"{k}: {v}", meta, flags=re.M)
        (d / "metadata.txt").write_text(meta)
        (d / "about.md").write_text("# About This Book {.unnumbered}\n\n*Built {today}.*\n")

    def run_assemble(self, name):
        md = assemble.assemble(name, self.out, self.books, self.texts,
                               self.covers, today="2026-01-02")
        meta = json.loads((self.out / f"{name}.meta.yaml").read_text())
        defaults = json.loads((self.out / f"{name}.pandoc.yaml").read_text())
        return md.read_text(), meta, defaults

    def test_single_folder_book(self):
        self.make_book("one", "  - 01_one")
        md, _, defaults = self.run_assemble("one")
        self.assertTrue(md.startswith("# About This Book {.unnumbered}"))
        self.assertIn("*Built 2026-01-02.*", md)
        self.assertIn("# Pubbabhāga-namakāra [— Preliminary Homage]{.toc-en}\n", md)
        self.assertNotIn("CHANGELOG-MARKER", md)
        self.assertNotIn("ORIGINAL-MARKER", md)
        # Divs in unit order: Pāli, Literal, Faithful, then the table.
        order = [md.index(s) for s in (
            "::: subtitle", "::: unit", '::: {.pali lang="pi"}\nHanda mayaṁ',
            "::: literal\n**Literal:**", "::: faithful\n**Faithful:**",
            "| Word | Analysis & Meaning |")]
        self.assertEqual(order, sorted(order))
        self.assertIn("::: citation", md)
        # Every fenced div is closed.
        opens = len(re.findall(r"^::: \S", md, re.M))
        closes = len(re.findall(r"^:::$", md, re.M))
        self.assertEqual(opens, closes)
        self.assertEqual(defaults["toc-depth"], 1)
        self.assertEqual(defaults["split-level"], 1)

    def test_metadata_drops_empty_keys(self):
        self.make_book("one", "  - 01_one")
        _, meta, _ = self.run_assemble("one")
        self.assertEqual(meta["title"], [
            {"type": "main", "text": "Test Chants"},
            {"type": "subtitle", "text": "Pariyatti-pāṭha"},
        ])
        self.assertEqual(meta["source"], "Source One; Source Two")
        self.assertEqual(meta["lang"], "en-GB")
        for key in ("author", "publisher", "cover-image"):
            self.assertNotIn(key, meta)

    def test_pdf_metadata_keys(self):
        self.make_book("one", "  - 01_one")
        _, meta, _ = self.run_assemble("one")
        self.assertEqual(meta["book-id"], "one")
        self.assertNotIn("cover-pdf", meta)

    def test_cover_override_for_pdf(self):
        self.make_book("one", "  - 01_one", **{"cover-image": "cover.jpg"})
        _, meta, _ = self.run_assemble("one")
        self.assertEqual(meta["cover-image"], str(self.books / "one" / "cover.jpg"))
        self.assertTrue(meta["cover-pdf"].endswith("one/cover.jpg"))

    def test_cover_data(self):
        self.make_book("one", "  - 01_one", **{"pali-title-first": "true"})
        data = assemble.cover_data(books.load_book("one", self.books))
        self.assertEqual(data, {
            "title": "Test Chants",
            "subtitle": "Pariyatti-pāṭha",
            "pali-title-first": True,
            "series-line": "",
            "accent": "",
        })

    def test_generated_cover_used_when_built(self):
        self.make_book("one", "  - 01_one")
        self.covers.mkdir()
        (self.covers / "one.png").write_bytes(b"")
        _, meta, _ = self.run_assemble("one")
        self.assertEqual(meta["cover-image"], str(self.covers / "one.png"))

    def test_book_in_parts(self):
        self.make_book("parts", "\n".join([
            "  - folder: 01_one", '    heading: "Part One"',
            "  - folder: 02_two", '    heading: "Part Two"',
        ]))
        md, _, defaults = self.run_assemble("parts")
        self.assertLess(md.index("# Part One\n"), md.index("## Pubbabhāga-namakāra"))
        self.assertLess(md.index("## Pubbabhāga-namakāra"), md.index("# Part Two\n"))
        self.assertIn("::: instruction\n", md)
        self.assertNotIn("\n> ", md)
        self.assertEqual(defaults["toc-depth"], 2)

    def test_missing_key_is_an_error(self):
        self.make_book("one", "  - 01_one")
        meta = self.books / "one" / "metadata.txt"
        meta.write_text(re.sub(r"^rights: .*\n", "", meta.read_text(), flags=re.M))
        with self.assertRaisesRegex(MetadataError, "missing keys: rights"):
            books.load_book("one", self.books)

    def test_book_files_skip_changelog_and_originals(self):
        self.make_book("one", "  - 01_one")
        book = books.load_book("one", self.books)
        [(part, files)] = books.book_files(book, self.texts)
        self.assertEqual([f.name for f in files], ["01_text.md"])
        self.assertIsNone(part.heading)

    def test_real_books_load(self):
        ids = books.list_books()
        self.assertEqual(len(ids), 13)
        for b in ids:
            book = books.load_book(b)
            for _, files in books.book_files(book):
                self.assertTrue(files, f"{b}: no text files")


if __name__ == "__main__":
    unittest.main()
