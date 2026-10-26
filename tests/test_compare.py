import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import compare

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "compare"
# The sc entries' /sutta.json answers (sutta_xx1_pli_ms.json, …).
SIMSAPA_FIXTURES = FIXTURES.parent / "simsapa"
_saved_env = {}


def setUpModule():
    for k in ("SIMSAPA_FIXTURES", "SIMSAPA_DIR"):
        _saved_env[k] = os.environ.pop(k, None)
    os.environ["SIMSAPA_FIXTURES"] = str(SIMSAPA_FIXTURES)


def tearDownModule():
    for k, v in _saved_env.items():
        os.environ.pop(k, None)
        if v is not None:
            os.environ[k] = v


def entries(**changes):
    """The fixture map, with the key of some entries changed: {text: key}."""
    es = compare.read_map(FIXTURES / "map.tsv")
    for e in es:
        if e.text in changes:
            e.key = changes[e.text]
    return es


def entry(text, **changes):
    return next(e for e in entries(**changes) if e.text == text and e.source != "none")


def report(es):
    out = io.StringIO()
    errors = compare.run_diff(es, root=FIXTURES, out=out)
    return errors, out.getvalue()


class TestBM(unittest.TestCase):
    def test_structural_rules(self):
        lines = compare.ref_lines(entry("homage.md"), FIXTURES)
        self.assertEqual(lines, [
            "Handa mayaṁ buddhassa karomase",
            "Namo tassa bhagavato",
            "Arahato – sammāsambuddhassa (×3)",
            "Buddhaṁ saraṇaṁ gacchāmi",
        ])

    def test_anchor_stops_at_next_anchor(self):
        lines = compare.ref_lines(entry("homage-short.md"), FIXTURES)
        self.assertNotIn("Buddhaṁ saraṇaṁ gacchāmi", lines)

    def test_range_stops_before_end_anchor(self):
        lines = compare.ref_lines(entry("homage.md", **{"homage.md": "homage..second"}), FIXTURES)
        self.assertEqual(lines[-1], "Arahato – sammāsambuddhassa (×3)")

    def test_range_to_end(self):
        lines = compare.ref_lines(entry("homage.md", **{"homage.md": "homage-english..END"}), FIXTURES)
        self.assertIn("Then: 'Imaṁ pattaṁ adhiṭṭhāmi.'", lines)

    def test_identical(self):
        status, lines = compare.compare_entry(entry("homage.md"), FIXTURES)
        self.assertEqual((status, lines), ("identical", []))

    def test_ccb_tone_marks_do_not_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = Path(tmp) / "map.tsv"
            m.write_text("text\tsource\tfile\tkey\tmode\tnote\nhomage.md\tccb\tccb.md\thomage\tdiff\t\n", encoding="utf-8")
            e = compare.read_map(m)[0]
        self.assertNotIn("Dhammaṁ saraṇaṁ gacchāmi", compare.ref_lines(e, FIXTURES))
        self.assertEqual(compare.compare_entry(e, FIXTURES), ("identical", []))

    def test_difference_gives_line_and_context(self):
        status, lines = compare.compare_entry(entry("homage.md", **{"homage.md": "homage"}), FIXTURES)
        self.assertEqual(status, "1 difference")
        self.assertIn("line 19: delete", lines[0])
        self.assertIn("⟦buddhaṁsaraṇaṁgacchāmi⟧", lines[0])


    def test_italic_table_cells_are_dropped(self):
        e = entry("homage.md", **{"homage.md": "parts..verse-one"})
        self.assertEqual(compare.ref_lines(e, FIXTURES), ["kesā", "lomā"])

    def test_anchor_off_a_heading(self):
        e = entry("homage.md", **{"homage.md": "verse-one"})
        self.assertEqual(compare.stream(compare.ref_lines(e, FIXTURES)), "yaṅkiñcivittaṁ")


class TestContain(unittest.TestCase):
    def test_all_found_despite_english(self):
        status, _ = compare.compare_entry(entry("vinaya.md"), FIXTURES)
        self.assertEqual(status, "all lines found")

    def test_not_found_and_out_of_order(self):
        status, lines = compare.compare_entry(entry("vinaya-bad.md"), FIXTURES)
        self.assertEqual(status, "2 lines not found")
        self.assertIn("line 12: out of order: imaṁsaṅghāṭiṁadhiṭṭhāmi", lines[0])
        self.assertIn("line 19: not found: imaṁcīvaraṁdammi", lines[1])


