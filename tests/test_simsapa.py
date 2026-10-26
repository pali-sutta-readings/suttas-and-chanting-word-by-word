import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import simsapa
from chantlib.parse import parse_file

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "simsapa"
TEXT = FIXTURES / "texts" / "01_check.md"


def fx():
    return simsapa.FixtureClient(FIXTURES)


def run(*argv):
    """Run simsapa.py on the fixtures; returns (exit status, stdout)."""
    out = io.StringIO()
    old = os.environ.get("SIMSAPA_FIXTURES")
    os.environ["SIMSAPA_FIXTURES"] = str(FIXTURES)
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            status = simsapa.main(list(argv))
    finally:
        if old is None:
            del os.environ["SIMSAPA_FIXTURES"]
        else:
            os.environ["SIMSAPA_FIXTURES"] = old
    return status, out.getvalue()


def head(lemma_1, construction=(), root_key="", pos="masc", matched_as="inflection",
         summary="", root_base=""):
    return {"uid": "1/dpd", "lemma_1": lemma_1, "pos": pos, "grammar": "",
            "construction": list(construction), "construction_summary": summary,
            "root_key": root_key, "root_base": root_base, "root_sign": "",
            "form_grammar": [], "meaning_1": "", "matched_as": matched_as}


def result(*heads, splits=(), raw=()):
    return {"input": "x", "lookup_key": "x", "status": "found", "headwords": list(heads),
            "deconstructions": [{"split": s, "kind": "sandhi", "source": "dpd",
                                 "components": []} for s in splits],
            "form_grammar_raw": [list(t) for t in raw]}


class TestCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rows = [(TEXT, r) for u in parse_file(TEXT).units for r in u.rows]
        cls.items = {it.key.split("#")[0]: it for it in simsapa.check_rows(fx(), rows)}

    def test_good_rows_pass(self):
        for word in ("bhagavantaṁ", "dhamm'", "sat'", "cittan'ti", "attham-"):
            self.assertFalse([k for k in self.items if k.endswith(":" + word)
                              and not k.startswith("noroot")], word)

    def test_verb_row_passes_through_construction_summary(self):
        # DPD stores bhaṇa + mase; its entry shows √bhaṇ + a + mase, as our row does.
        self.assertNotIn("ety:bhaṇāmase", self.items)
        self.assertNotIn("grammar:bhaṇāmase", self.items)

    def test_root_flags(self):
        self.assertEqual(self.items["root:vicāraṁ"].level, "FLAG")
        self.assertIn("√car", self.items["root:vicāraṁ"].dpd)
        self.assertEqual(self.items["root:vattu"].level, "FLAG")

    def test_no_root_flag(self):
        self.assertEqual(self.items["noroot:bhagavantaṁ"].level, "FLAG")

    def test_etymology_candidate(self):
        it = self.items["ety:sammāsambuddho"]
        self.assertEqual(it.level, "CANDIDATE")
        self.assertEqual(it.dpd, "sammā + sambuddha")

    def test_grammar_candidates(self):
        self.assertIn("fut 3rd pl", self.items["grammar:carissanti"].dpd)
        self.assertIn("grammar:manussaṁ", self.items)

    def test_not_found_candidate(self):
        self.assertEqual(self.items["notfound:xyzqq"].level, "CANDIDATE")

    def test_key_does_not_depend_on_file(self):
        self.assertEqual(self.items["root:vattu"].key, "root:vattu#b143f44f3f")

    def test_ledger_hides_and_exit_status(self):
        # Every run gets its own ledger, never checks/dpd-review.tsv.
        with tempfile.TemporaryDirectory() as d:
            ledger = Path(d) / "dpd-review.tsv"
            ledger.write_text("key\tverdict\treason\tdate\n", encoding="utf-8")
            status, out = run("check", str(TEXT), "--ledger", str(ledger))
            self.assertEqual(status, 1)
            flags = [ln.split()[2] for ln in out.splitlines() if " FLAG " in ln]
            self.assertEqual(len(flags), 3)
            ledger.write_text("key\tverdict\treason\tdate\n" + "".join(
                f"{k}\terror\ttest\t2026-10-26\n" for k in flags), encoding="utf-8")
            status, out = run("check", str(TEXT), "--ledger", str(ledger))
            self.assertEqual(status, 0)
            self.assertNotIn(" FLAG ", out)
            status, _ = run("check", str(TEXT), "--ledger", str(ledger), "--strict")
            self.assertEqual(status, 1)

    def test_json(self):
        _, out = run("check", str(TEXT), "--json", "--ledger", os.devnull)
        items = json.loads(out)
        self.assertTrue(all({"key", "level", "kind", "word", "ours", "dpd", "places"} <= set(i)
                            for i in items))


