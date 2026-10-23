import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import index

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "index"
ONE = FIXTURES / "a" / "01_one.md"
TWO = FIXTURES / "b" / "01_two.md"


def files():
    return index.parsed([ONE, TWO])


class TestTagClass(unittest.TestCase):
    def test_case_and_number_left_out(self):
        self.assertEqual(index.tag_class(["masc dat sg"]), index.tag_class(["masc gen pl"]))

    def test_noun_gender_kept(self):
        self.assertEqual(index.tag_class(["fem nom sg comp"]), "comp fem")

    def test_agreeing_gender_left_out(self):
        self.assertEqual(index.tag_class(["adj masc nom sg"]), index.tag_class(["adj nt acc pl"]))
        self.assertNotEqual(index.tag_class(["masc nom sg"]), index.tag_class(["pp masc nom sg"]))

    def test_alternative_groups(self):
        self.assertEqual(index.tag_class(["masc nom pl", "fem abl sg"]), "fem / masc")


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.report = index.index_report(index.occurrences(files()), root=FIXTURES)

    def test_etymology_conflict(self):
        self.assertIn("### `bhagavā`", self.report)
        self.assertIn("- E [√bhaj + a + vant] — 1×: b/01_two.md:34", self.report)

    def test_word_class_conflict_only(self):
        self.assertIn("- T `buddho`:", self.report)
        self.assertNotIn("`buddhassa`", self.report)    # dat vs gen: set by the line

    def test_all_tags(self):
        report = index.index_report(index.occurrences(files()), all_tags=True, root=FIXTURES)
        self.assertIn("- T `buddhassa`:", report)

    def test_folder_filter(self):
        occ = index.occurrences(files())
        self.assertIn("`bhagavā`", index.index_report(occ, folder="b/", root=FIXTURES))
        self.assertNotIn("`bhagavā`", index.index_report(occ, folder="c/", root=FIXTURES))


class TestRows(unittest.TestCase):
    def test_commonest_rows(self):
        rows = index.common_rows(index.occurrences(files()), "Namo", root=FIXTURES)
        self.assertEqual(rows, [("| **`namo`** | `(ind)` homage; **[namo]** |", 2, "a/01_one.md:12")])

    def test_unknown_word(self):
        self.assertEqual(index.common_rows(index.occurrences(files()), "dhammo"), [])

    def test_json_output(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            index.main(["--books", str(FIXTURES / "nobooks"), "rows", "namo", "--json"])
        self.assertEqual(json.loads(out.getvalue()), [{"word": "namo", "rows": []}])


class TestOverlapsAndDupes(unittest.TestCase):
    def test_overlaps_in_other_folders(self):
        report = index.overlaps_report(index.parsed([TWO]), files(), root=FIXTURES)
        self.assertIn("b/01_two.md:5: Namo buddhassa\n    = a/01_one.md:5 (table)", report)
        self.assertIn("b/01_two.md:26: Buddho bhagavā\n    = a/01_one.md:15 (table)", report)
        self.assertNotIn("saraṇaṁ", report)

    def test_dupes_lines(self):
        report = index.dupes_report(files(), lines=True, root=FIXTURES)
        self.assertIn("## Texts with identical Pāli (0)", report)
        self.assertIn("- Namo buddhassa — 2×: a/01_one.md:5, b/01_two.md:5", report)


class TestStats(unittest.TestCase):
    def test_counts(self):
        report = index.stats_report(files())
        self.assertIn("| **all** | 2 | 5 | 5 | 0 | 0 | 11 | 0 | 7 |", report)


if __name__ == "__main__":
    unittest.main()
