#!/usr/bin/env python3
"""DPD lookups through the Simsapa localhost API, and DPD checks of the word
tables. The API is served by the Simsapa app while it runs, or by the
`simsapa` CLI's `simsapa serve`.

Usage:
    simsapa.py lookup WORD... [--json] [--inflections] [--widen]
    simsapa.py check FILE... [--strict] [--json] [--ledger TSV]
    simsapa.py gloss FILE... | --text TEXT [--text-output]

Only the exact routes answer the checks (docs/simsapa-cli-and-localhost-
api.md §19): POST /lookup_forms and /gloss_text with "exact": true.
/word.json is used only by `lookup --inflections`, and /dict_combined_search
only by `lookup --widen`, whose results are printed as guesses.

Words are sent as written; the API handles apostrophes, hyphens and iti
sandhi. Two of our notations are not DPD forms and get a fixed respelling
(PRD FR-17a): an elided member (`dhamm'`) is looked up as the stem plus each
vowel, keeping only citation forms; a sandhi spelling (`attham-`, `buddhañ`)
that DPD does not know loses its hyphens and ends in ṁ.

The scripts never assign grammar labels, split compounds or compose rows.
`check` compares rows with DPD and reports items for review by the
dpd-review skill; `gloss` presents DPD's data for the pali-word-analysis
skill. See docs/script-or-skill.md (spike 2 and its follow-up).

The port is read from $SIMSAPA_DIR/api-port.txt, else from the data folder
that `simsapa paths --json` reports, else 4848. With
SIMSAPA_FIXTURES set to a folder of recorded responses (tests/fixtures/
simsapa/), no request is made.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chantlib import books
from chantlib.parse import parse_file, tag_tokens
from chantlib.text import APOSTROPHES, fold_niggahita, nfc

import index
import simsapa_fmt

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "checks" / "dpd-review.tsv"
API_DOC = "docs/simsapa-cli-and-localhost-api.md"
BATCH = 5000   # the most forms /lookup_forms takes in one call

VOWELS = "aāiīuūeo"
CASES = {"nom", "acc", "instr", "dat", "abl", "gen", "loc", "voc"}
NUMBERS = {"sg", "pl"}
GENDERS = {"masc", "fem", "nt"}
PERSONS = {"1st", "2nd", "3rd"}
# Our tense and mood tags → DPD's parse words. DPD calls some aorists
# `imperf` (āgū, ajjhagā), which our rows tag aor.
MOODS = {"imperat": {"imp"}, "opt": {"opt"}}
TENSES = {"pres": {"pr"}, "aor": {"aor", "imperf"}, "fut": {"fut"},
          "perf": {"perf"}, "cond": {"cond"}}
# DPD's pos values of finite verbs.
VERB_POS = {"pr", "aor", "fut", "opt", "imp", "perf", "cond", "imperf"}
# Tense signs our verb rows write before the ending (rule h).
TENSE_SIGNS = {"ssa", "issa", "essa", "ss", "iss", "s", "i"}


class SimsapaError(Exception):
    """Simsapa is not running, too old, or answered with an error."""


# ------------------------------------------------------------------ client

def api_port():
    d = os.environ.get("SIMSAPA_DIR")
    if d:
        try:
            return int((Path(d) / "api-port.txt").read_text().strip())
        except (OSError, ValueError):
            pass
        return 4848
    try:
        out = subprocess.run(["simsapa", "paths", "--json"], capture_output=True,
                             text=True, timeout=10).stdout
        return int(json.loads(out)["api_port_file"]["port"])
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError):
        return 4848


class Client:
    """The routes the tools use, on the live API."""

    def __init__(self, port=None, timeout=60):
        self.port = port or api_port()
        self.base = f"http://localhost:{self.port}"
        self.timeout = timeout
        self.dpd_version = None
        self.warned = False

    def _open(self, req):
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()
        except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
            raise SimsapaError(
                f"Simsapa is not running on port {self.port} ({e}); start it with "
                f"`simsapa serve` or start the Simsapa app (see {API_DOC})") from None

    def get(self, path, **params):
        url = self.base + path + ("?" + urllib.parse.urlencode(params) if params else "")
        return self._open(urllib.request.Request(url))

    def post(self, path, body):
        req = urllib.request.Request(self.base + path, json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
        status, data = self._open(req)
        if status == 404:
            raise SimsapaError(f"Simsapa has no {path} route: simsapa.py needs "
                               "Simsapa 1.1.0-alpha.2 or later")
        if status != 200:
            raise SimsapaError(f"{path} answered HTTP {status}: {data[:300].decode(errors='replace')}")
        return json.loads(data)

    def _lookup_batch(self, forms):
        return self.post("/lookup_forms", {"forms": forms})

    def lookup_forms(self, forms):
        """One /lookup_forms result per form, in order, in batches."""
        out = []
        for i in range(0, len(forms), BATCH):
            data = self._lookup_batch(forms[i:i + BATCH])
            self.dpd_version = data.get("dpd_version")
            out += data["results"]
        self._check_fields(out)
        return out

    def gloss_exact(self, text):
        data = self.post("/gloss_text", {"text": text, "options": {"exact": True}})
        if not data.get("exact"):
            raise SimsapaError("/gloss_text ignored \"exact\": simsapa.py needs "
                               "Simsapa 1.1.0-alpha.2 or later")
        self.dpd_version = data.get("dpd_version")
        self._check_fields([t["lookup"] for p in data["paragraphs"] for t in p["tokens"]])
        return data

    def word(self, uid):
        """The /word.json record for a uid, or None (HTTP 404)."""
        status, data = self.get("/word.json", uid=uid)
        if status != 200:
            return None
        recs = json.loads(data)
        return recs[0] if recs else None

    def search(self, query):
        return self.post("/dict_combined_search", {"query_text": query})

    def _check_fields(self, results):
        """Fail on a Simsapa without DPD's parses; warn on an old dpd.sqlite3."""
        if results and "form_grammar_raw" not in results[0]:
            raise SimsapaError("Simsapa's /lookup_forms returns no form_grammar_raw: "
                               f"update Simsapa (see {API_DOC} §19.1)")
        if not self.warned and any(h.get("construction_summary", "") is None
                                   for r in results for h in r["headwords"]):
            self.warned = True
            print("warning: construction_summary is null: the installed dpd.sqlite3 "
                  "predates it; constructions are compared without it", file=sys.stderr)