class TestSegments(unittest.TestCase):
    def test_sc_skips_title_and_heading_segments(self):
        self.assertEqual(compare.ref_lines(entry("sc-text.md"), FIXTURES),
                         ["Evaṁ me sutaṁ—", "ekaṁ samayaṁ bhagavā. "])
        self.assertEqual(compare.compare_entry(entry("sc-text.md"), FIXTURES)[0], "identical")

    def test_sc_difference(self):
        status, lines = compare.compare_entry(entry("sc-diff.md"), FIXTURES)
        self.assertEqual(status, "1 difference")
        self.assertIn("⟦pañcamaṁ⟧", lines[0])

    def test_uid_not_in_simsapa(self):
        e = entry("sc-text.md")
        e.file = "xx9/pli/ms"
        with self.assertRaisesRegex(compare.MapError, r"\(sc-text.md\): Simsapa has no SuttaCentral text 'xx9/pli/ms' \(not_found\)"):
            compare.ref_lines(e, FIXTURES)

    def test_skipped_when_simsapa_is_not_running(self):
        e = entry("sc-text.md")
        e.file = "xx8/pli/ms"
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "api-port.txt").write_text("1\n")
            del os.environ["SIMSAPA_FIXTURES"]
            os.environ["SIMSAPA_DIR"] = tmp
            try:
                status, lines = compare.compare_entry(e, FIXTURES)
            finally:
                del os.environ["SIMSAPA_DIR"]
                os.environ["SIMSAPA_FIXTURES"] = str(SIMSAPA_FIXTURES)
        self.assertRegex(status, r"^skipped: Simsapa is not running on port 1")

    def test_missing_segment(self):
        with self.assertRaisesRegex(compare.MapError, r"ref-map.tsv:6 \(sc-text.md\): segment 'xx1:9.9' not found"):
            compare.ref_lines(entry("sc-text.md", **{"sc-text.md": "xx1:1.1..xx1:9.9"}), FIXTURES)


class TestReport(unittest.TestCase):
    def test_differences_are_not_errors(self):
        errors, out = report(entries(**{"homage.md": "homage"}))
        self.assertEqual(errors, 0)
        self.assertIn("1 difference", out)
        self.assertIn("no reference\n  not in any source", out)

    def test_missing_anchor_names_entry(self):
        errors, out = report(entries(**{"homage.md": "gone"}))
        self.assertEqual(errors, 1)
        self.assertIn("MAP ERROR: ref-map.tsv:2 (homage.md): anchor 'gone' not found", out)

    def test_main_exit_codes(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(compare.main(["--map", str(FIXTURES / "map.tsv"), "--root", str(FIXTURES), "diff"]), 0)
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "map.tsv"
            bad.write_text((FIXTURES / "map.tsv").read_text(encoding="utf-8").replace("\tsecond\t", "\tx\t")
                           .replace("homage..homage-english", "homage..nowhere"), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(compare.main(["--map", str(bad), "--root", str(FIXTURES), "diff"]), 1)

    def test_chanting_guide_without_local_copy_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copy(FIXTURES / "homage.md", root)
            (root / "map.tsv").write_text(
                "text\tsource\tfile\tkey\tmode\tnote\n"
                "homage.md\tchanting-guide\tupstream/cg.md\tHomage\tcontain\t\n", encoding="utf-8")
            errors, out = 0, io.StringIO()
            errors = compare.run_diff(compare.read_map(root / "map.tsv"), root=root, out=out)
            self.assertEqual(errors, 0)
            self.assertIn("skipped: no local copy at upstream/cg.md", out.getvalue())

    def test_chanting_guide_heading_range(self):
        lines = ["### Homage ", "Namo tassa bhagavato arahato sammāsambuddhassa", "### Next ", "Buddhaṁ saraṇaṁ"]
        self.assertEqual(compare.heading_passage(lines, "Homage..Next", "x"),
                         ["Namo tassa bhagavato arahato sammāsambuddhassa"])
        with self.assertRaisesRegex(compare.MapError, "heading 'Gone' not found"):
            compare.heading_passage(lines, "Homage..Gone", "x")

    def test_bad_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "map.tsv"
            p.write_text("text\tsource\n", encoding="utf-8")
            with self.assertRaisesRegex(compare.MapError, "header must be"):
                compare.read_map(p)


class TestOurText(unittest.TestCase):
    def test_units_exclude_repeat_marks(self):
        units = compare.our_units(FIXTURES / "homage-short.md")
        self.assertEqual(units, [(5, "namotassabhagavatoarahatosammāsambuddhassa")])


if __name__ == "__main__":
    unittest.main()
