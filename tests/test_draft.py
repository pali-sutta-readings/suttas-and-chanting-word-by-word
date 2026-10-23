import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import draft
from chantlib.books import DEFAULT_OPTIONS

FIXTURES = Path(__file__).resolve().parent / "fixtures"
DN22_OPTIONS = dict(DEFAULT_OPTIONS, **{
    "heading-gloss": True, "heading-numbers": True, "repeat-across-files": True,
})

SOURCE = """# Namo

*Homage*

**Namo tassa bhagavato arahato sammāsambuddhassa (×3)**

**Literal:** Homage to-him, [the] Blessed One
**Faithful:** Homage to the Blessed One.

| Word | Analysis & Meaning |
| :--- | :--- |
| **`namo`** | `(ind)` homage; **[namo]** |

**Buddhaṁ saraṇaṁ gacchāmi**

**Literal:** [The] Buddha [as] refuge I go [to]
**Faithful:** I go to the Buddha for refuge.

*Word analysis as at the first occurrence of this line.*
"""


class RoundTrip(unittest.TestCase):
    def check(self, name, options=None):
        path = FIXTURES / name
        d = draft.extract(path, options if options is not None else DEFAULT_OPTIONS)
        self.assertEqual(draft.build(d), path.read_text(encoding="utf-8"))

    def test_good(self):
        self.check("good.md")

    def test_good_vinaya(self):
        self.check("good-vinaya.md")

    def test_good_dn22(self):
        self.check("good-dn22.md", DN22_OPTIONS)

    def test_layout_difference_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "01_x.md"
            p.write_text((FIXTURES / "good.md").read_text(encoding="utf-8").rstrip("\n"), encoding="utf-8")
            with self.assertRaisesRegex(draft.DraftError, "layout differs"):
                draft.extract(p, DEFAULT_OPTIONS)


class Build(unittest.TestCase):
    def test_rows_and_repeat(self):
        text = draft.build("\n".join([
            "T|Namo", "E|Homage",
            "P|Namo tassa", "L|Homage to him", "F|Homage to him.",
            "R|namo|ind|homage|namo", "M|tassa|dem pron masc dat sg|[agrees with *bhagavato*] to him|ta",
            "P|Namo tassa", "L|Homage to him", "F|Homage to him.",
            "P!|Namo tassa", "L|a", "F|b", "T0|",
            "P~|Buddho", "L|c", "F|d",
        ]))
        self.assertIn("| ↳ **`tassa`** | `(dem pron masc dat sg)` [agrees with *bhagavato*] to him; **[ta]** |", text)
        self.assertEqual(text.count("*Word analysis as at the first occurrence of this line.*"), 2)
        self.assertIn("**Literal:** a  \n**Faithful:** b  \n\n| Word | Analysis & Meaning |\n| :--- | :--- |\n", text)

    def test_variant_and_vinaya_items(self):
        text = draft.build("\n".join([
            "T|X", "E|Y", "S|Before use, say:", "P|Imaṁ pattaṁ", "L|a", "F|b", "R|imaṁ|dem pron masc acc sg|this|ima",
            "V|bowl: *imaṁ* → *etaṁ*", "R|etaṁ|dem pron masc acc sg|that|eta", "V|omit: *pattaṁ* → (omit)", "C|Kd 8:20.2",
        ]))
        self.assertIn("> Before use, say:\n\n**Imaṁ pattaṁ**", text)
        self.assertIn("**Variant:** bowl: *imaṁ* → *etaṁ*  \n\n| Word | Analysis & Meaning |", text)
        self.assertIn("**Variant:** omit: *pattaṁ* → (omit)  \n\n*Kd 8:20.2*\n", text)

    def test_unknown_item(self):
        with self.assertRaisesRegex(draft.DraftError, r"draft:1: unknown item X\|"):
            draft.build("X|y")


class Include(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)
        (self.root / "src.md").write_text(SOURCE, encoding="utf-8")

    def test_copies_the_unit_by_key(self):
        text = draft.build("T|X\nE|Y\nI|src.md|Namo tassa bhagavato arahato sammā-sambuddhassa (×3)\n"
                           "P|Namo tassa bhagavato arahato sammāsambuddhassa", root=self.root)
        self.assertIn("| **`namo`** | `(ind)` homage; **[namo]** |\n\n**Namo tassa", text)
        # The copied line counts as seen, so the next one gets the repeat note.
        self.assertTrue(text.rstrip().endswith("*Word analysis as at the first occurrence of this line.*"))

    def test_copy_stops_at_the_next_unit(self):
        text = draft.build("T|X\nE|Y\nI|src.md|Namo tassa bhagavato arahato sammāsambuddhassa", root=self.root)
        self.assertNotIn("Buddhaṁ", text)

    def test_key_not_found(self):
        with self.assertRaisesRegex(draft.DraftError, "draft:1: no unit with that Pāli line in src.md"):
            draft.build("I|src.md|Dhammaṁ saraṇaṁ gacchāmi", root=self.root)

    def test_key_found_twice(self):
        (self.root / "src.md").write_text(SOURCE + "\n" + SOURCE.split("\n\n", 2)[2], encoding="utf-8")
        with self.assertRaisesRegex(draft.DraftError, "2 units with that Pāli line"):
            draft.build("I|src.md|Buddhaṁ saraṇaṁ gacchāmi", root=self.root)


if __name__ == "__main__":
    unittest.main()