class FixtureClient(Client):
    """Answers from recorded responses (tests/fixtures/simsapa/).

    /lookup_forms answers each form from the results in lookup_forms.json
    (matched on `input`); a form not recorded there is `not_found`.
    /sutta.json (used by compare.py) answers uid `a/b/c` from sutta_a_b_c.json.
    """

    def __init__(self, folder):
        super().__init__(port=0)
        self.folder = Path(folder)
        data = json.loads((self.folder / "lookup_forms.json").read_text(encoding="utf-8"))
        self.recorded = {r["input"]: r for r in data["results"]}
        self.version = data.get("dpd_version")

    def _lookup_batch(self, forms):
        return {"dpd_version": self.version,
                "results": [self.recorded.get(f) or not_found(f) for f in forms]}

    def post(self, path, body):
        if path == "/gloss_text":
            return json.loads((self.folder / "gloss_exact.json").read_text(encoding="utf-8"))
        if path == "/dict_combined_search":
            q = body["query_text"]
            for f in [self.folder / f"search_{q}.json", *sorted(self.folder.glob(f"search_{q}-*.json"))]:
                if f.is_file():
                    return json.loads(f.read_text(encoding="utf-8"))
            return {"hits": 0, "results": []}
        raise SimsapaError(f"no fixture for {path}")

    def get(self, path, **params):
        if path == "/word.json":
            f = self.folder / f"word_{params['uid'].split('/')[0]}.json"
            return (200, f.read_bytes()) if f.is_file() else (404, b"[]")
        if path == "/sutta.json":
            f = self.folder / f"sutta_{params['uid'].replace('/', '_')}.json"
            return (200, f.read_bytes()) if f.is_file() else (404, b'{"reason": "not_found"}')
        raise SimsapaError(f"no fixture for {path}")


