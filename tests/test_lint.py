import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import lint
from chantlib.books import DEFAULT_OPTIONS
from chantlib.spec import load_spec

FIXTURES = Path(__file__).resolve().parent / "fixtures"
DN22_OPTIONS = dict(DEFAULT_OPTIONS, **{
    "heading-gloss": True, "heading-numbers": True, "repeat-across-files": True,
})

# Each bad fixture, the severity it must give, and a part of the message.
BAD = {
    "bad-unknown-tag": ("ERROR", "tag 'pers' not in allowed list"),
    "bad-tag-order": ("ERROR", "not in canonical nominal order"),
    "bad-coverage": ("ERROR", "do not cover the Pāli line"),
    "bad-comp-members": ("WARN", "needs a member row"),
    "bad-english": ("STRAY", "outside the allowed structure"),
    "bad-niggahita": ("ERROR", "ṃ found"),
    "bad-separator": ("STRAY", "'---' separator"),
    "bad-trailing-spaces": ("WARN", "does not end with two spaces"),
    "bad-synonym": ("ERROR", "tag 'cmpd' not in allowed list"),
}


def lint_fixture(name, options=None):
    path = FIXTURES / f"{name}.md"
    return lint.lint_text(path.read_text(encoding="utf-8"), SPEC,
                          options or DEFAULT_OPTIONS, path)


def setUpModule():
    global SPEC
    SPEC = load_spec()


class GoodFixturesTest(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(lint_fixture("good"), [])
        self.assertEqual(lint_fixture("good-vinaya"), [])
        self.assertEqual(lint_fixture("good-dn22", DN22_OPTIONS), [])

    def test_dn22_without_options(self):
        sevs = {sev for sev, _, _ in lint_fixture("good-dn22")}
        self.assertIn("STRAY", sevs)   # digits in headings, glosses as stray text


class BadFixturesTest(unittest.TestCase):
    def test_each_bad_fixture(self):
        for name, (sev, part) in BAD.items():
            with self.subTest(name):
                issues = lint_fixture(name)
                self.assertTrue(
                    any(s == sev and part in msg for s, _, msg in issues),
                    f"{name}: expected {sev} '{part}', got {issues}",
                )


class TagOrderTest(unittest.TestCase):
    def test_canonical(self):
        for grp in ("masc nom pl", "adj fem acc sg", "pp nt nom sg", "prp pass nt loc sg",
                    "3rd pl pres act indic", "3rd sg pres caus act indic",
                    "3rd sg pass mid opt", "1st sg act opt", "2nd sg dat",
                    "1st sg dat/gen", "rel pron masc nom sg", "dem pron nt acc sg",
                    "card masc nom pl", "masc nom sg comp", "adj comp", "ind",
                    "2nd pl pres act imperat comp"):
            with self.subTest(grp):
                self.assertIsNone(lint.tag_order_problem(grp))

    def test_wrong(self):
        for grp in ("nom masc sg", "masc sg nom", "pres 3rd sg act indic",
                    "3rd sg pres indic act", "2nd dat sg", "pron rel masc nom sg",
                    "comp masc nom sg"):
            with self.subTest(grp):
                self.assertIsNotNone(lint.tag_order_problem(grp))


class RepeatTest(unittest.TestCase):
    UNIT = ("**Namo tassa**\n\n**Literal:** Homage to that  \n**Faithful:** Homage to him.  \n\n")
    TABLE = ("| Word | Analysis & Meaning |\n| :--- | :--- |\n"
             "| **`namo`** | `(ind)` homage; **[√nam + as + o]** |\n"
             "| **`tassa`** | `(dem pron masc dat sg)` to him; **[ta]** |\n\n")
    NOTE = "*Word analysis as at the first occurrence of this line.*\n\n"

    def lint(self, text, options=DEFAULT_OPTIONS, path=None):
        return lint.lint_text("# Namo\n\n*Homage*\n\n" + text, SPEC, options, path)

    def test_repeat_written_out(self):
        issues = self.lint(self.UNIT + self.TABLE + self.UNIT + self.TABLE)
        self.assertEqual([(s, m[:9]) for s, _, m in issues], [("WARN", "repeat of")])

    def test_note_without_earlier_table(self):
        issues = self.lint(self.UNIT + self.NOTE)
        self.assertTrue(any("no earlier full table" in m for _, _, m in issues))

    def test_repeat_across_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "01_a.md", Path(tmp) / "02_b.md"
            first.write_text("# A\n\n*A*\n\n" + self.UNIT + self.TABLE, encoding="utf-8")
            text = self.UNIT + self.NOTE
            self.assertTrue(any("no earlier" in m for _, _, m in self.lint(text, path=second)))
            self.assertEqual(self.lint(text, DN22_OPTIONS, second), [])


class FixTest(unittest.TestCase):
    def test_safe_fixes(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ("bad-niggahita", "bad-separator", "bad-synonym"):
                path = Path(tmp) / f"{name}.md"
                shutil.copy(FIXTURES / f"{name}.md", path)
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    code = lint.main(["--fix", str(path)])
                self.assertEqual(code, 0, out.getvalue())
                self.assertIn("safe fixes applied", out.getvalue())
                self.assertEqual(path.read_text(encoding="utf-8"),
                                 (FIXTURES / "good.md").read_text(encoding="utf-8"), name)

    def test_fix_leaves_good_file_alone(self):
        good = (FIXTURES / "good.md").read_text(encoding="utf-8")
        self.assertEqual(lint.safe_fixes(good), good)

    def test_fix_tags(self):
        self.assertEqual(lint.fix_tags("masc nom sg in cmpd"), "masc nom sg comp")
        self.assertEqual(lint.fix_tags("ppp masc inst sg"), "pp masc instr sg")
        self.assertEqual(lint.fix_tags("indcl"), "ind")


if __name__ == "__main__":
    unittest.main()