class TestRespellings(unittest.TestCase):
    def test_elided_member_takes_citation_forms(self):
        res, via = simsapa.resolve(fx(), ["dhamm'"])["dhamm'"]
        self.assertEqual(res["status"], "found")
        self.assertTrue(all(h["matched_as"] == "lemma" for h in res["headwords"]))
        self.assertIn("dhamma 1.01", [h["lemma_1"] for h in res["headwords"]])
        self.assertIn("elided", via)

    def test_elided_rule_applies_even_when_the_stem_is_a_word(self):
        res, _ = simsapa.resolve(fx(), ["sat'"])["sat'"]
        self.assertIn("√sar 2", [h["root_key"] for h in res["headwords"]])

    def test_sandhi_spelling(self):
        self.assertEqual(simsapa.sandhi_respelling("attham-"), "atthaṁ")
        self.assertEqual(simsapa.sandhi_respelling("buddhañ"), "buddhaṁ")
        self.assertIsNone(simsapa.sandhi_respelling("buddha"))
        res, via = simsapa.resolve(fx(), ["attham-"])["attham-"]
        self.assertEqual((res["status"], res["input"], via),
                         ("found", "attham-", "respelled as atthaṁ"))

    def test_not_found_stays_not_found(self):
        res, via = simsapa.resolve(fx(), ["xyzqq"])["xyzqq"]
        self.assertEqual((res["status"], via), ("not_found", None))


