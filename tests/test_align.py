import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import align

ROWS = """# Test

*Test*

**Bhagavā sāvako no**

**Literal:** x
**Faithful:** x.

| Word | Analysis & Meaning |
| :--- | :--- |
| **`bhagavā`** | `(masc nom sg)` [cf. √bhaj + a + vant] the Blessed One; **[√bhaj + a + vant]** |
| **`sāvako`** | `(masc nom sg)` disciple, from √bhaj + a + vant (sic); **[√su + aka]** |
| **`no`** | `(ind)` not; **[na + u]** |
| **`anuttaro`** | `(masc nom sg)` unsurpassed; **[na + ud + tara]** |
"""


class AlignTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.tree = self.tmp / "texts"
        self.tree.mkdir()
        self.file = self.tree / "01_test.md"
        self.file.write_text(ROWS, encoding="utf-8")
        (self.tree / "CHANGELOG.md").write_text("√bhaj + a + vant\n", encoding="utf-8")

    def rules(self, rules):
        p = self.tmp / "rules.json"
        p.write_text(json.dumps(rules, ensure_ascii=False), encoding="utf-8")
        return p

    def run_main(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = align.main([str(a) for a in args])
        return code, out.getvalue()

    def test_cell_match_only_in_named_cell(self):
        rules = self.rules([{"word": ".", "old": "√bhaj + a + vant", "new": "√bhaj > bhag + a + vant"}])
        self.run_main(self.tree, rules, self.tmp / "log.json", "--apply")
        text = self.file.read_text(encoding="utf-8")
        self.assertIn("**[√bhaj > bhag + a + vant]**", text)
        self.assertIn("[cf. √bhaj + a + vant] the Blessed One", text)       # note untouched
        self.assertIn("disciple, from √bhaj + a + vant (sic)", text)      # meaning untouched
        self.assertEqual((self.tree / "CHANGELOG.md").read_text(encoding="utf-8"), "√bhaj + a + vant\n")

    def test_dry_run_writes_nothing(self):
        rules = self.rules([{"word": "bhagav", "old": "√bhaj + a + vant", "new": "√bhaj > bhag + a + vant"}])
        code, out = self.run_main(self.tree, rules, self.tmp / "log.json")
        self.assertEqual(code, 0)
        self.assertIn("+| **`bhagavā`**", out)
        self.assertIn("1 changes in 1 files; 0 cells already aligned (dry run, nothing written)", out)
        self.assertEqual(self.file.read_text(encoding="utf-8"), ROWS)
        self.assertFalse((self.tmp / "log.json").exists())

    def test_whole_cell_needed_by_default(self):
        rules = self.rules([{"word": ".", "old": "na + u", "new": "na + u > no"},
                            {"word": ".", "old": "ud + tara", "new": "x"}])
        self.run_main(self.tree, rules, self.tmp / "log.json", "--apply")
        text = self.file.read_text(encoding="utf-8")
        self.assertIn("**[na + u > no]**", text)
        self.assertIn("**[na + ud + tara]**", text)     # part of the cell only: no match

    def test_substring_rules_are_safe_to_rerun(self):
        rules = self.rules([{"word": "`no`", "old": "na + u", "new": "na + u > no", "match": "substring"}])
        self.run_main(self.tree, rules, self.tmp / "log.json", "--apply")
        once = self.file.read_text(encoding="utf-8")
        self.assertIn("**[na + u > no]**", once)
        _, out = self.run_main(self.tree, rules, self.tmp / "log2.json", "--apply")
        self.assertEqual(self.file.read_text(encoding="utf-8"), once)
        self.assertIn("0 changes in 0 files; 1 cells already aligned", out)

    def test_tags_cell(self):
        rules = self.rules([{"word": "`anuttaro`", "cell": "tags", "old": "masc nom sg", "new": "adj masc nom sg"}])
        self.run_main(self.tree, rules, self.tmp / "log.json", "--apply")
        text = self.file.read_text(encoding="utf-8")
        self.assertIn("| **`anuttaro`** | `(adj masc nom sg)` unsurpassed;", text)
        self.assertIn("| **`sāvako`** | `(masc nom sg)` disciple", text)

    def test_meaning_cell(self):
        rules = self.rules([{"word": "`no`", "cell": "meaning", "old": "not", "new": "not, no"}])
        self.run_main(self.tree, rules, self.tmp / "log.json", "--apply")
        self.assertIn("`(ind)` not, no; **[na + u]**", self.file.read_text(encoding="utf-8"))

    def test_log_and_changelog(self):
        rules = self.rules([{"word": "bhagav", "old": "√bhaj + a + vant", "new": "√bhaj > bhag + a + vant",
                             "why": "DPD construction of bhagavant", "ref": "DPD bhagavant 1"}])
        log = self.tmp / "log.json"
        self.run_main(self.tree, rules, log, "--apply")
        entries = json.loads(log.read_text(encoding="utf-8"))
        self.assertEqual([(e["line"], e["word"], e["old"]) for e in entries], [(12, "bhagavā", "√bhaj + a + vant")])
        _, out = self.run_main("--changelog", log)
        self.assertEqual(out, "### 01_test.md\n| Line | Was | Now | Why | Reference |\n| :--- | :--- | :--- | :--- | :--- |\n"
                              "| 12 | *bhagavā* √bhaj + a + vant | √bhaj > bhag + a + vant | DPD construction of bhagavant | DPD bhagavant 1 |\n")

    def test_bad_rule(self):
        with self.assertRaisesRegex(align.RuleError, "cell must be one of"):
            align.load_rules(self.rules([{"word": "x", "old": "a", "new": "b", "cell": "ety"}]))


if __name__ == "__main__":
    unittest.main()