def client():
    fx = os.environ.get("SIMSAPA_FIXTURES")
    return FixtureClient(fx) if fx else Client()


def not_found(form, key=None):
    return {"input": form, "lookup_key": key or form, "status": "not_found",
            "headwords": [], "deconstructions": [], "form_grammar_raw": []}


# ------------------------------------------------------------------ respellings

def is_elided(form):
    return form[-1:] in APOSTROPHES


def stem_of(form):
    return form.rstrip(APOSTROPHES)


def sandhi_respelling(form):
    """`attham-` → `atthaṁ`; None when the rule changes nothing."""
    s = re.sub("[mñṅn]$", "ṁ", form.replace("-", ""))
    return s if s != form else None


def resolve(cl, forms, known=None):
    """{form: (result, via)} for each form, after the two fixed respellings.

    `known` holds results already fetched for some forms (from a gloss).
    `via` says which respelling answered, or is None.
    """
    forms = list(dict.fromkeys(forms))
    known = dict(known or {})
    todo = [f for f in forms if f not in known and not is_elided(f)]
    known.update(zip(todo, cl.lookup_forms(todo)))

    second = {}
    for f in forms:
        if is_elided(f):
            second[f] = [stem_of(f) + v for v in VOWELS]
        elif known[f]["status"] == "not_found" and sandhi_respelling(f):
            second[f] = [sandhi_respelling(f)]
    extra = sorted({x for xs in second.values() for x in xs})
    got = dict(zip(extra, cl.lookup_forms(extra)))

    out = {}
    for f in forms:
        if f not in second:
            out[f] = (known[f], None)
        elif is_elided(f):
            heads, seen = [], set()
            for x in second[f]:
                for h in got[x]["headwords"]:
                    if h["matched_as"] == "lemma" and h["uid"] not in seen:
                        seen.add(h["uid"])
                        # The parses are of the citation form, not of ours.
                        heads.append(dict(h, form_grammar=[]))
            res = not_found(f, stem_of(f))
            if heads:
                res.update(status="found", headwords=heads)
            out[f] = (res, "elided member: stem + vowel, citation forms")
        else:
            res = got[second[f][0]]
            if res["status"] == "not_found":
                out[f] = (known[f], None)
            else:
                out[f] = (dict(res, input=f), f"respelled as {second[f][0]}")
    return out


# ------------------------------------------------------------------ DPD data

def lemma_clean(lemma_1):
    return re.sub(r" \d+(\.\d+)*$", "", lemma_1)


def root_name(s):
    return re.sub(r"\s+\d+$", "", s.strip())


ROOT_RE = re.compile(r"√[^\s+>()\[\];,/]+")


def substitute_root_base(construction, root_base):
    """`bhaṇa + mase` with root base `√bhaṇ + a > bhaṇa` → `√bhaṇ + a > bhaṇa + mase`."""
    chain = re.sub(r"\s*\([^)]*\)\s*$", "", root_base).strip()
    stem = chain.rpartition(" > ")[2].strip()
    if not stem:
        return None
    parts = re.split(r"\s*\+\s*", construction)
    if stem not in parts:
        return None
    parts[parts.index(stem)] = chain
    return " + ".join(parts)


def dpd_constructions(res):
    """[(text, kind)]: every form of DPD's construction for the result.

    Each `construction` line, the `construction_summary` (the form DPD's entry
    displays; only the root for entries without meaning_1), each line with its
    stem replaced by the `root_base` chain, and each split. kind is "split",
    "verb" for a verb headword that the form inflects (its construction ends
    in the lemma's ending, not the form's), or "word".
    """
    out = []
    for h in res["headwords"]:
        kind = "verb" if h["pos"] in VERB_POS and h["matched_as"] == "inflection" else "word"
        for c in h["construction"]:
            out.append((c, kind))
            if h.get("root_base"):
                s = substitute_root_base(c, h["root_base"])
                if s:
                    out.append((s, kind))
        if h.get("construction_summary"):
            out.append((h["construction_summary"], kind))
    out += [(d["split"], "split") for d in res["deconstructions"]]
    return list(dict.fromkeys(out))