class TestNotation(unittest.TestCase):
    """The fixed notation rules (docs/script-or-skill.md, spike 2 and follow-up)."""

    def test_a_bare_lemma(self):
        self.assertTrue(simsapa.ety_matches("ca", result(head("ca 1.1", ["x + y"]))))

    def test_b_nothing_to_compare(self):
        self.assertTrue(simsapa.ety_matches("anything + else", result(head("cīvara"))))

    def test_c_brackets_and_asterisks(self):
        self.assertTrue(simsapa.matches("ā + √khā + y + ī", "ā + √khā + [y] + ī"))
        self.assertTrue(simsapa.matches("√su + aka", "√su + *aka"))
        self.assertTrue(simsapa.matches("siri + ttha", "?? siri + *ttha"))

    def test_d_nested_sub_analyses(self):
        self.assertTrue(simsapa.matches("vibhūsana (vi + √bhūs + ana) + ṭhāna (√ṭhā + ana)",
                                        "vibhūsana + ṭhāna"))

    def test_e_chain_links(self):
        self.assertTrue(simsapa.matches("adhi > ajjh + āsaya", "adhi > adhy > ajjh + āsaya"))
        self.assertTrue(simsapa.matches("√nī + a", "√nī > nay + *a"))
        self.assertFalse(simsapa.matches("√nī + a", "√nī + ana"))

    def test_f_trailing_ending(self):
        self.assertTrue(simsapa.matches("viññāṇa + paccaya", "viññāṇa + paccaya + ā"))
        self.assertFalse(simsapa.matches("pa + √i", "pa + √i + ta"))

    def test_g_inflected_split_member(self):
        self.assertTrue(simsapa.matches("gaja + vara", "gaja + varaṁ", "split"))
        self.assertTrue(simsapa.matches("ta + api", "taṁ + api", "split"))
        self.assertTrue(simsapa.matches("muni + rāja", "muni + rājassa", "split"))
        self.assertFalse(simsapa.matches("gaja + vara", "gaja + varaṁ"))
        # The same text as a headword's construction and as a split keeps both kinds.
        res = result(head("tampi", ["taṁ + api"]), splits=["taṁ + api"])
        self.assertTrue(simsapa.ety_matches("ta + api", res))

    def test_h_verb_ending(self):
        self.assertTrue(simsapa.matches("anu + √mud + a + tha", "anu + √mud + *a + ti", "verb"))
        self.assertTrue(simsapa.matches("upa + √ṭhā > ṭhāpe + ssa + nti", "upa + ṭhāpe + ti", "verb"))
        self.assertFalse(simsapa.matches("anu + √mud + a + tha", "anu + √mud + *a + ti"))
        self.assertFalse(simsapa.matches("anu + √bhuj + a + tha", "anu + √mud + *a + ti", "verb"))

    def test_i_member_grouping(self):
        self.assertTrue(simsapa.matches("pubba + bhāga + namakāra", "pubbabhāga + namakāraṁ", "split"))
        self.assertTrue(simsapa.matches("abyāpāda + saṅkappa", "na > a + byāpāda + saṅkappa"))
        self.assertTrue(simsapa.matches("sabba + roga + vināsa", "sabbaroga + vināsāya", "split"))
        # Letters must join exactly, and roots are never joined.
        self.assertFalse(simsapa.matches("dhamma + savana + kāla", "dhammassavana + kāla"))
        self.assertFalse(simsapa.matches("pari + √vā + ta", "parivāta"))

    def test_j_enclitic(self):
        res = result(head("saṅgha", ["saṁ + √ghaṭ + a"]), splits=["saṅghaṁ + ca"])
        self.assertTrue(simsapa.ety_matches("saṁ + √ghaṭ + a + ca", res))
        self.assertFalse(simsapa.ety_matches("saṁ + √ghaṭ + a + ca", result(head("saṅgha", ["saṁ + √ghaṭ + a"]))))

    def test_root_base_substitution(self):
        self.assertEqual(simsapa.substitute_root_base("a + dese + si", "√dis + *e > dese (caus)"),
                         "a + √dis + *e > dese + si")
        self.assertIsNone(simsapa.substitute_root_base("bhaga + vant", "√x > y"))
        res = result(head("bhaṇāmase", ["bhaṇa + mase"], "√bhaṇ", pos="imp",
                          root_base="√bhaṇ + a > bhaṇa"))
        self.assertTrue(simsapa.ety_matches("√bhaṇ + a + mase", res))

    def test_our_analyses(self):
        self.assertEqual(simsapa.our_analyses("agga, no root in DPD"), (["agga"], "agga"))
        self.assertEqual(simsapa.our_analyses("pa + √su + ta; DPD pasūta")[0], ["pa + √su + ta"])
        self.assertEqual(simsapa.our_analyses("na > an + atta; + iti")[0], ["na > an + atta + iti"])
        self.assertEqual(simsapa.our_analyses("pp of bhāveti, √bhū > bhāve + ita")[0],
                         ["√bhū > bhāve + ita"])
        self.assertEqual(simsapa.our_analyses("ta / tvaṁ")[0], ["ta", "tvaṁ"])

    def test_grammar(self):
        agree = simsapa.grammar_agrees
        self.assertTrue(agree(["masc acc sg"], ["masc acc sg"]))
        self.assertTrue(agree(["masc dat/gen sg"], ["masc gen sg"]))
        self.assertTrue(agree(["adj masc nom sg"], ["masc nom sg", "nt nom sg"]))
        self.assertFalse(agree(["fem acc sg"], ["masc acc sg"]))
        self.assertTrue(agree(["2nd sg dat"], ["2nd dat sg"]))
        self.assertTrue(agree(["pron masc nom pl"], ["dual nom sg"]))
        self.assertTrue(agree(["1st pl pres mid imperat"], ["reflx imp 1st pl"]))
        self.assertFalse(agree(["1st pl pres act indic"], ["reflx imp 1st pl"]))
        self.assertTrue(agree(["3rd pl aor act indic"], ["imperf 3rd pl"]))
        self.assertIsNone(agree(["ind"], ["masc nom sg"]))


