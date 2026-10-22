import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from chantlib.parse import parse_file, parse_text, split_row, split_tags, tag_tokens
from chantlib.text import fold_niggahita, nfc, norm_line, pali_letters_only

FIXTURES = Path(__file__).resolve().parent / "fixtures"
DN22_OPTIONS = {"heading-gloss": True, "heading-numbers": True}


class TextTest(unittest.TestCase):
    def test_nfc(self):
        self.assertEqual(nfc("ā"), "ā")

    def test_fold_niggahita(self):
        self.assertEqual(fold_niggahita("mayaṃ Ṃ"), "mayaṁ Ṁ")

    def test_pali_letters_only(self):
        self.assertEqual(pali_letters_only("Sabb'ītiyo, Vivajjantu—"), "sabbītiyo vivajjantu")

    def test_norm_line(self):
        self.assertEqual(
            norm_line("Namo tassa bhagavato (×3)"), norm_line("namo-tassa  bhagavato")
        )
        self.assertEqual(norm_line("[Yo so] bhagavā"), "yosobhagavā")
        self.assertEqual(norm_line("evaṃ …pe… hoti"), "evaṁhoti")


class SplitRowTest(unittest.TestCase):
    def test_row_with_note(self):
        row = split_row(
            "| **`bhikkhavo'ti`** | `(masc voc pl)` [*bhikkhavo* + *iti* (ind), "
            "closing the quotation] bhikkhus!; **[√bhikkh + u + avo; iti]** |", 7
        )
        self.assertEqual(row.line, 7)
        self.assertEqual(row.word, "bhikkhavo'ti")
        self.assertFalse(row.member)
        self.assertEqual(row.groups, ["masc voc pl"])
        self.assertEqual(row.note, "*bhikkhavo* + *iti* (ind), closing the quotation")
        self.assertEqual(row.meaning, "bhikkhus!")
        self.assertEqual(row.ety, "√bhikkh + u + avo; iti")

    def test_member_row(self):
        row = split_row("| ↳ **`sammā`** | `(ind comp)` perfectly, rightly; **[sammā]** |")
        self.assertTrue(row.member)
        self.assertEqual(row.word, "sammā")
        self.assertEqual(row.note, "")

    def test_alternative_groups(self):
        row = split_row("| **`te`** | `(fem nom pl)` / `(ind)` they; **[ta]** |")
        self.assertEqual(row.groups, ["fem nom pl", "ind"])
        self.assertEqual(tag_tokens(["masc dat/gen sg"]), {"masc", "dat", "gen", "sg"})
        self.assertEqual(split_tags("`(a b)` / `(c)`"), ["a b", "c"])

    def test_bad_row(self):
        self.assertIsNone(split_row("| **`word`** | meaning without tags |"))


class ParseGoodTest(unittest.TestCase):
    def test_good(self):
        cf = parse_file(FIXTURES / "good.md")
        self.assertEqual(cf.title, "Pubbabhāga-namakāra")
        self.assertEqual(cf.subtitle, "Preliminary Homage")
        self.assertEqual(cf.stray, [])
        self.assertEqual(len(cf.units), 3)
        first, second, third = cf.units
        self.assertTrue(first.pali.startswith("Handa mayaṁ"))
        self.assertEqual(first.literal_line, 7)
        self.assertEqual(first.faithful_line, 8)
        self.assertTrue(first.header)
        self.assertEqual([r.word for r in first.rows if not r.member],
                         ["handa", "mayaṁ", "buddhassa", "bhagavato",
                          "pubbabhāga-namakāraṁ", "karomase"])
        self.assertEqual(sum(r.member for r in first.rows), 3)
        self.assertFalse(second.repeat)
        self.assertTrue(third.repeat)
        self.assertEqual(third.rows, [])
        self.assertEqual(third.citation, "AN 11.15")
        kinds = {ln.kind for ln in cf.lines}
        self.assertTrue({"title", "subtitle", "heading", "rubric", "pali", "literal",
                         "faithful", "thead", "tsep", "row", "member", "repeat",
                         "citation", "blank"} <= kinds)

    def test_vinaya(self):
        cf = parse_file(FIXTURES / "good-vinaya.md")
        self.assertEqual(len(cf.kinds("instruction")), 1)
        unit = cf.units[0]
        self.assertEqual(len(unit.variants), 4)
        v = unit.variants[0]
        self.assertEqual(v.pairs, [("imaṁ saṅghāṭiṁ", "imaṁ uttarā-saṅgaṁ")])
        self.assertTrue(v.header)
        self.assertEqual([r.word for r in v.rows],
                         ["imaṁ", "uttarā-saṅgaṁ", "uttara", "āsaṅgaṁ"])
        self.assertEqual(len(unit.rows), 3)    # variant rows are not the unit's
        self.assertEqual(unit.citation, "Kd 8:20.2")

    def test_dn22_glosses_need_the_option(self):
        path = FIXTURES / "good-dn22.md"
        with_option = parse_file(path, options=DN22_OPTIONS)
        self.assertEqual(len(with_option.kinds("gloss")), 2)
        self.assertEqual(with_option.stray, [])
        without = parse_file(path)
        self.assertEqual(len(without.stray), 2)

    def test_omission_pair(self):
        cf = parse_text(
            "# T\n\n**Āma bhante**\n\n**Variant:** junior: *bhante* → (omit)  \n"
        )
        self.assertEqual(cf.units[0].variants[0].pairs, [("bhante", "")])

    def test_variant_without_unit(self):
        cf = parse_text("# T\n\n**Variant:** x: *a* → *b*  \n")
        self.assertEqual([ln.kind for ln in cf.lines], ["title", "blank", "badvariant"])

    def test_rubric_is_not_subtitle(self):
        cf = parse_text("# Title\n\n*(Optional)*\n")
        self.assertIsNone(cf.subtitle)
        self.assertEqual(cf.lines[2].kind, "rubric")


if __name__ == "__main__":
    unittest.main()