def dpd_roots(res):
    roots = set()
    for h in res["headwords"]:
        if h["root_key"]:
            roots.add(root_name(h["root_key"]))
        for s in h["construction"] + [h.get("construction_summary") or "", h.get("root_base") or ""]:
            roots |= {root_name(r) for r in ROOT_RE.findall(s)}
    return roots


def parses(res):
    """DPD's parses of the form: the result's, and its split components'."""
    out = [t[2] for t in res["form_grammar_raw"]]
    for d in res["deconstructions"]:
        for c in d["components"]:
            out += [t[2] for t in c.get("form_grammar_raw") or []]
    return list(dict.fromkeys(out))


def dpd_hash(res, grammar=False):
    """A short hash of the DPD data an item was compared with (no meanings)."""
    if grammar:
        data = sorted(parses(res))
    else:
        data = sorted("|".join([h["lemma_1"], h["root_key"], h.get("root_base") or "",
                                *h["construction"], h.get("construction_summary") or ""])
                      for h in res["headwords"])
        data += sorted(d["split"] for d in res["deconstructions"])
    return hashlib.sha1("\n".join(data).encode()).hexdigest()


# ------------------------------------------------------------------ our rows

def strip_parentheticals(s):
    """Drop ` (…)` groups (our nested sub-analyses, `(trad.)`), nesting allowed."""
    out, depth = [], 0
    for i, ch in enumerate(s):
        if ch == "(" and (depth or (i > 0 and s[i - 1] == " ")):
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
        elif not depth:
            out.append(ch)
    return " ".join("".join(out).split())


def our_analyses(ety):
    """(analyses, lemma said to have no root in DPD or None) of a row's etymology.

    The text after `; ` is a comment (`; v > bb`, `; DPD pasūta`), except a
    trailing `; + iti`, which is part of the analysis. ` / ` separates
    alternative analyses; `pp of bhāveti, ` before one names the lemma.
    """
    main, _, rest = ety.partition("; ")
    tail = " " + rest.split("; ")[0] if rest.startswith("+ ") else ""
    out, noroot = [], None
    for alt in main.split(" / "):
        m = re.match(r"^.* of [^,]+, (.+)$", alt)
        if m:
            alt = m.group(1)
        m = re.match(r"^(.+), no root in DPD$", alt)
        if m:
            alt = noroot = m.group(1).strip()
        out.append(strip_parentheticals(alt + tail))
    return out, noroot


def members(s):
    """`na > an + atta` → [{na, an}, {atta}]: each member's chain links."""
    # DPD's `*`, `[ ]` and its "uncertain" marker `??` are notation (rule c).
    s = nfc(fold_niggahita(s)).replace("??", "").replace("*", "").replace("[", "").replace("]", "")
    s = strip_parentheticals(s)
    return [frozenset(x.strip() for x in m.split(">") if x.strip())
            for m in re.split(r"\s*\+\s*", s.strip())]


def is_ending(member):
    """DPD's bare trailing ending (rule f): a vowel or `aṁ`."""
    return len(member) == 1 and next(iter(member)) in set(VOWELS) | {"aṁ", "ṁ"}


def inflected(ours, split):
    """Rule g: a split's member is an inflected form of ours (vara / varaṁ,
    rāja / rājassa): ours without its final letter, plus an ending of up to
    four letters."""
    return any(x != y and y.startswith(x[:-1]) and 0 <= len(y) - len(x) <= 4
               for x in ours for y in split if len(x) > 1)


def joined(run):
    """The words a run of root-free members spells when written together.

    `pubba + bhāga` → {pubbabhāga}; `na > a + byāpāda` → {nabyāpāda, abyāpāda}.
    Empty if a member has a root: roots are never joined.
    """
    if any(link.startswith("√") for m in run for link in m):
        return frozenset()
    out = {""}
    for m in run:
        out = {w + link for w in out for link in m}
    return frozenset(out)