class TestClient(unittest.TestCase):
    def test_missing_form_grammar_is_an_error(self):
        cl = fx()
        for r in cl.recorded.values():
            r.pop("form_grammar_raw", None)
        with self.assertRaises(simsapa.SimsapaError) as e:
            cl.lookup_forms(["bhagavantaṁ"])
        self.assertIn("form_grammar_raw", str(e.exception))

    def test_not_running(self):
        with self.assertRaises(simsapa.SimsapaError) as e:
            simsapa.Client(port=1, timeout=2).lookup_forms(["dhamma"])
        self.assertIn("not running", str(e.exception))

    def test_port_file(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "api-port.txt").write_text("4999\n")
            old = os.environ.get("SIMSAPA_DIR")
            os.environ["SIMSAPA_DIR"] = d
            try:
                self.assertEqual(simsapa.api_port(), 4999)
            finally:
                if old is None:
                    del os.environ["SIMSAPA_DIR"]
                else:
                    os.environ["SIMSAPA_DIR"] = old


class TestLookup(unittest.TestCase):
    def test_text(self):
        _, out = run("lookup", "bhaṇāmase")
        self.assertIn("summary: √bhaṇ + a + mase", out)
        self.assertIn("DPD parses: bhaṇati verb reflx imp 1st pl", out)

    def test_widen_is_labelled_as_guesses(self):
        _, out = run("lookup", "bhagav", "--widen")
        self.assertIn("bhagav — not_found", out)
        self.assertIn("guesses, not DPD's entry for this form", out)
        self.assertIn("bhagavant 1", out)

    def test_inflections_and_json(self):
        _, out = run("lookup", "bhagavantaṁ", "--inflections", "--json")
        w = json.loads(out)["words"][0]
        self.assertEqual(w["lookup"]["status"], "found")
        self.assertIn("49139/dpd", w["inflections"])
        self.assertIn("|", w["inflections"]["49139/dpd"])


class TestGloss(unittest.TestCase):
    def test_tokens_in_order_with_unknown_and_iti_kept(self):
        lines = [("a", "Yo so tathāgato arahaṁ sammāsambuddho"),
                 ("b", "Puna caparaṁ, bhikkhave, bhikkhu gacchanto vā gacchāmī'ti pajānāti "
                       "sabb'ītiyo xyzqq")]
        out = simsapa.gloss_lines(fx(), lines)
        self.assertEqual([ln["line"] for ln in out], ["a", "b"])
        words = [t["word"] for t in out[1]["tokens"]]
        self.assertEqual(words[-4:], ["gacchāmī'ti", "pajānāti", "sabb'ītiyo", "xyzqq"])
        self.assertEqual([t["token_index"] for t in out[1]["tokens"]], list(range(len(words))))
        self.assertEqual(out[1]["tokens"][-1]["status"], "not_found")
        tok = out[0]["tokens"][4]
        self.assertIn("form_grammar_raw", tok["lookup"])
        self.assertTrue(tok["settled_rows"])

    def test_line_count_mismatch_is_an_error(self):
        with self.assertRaises(simsapa.SimsapaError):
            simsapa.gloss_lines(fx(), [("a", "Yo so")])


if __name__ == "__main__":
    unittest.main()
