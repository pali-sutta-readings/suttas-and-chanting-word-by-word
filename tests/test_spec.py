import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from chantlib.spec import SpecError, load_spec, read_blocks


class StyleSpecTest(unittest.TestCase):
    """The real docs/style-spec.md has the blocks the checks rely on."""

    @classmethod
    def setUpClass(cls):
        cls.spec = load_spec()

    def test_tags(self):
        tags = self.spec["tags"]
        self.assertEqual(len(tags), 47)
        self.assertEqual(len(set(tags)), 47)
        for tag in ("masc", "comp", "imperat", "1st", "sandhi"):
            self.assertIn(tag, tags)

    def test_other_blocks_present(self):
        self.assertIn("(Optional)", self.spec["rubrics"])
        self.assertIn("(For the living)", self.spec["rubrics"])
        self.assertIn("the", self.spec["english-stopwords"])
        self.assertEqual(
            self.spec["repeat-note"],
            "Word analysis as at the first occurrence of this line.",
        )

    def test_example_blocks_are_not_rules(self):
        # The ```text layout examples contain table rows; none may leak in.
        for name in ("tags", "rubrics", "english-stopwords"):
            for entry in self.spec[name]:
                self.assertNotIn("|", entry)


class ReadBlocksTest(unittest.TestCase):
    def test_blocks_and_comments(self):
        text = "intro\n```tags\nmasc\n# comment\n\nfem\n```\n```repeat-note\nNote.\n```\n"
        self.assertEqual(read_blocks(text)["tags"], ["masc", "# comment", "", "fem"])

    def test_unclosed_block(self):
        with self.assertRaises(SpecError):
            read_blocks("```tags\nmasc\n")

    def test_missing_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "spec.md"
            path.write_text("```tags\nmasc\n```\n", encoding="utf-8")
            with self.assertRaisesRegex(SpecError, "rubrics"):
                load_spec(path)

    def test_missing_file(self):
        with self.assertRaisesRegex(SpecError, "not found"):
            load_spec("/nonexistent/style-spec.md")


if __name__ == "__main__":
    unittest.main()