GROUP = 4   # the longest run of members rule i joins
ENCLITICS = ("ca", "api", "pi", "eva", "va", "iti", "ti")


def _same(a, b, split):
    if len(b) >= 3 and is_ending(b[-1]) and not is_ending(a[-1]):
        b = b[:-1]                                           # rule f

    def one(x, y):
        return bool(x & y) or (split and inflected(x, y))    # rules e, g

    seen = {}

    def align(i, j):
        """Can a[i:] and b[j:] be paired, member by member or run by run?"""
        if i == len(a) or j == len(b):
            return i == len(a) and j == len(b)
        if (i, j) not in seen:
            seen[i, j] = (
                (one(a[i], b[j]) and align(i + 1, j + 1))
                # rule i: our run spells DPD's member, or DPD's run spells ours
                or any(one(joined(a[i:i + k]), b[j]) and align(i + k, j + 1)
                       for k in range(2, GROUP + 1) if i + k <= len(a))
                or any(one(a[i], joined(b[j:j + k])) and align(i + 1, j + k)
                       for k in range(2, GROUP + 1) if j + k <= len(b)))
        return seen[i, j]

    return align(0, 0)


def matches(ours, dpd, kind="word"):
    """Do two analyses agree after the fixed notation rules (c)–(i)?

    Rule h: a verb headword's construction ends in the lemma's ending
    (`anu + √mud + *a + ti`) where ours ends in the form's (`… + tha`, or
    `… + ssa + nti`), so the endings and our tense sign are left out. The
    ending is checked against DPD's parses by the grammar check instead.
    """
    a, b = members(ours), members(dpd)
    if _same(a, b, kind == "split"):
        return True
    if kind != "verb" or len(a) < 2 or len(b) < 2:
        return False
    a, b = a[:-1], b[:-1]
    if len(a) == len(b) + 1 and a[-1] & TENSE_SIGNS:
        a = a[:-1]
    return _same(a, b, False)


def ety_matches(ety, res):
    """True when the row's etymology agrees with DPD, or DPD gives nothing to compare."""
    forms = dpd_constructions(res)
    if not forms:
        return True                                          # rule b
    analyses, _ = our_analyses(ety)
    lemmas = {lemma_clean(h["lemma_1"]) for h in res["headwords"]}
    lemmas |= {c["word"] for d in res["deconstructions"] for c in d["components"]}
    # Our `x; + iti` (an iti form): the headwords are the base word's.
    analyses += [a[:-len(" + iti")] for a in analyses if a.endswith(" + iti")]
    # Rule j: an enclitic we add to the analysis (`saṁ + √ghaṭ + a + ca`)
    # where DPD splits it off (`saṅghaṁ + ca`): the rest is the base word's.
    for enc in ENCLITICS:
        if any(f.endswith(" + " + enc) for f, kind in forms if kind == "split"):
            analyses += [a[:-len(enc) - 3] for a in analyses if a.endswith(" + " + enc)]
    for a in analyses:
        if "+" not in a and ">" not in a and "√" not in a and a in lemmas:
            return True                                      # rule a
        if any(matches(a, f, kind) for f, kind in forms):
            return True
    return False


def grammar_agrees(groups, dpd_parses):
    """Does any of the row's tag groups agree with one of DPD's parses?

    Nominals: case, number, and gender when both give one. Finite verbs:
    person, number, and tense or mood. None when the row has neither.
    """
    seen = False
    for g in groups:
        toks = tag_tokens([g])
        if toks & CASES:
            seen = True
            for p in dpd_parses:
                pt = set(p.split())
                if (toks & CASES & pt and (toks & NUMBERS & pt or "dual" in pt)
                        and (not toks & GENDERS or not pt & GENDERS or toks & GENDERS & pt)):
                    return True
        elif toks & PERSONS:
            seen = True
            want = set().union(*[MOODS[t] for t in toks if t in MOODS]) or \
                set().union(*[TENSES[t] for t in toks if t in TENSES])
            for p in dpd_parses:
                pt = set(p.split())
                if toks & PERSONS & pt and toks & NUMBERS & pt and (not want or want & pt):
                    return True
    return False if seen else None


# ------------------------------------------------------------------ check

class Item:
    def __init__(self, level, kind, row, path, text, reason, dpd, hashed):
        self.level, self.kind, self.row = level, kind, row
        self.places = [(path, row.line)]
        self.text, self.reason, self.dpd = text, reason, dpd
        h = hashlib.sha1("\t".join([kind, row.word, text, hashed]).encode()).hexdigest()[:10]
        self.key = f"{kind}:{row.word}#{h}"


def table_rows(cf, options):
    for u in cf.units:
        yield from (r for r in u.rows if r is not None)
        if options.get("dpd-variant-rows"):
            for v in u.variants:
                yield from (r for r in v.rows if r is not None)


def note_words(note):
    """The italic words of a `(sandhi)` row's note; `*-r-*`, `*y-*` are glue, not words."""
    return [w for w in re.findall(r"\*([^*\s][^*]*)\*", note) if "-" not in w and len(w) > 1]


def check_rows(cl, rows):
    """[Item] for [(path, row)]: flags and candidates, one item per key."""
    forms = [r.word for _, r in rows]
    forms += [w for _, r in rows if "sandhi" in tag_tokens(r.groups) for w in note_words(r.note)]
    found = resolve(cl, forms)

    items = {}

    def add(level, kind, path, row, text, reason, dpd, hashed):
        it = Item(level, kind, row, path, text, reason, dpd, hashed)
        if it.key in items:
            items[it.key].places.append((path, row.line))
        else:
            items[it.key] = it

    for path, row in rows:
        toks = tag_tokens(row.groups)
        res, via = found[row.word]
        via = f"; {via}" if via else ""
        if "sandhi" in toks:
            for w in note_words(row.note):
                if found[w][0]["status"] == "not_found":
                    add("CANDIDATE", "notfound", path, row, w,
                        f"note word *{w}* is not in DPD", "", "")
            continue
        if res["status"] == "not_found":
            if "comp" not in toks or row.member:
                add("CANDIDATE", "notfound", path, row, row.ety,
                    f"not in DPD{via}", "", "")
            continue

        ours = {root_name(r) for r in ROOT_RE.findall(row.ety)}
        theirs = dpd_roots(res)
        if ours and theirs and not ours & theirs:
            add("FLAG", "root", path, row, row.ety,
                f"root {', '.join(sorted(ours))} matches no DPD root{via}",
                ", ".join(sorted(theirs)), dpd_hash(res))

        _, noroot = our_analyses(row.ety)
        if noroot:
            named = [h for h in res["headwords"] if lemma_clean(h["lemma_1"]) == noroot]
            if named and all(h["root_key"] for h in named):
                add("FLAG", "noroot", path, row, row.ety,
                    f"says no root in DPD, but DPD's {noroot} has one{via}",
                    "; ".join(f"{h['lemma_1']} {h['root_key']}" for h in named), dpd_hash(res))

        if "(trad.)" not in row.ety and not ety_matches(row.ety, res):
            add("CANDIDATE", "ety", path, row, row.ety,
                f"etymology matches no DPD construction or split{via}",
                " | ".join(dict.fromkeys(f for f, _ in dpd_constructions(res))), dpd_hash(res))

        ps = parses(res)
        if ps and grammar_agrees(row.groups, ps) is False:
            add("CANDIDATE", "grammar", path, row, " / ".join(f"({g})" for g in row.groups),
                f"tags match none of DPD's parses of the form{via}",
                "; ".join(ps), dpd_hash(res, grammar=True))
    return list(items.values())


def read_ledger(path):
    keys = set()
    p = Path(path)
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            key = line.split("\t", 1)[0].strip()
            if key and key != "key" and not key.startswith("#"):
                keys.add(key)
    return keys


def _rel(path):
    return index._rel(path)


def cmd_check(cl, a):
    rows = []
    for f in a.files:
        p = Path(f)
        opts = books.options_for_text(p)
        rows += [(p, r) for r in table_rows(parse_file(p, options=opts), opts)]
    items = check_rows(cl, rows)
    reviewed = read_ledger(a.ledger)
    shown = [it for it in items if it.key not in reviewed]
    hidden = len(items) - len(shown)
    shown.sort(key=lambda it: (it.level != "FLAG", str(it.places[0][0]), it.places[0][1]))
    if a.json:
        print(json.dumps([{"key": it.key, "level": it.level, "kind": it.kind,
                           "word": it.row.word, "ours": it.text, "reason": it.reason,
                           "dpd": it.dpd,
                           "places": [f"{_rel(p)}:{n}" for p, n in it.places]}
                          for it in shown], ensure_ascii=False, indent=1))
    else:
        for it in shown:
            p, n = it.places[0]
            more = f" [+{len(it.places) - 1} more]" if len(it.places) > 1 else ""
            dpd = f" (DPD: {it.dpd})" if it.dpd else ""
            print(f"{_rel(p)}:{n}: {it.level} {it.key} {it.row.word} [{it.text}] — "
                  f"{it.reason}{dpd}{more}")
    flags = sum(it.level == "FLAG" for it in shown)
    print(f"# {len(rows)} rows, DPD {cl.dpd_version}: {flags} flags, "
          f"{len(shown) - flags} candidates, {hidden} hidden by {_rel(Path(a.ledger))}",
          file=sys.stderr)
    return 1 if flags or (a.strict and shown) else 0


# ------------------------------------------------------------------ lookup

def inflections_text(record):
    """A word record's inflections_html table as plain text, one row per line."""
    h = record.get("inflections_html") or ""
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"(?i)</tr>", "\n", h)
    return "\n".join(ln.strip().rstrip("|").strip()
                     for ln in simsapa_fmt.strip_html(h, mark_matches=False).splitlines()
                     if ln.strip().strip("|").strip())


def fmt_args(**kw):
    return argparse.Namespace(no_snippet=False, snippet_len=0, **kw)


def cmd_lookup(cl, a):
    words = [nfc(fold_niggahita(w)) for w in a.words]
    found = resolve(cl, words)
    out = []
    for w in words:
        res, via = found[w]
        entry = {"word": w, "via": via, "lookup": res}
        if a.inflections:
            entry["inflections"] = {}
            for h in res["headwords"]:
                rec = cl.word(h["uid"])
                if rec:
                    entry["inflections"][h["uid"]] = inflections_text(rec)
        if a.widen and res["status"] == "not_found":
            s = cl.search(w)
            entry["guesses"] = {
                "headwords": [r["title"] for r in s.get("results") or [] if r["uid"].endswith("/dpd")],
                "deconstructor": s.get("deconstructor") or []}
        out.append(entry)
    if a.json:
        print(json.dumps({"dpd_version": cl.dpd_version, "words": out},
                         ensure_ascii=False, indent=1))
        return 0
    print(f"# dpd {cl.dpd_version}")
    for e in out:
        print()
        simsapa_fmt.fmt_form(e["lookup"], fmt_args(), sys.stdout)
        if e["via"]:
            print(f"    ({e['via']})")
        for uid, table in (e.get("inflections") or {}).items():
            print(f"    inflections of {uid}:")
            for ln in table.splitlines():
                print(f"        {ln}")
        if "guesses" in e:
            g = e["guesses"]
            print("    guesses, not DPD's entry for this form (/dict_combined_search):")
            print(f"        headwords: {', '.join(g['headwords']) or 'none'}")
            if g["deconstructor"]:
                print(f"        deconstructor: {'; '.join(map(str, g['deconstructor']))}")
    return 0


# ------------------------------------------------------------------ gloss

def gloss_lines(cl, lines):
    """[(label, pali)] → [{label, pali, tokens}] with every token's DPD data."""
    clean = [(lab, " ".join(re.sub(r"\((?:×|x)\d+\)", "", p).split())) for lab, p in lines]
    clean = [(lab, p) for lab, p in clean if p]
    data = cl.gloss_exact("\n\n".join(p for _, p in clean))
    paras = data["paragraphs"]
    if len(paras) != len(clean):
        raise SimsapaError(f"/gloss_text returned {len(paras)} paragraphs for {len(clean)} lines")
    tokens = [t for p in paras for t in p["tokens"]]
    redo = [t["original_word"] for t in tokens
            if t["lookup"]["status"] == "not_found" or is_elided(t["original_word"])]
    known = {t["original_word"]: t["lookup"] for t in tokens if t["original_word"] not in redo}
    found = resolve(cl, redo, known) if redo else {}
    occ = index.occurrences(index.parsed(index.all_texts()))
    out = []
    for (label, pali), p in zip(clean, paras):
        toks = []
        for t in p["tokens"]:
            w = t["original_word"]
            res, via = found.get(w, (t["lookup"], None))
            toks.append({"token_index": t["token_index"], "word": w, "status": res["status"],
                         "via": via, "lookup": res,
                         "settled_rows": [{"row": r, "count": c, "first": f}
                                          for r, c, f in index.common_rows(occ, w.lower())]})
        out.append({"line": label, "pali": pali, "tokens": toks})
    return out


def cmd_gloss(cl, a):
    lines = []
    if a.text is not None:
        lines = [(f"text {i}", t) for i, t in enumerate(a.text.split("\n\n"))]
    for f in a.files:
        p = Path(f)
        cf = parse_file(p, options=books.options_for_text(p))
        lines += [(f"{_rel(p)}:{u.line}", u.pali) for u in cf.units]
    if not lines:
        raise SimsapaError("nothing to gloss: give FILEs or --text")
    out = gloss_lines(cl, lines)
    if not a.text_output:
        print(json.dumps({"dpd_version": cl.dpd_version, "lines": out},
                         ensure_ascii=False, indent=1))
        return 0
    print(f"# dpd {cl.dpd_version}")
    for ln in out:
        print(f"\n## {ln['line']}: {ln['pali']}")
        for t in ln["tokens"]:
            print(f"\n[{t['token_index']}] ", end="")
            simsapa_fmt.fmt_form(t["lookup"], fmt_args(), sys.stdout)
            if t["via"]:
                print(f"    ({t['via']})")
            for r in t["settled_rows"]:
                print(f"    settled: {r['row']}    ← {r['count']}×, first {r['first']}")
    return 0


# ------------------------------------------------------------------ main

def main(argv=None):
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0],
                                 epilog=f"See {API_DOC} and docs/quality-process.md.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lookup", help="DPD's headwords, splits and parses for word forms")
    p.add_argument("words", nargs="+", metavar="WORD")
    p.add_argument("--json", action="store_true")
    p.add_argument("--inflections", action="store_true",
                   help="add each headword's inflection table (/word.json)")
    p.add_argument("--widen", action="store_true",
                   help="for a form DPD lacks, show /dict_combined_search's guesses")
    p = sub.add_parser("check", help="check the word tables against DPD")
    p.add_argument("files", nargs="+", metavar="FILE")
    p.add_argument("--strict", action="store_true", help="exit 1 on unreviewed candidates too")
    p.add_argument("--json", action="store_true")
    p.add_argument("--ledger", default=str(LEDGER),
                   help="reviewed items (default: checks/dpd-review.tsv)")
    p = sub.add_parser("gloss", help="DPD candidate data for each word of Pāli lines")
    p.add_argument("files", nargs="*", metavar="FILE")
    p.add_argument("--text", help="Pāli text instead of files; paragraphs split on blank lines")
    p.add_argument("--text-output", action="store_true", help="readable text instead of JSON")
    a = ap.parse_args(argv)
    try:
        return {"lookup": cmd_lookup, "check": cmd_check, "gloss": cmd_gloss}[a.cmd](client(), a)
    except SimsapaError as e:
        print(f"simsapa.py: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
