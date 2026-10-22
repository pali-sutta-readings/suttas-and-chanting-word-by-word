"""Shared text normalisation for the chant tools.

The character rules are in docs/style-spec.md §2 (niggahīta, apostrophe) and
§10 (NFC, the Pāli alphabet, tone marks).
"""

import re
import unicodedata

# The Pāli alphabet (style spec §10), as single letters.
PALI_LETTERS = frozenset("aāiīuūeokgṅcjñṭḍṇtdnpbmyrlḷvshṁ")

# Tone marks of the Amaravati chanting book (U+A700–U+A71F).
TONE_MARKS = re.compile("[꜀-ꜟ]")

# Letters that occur in Sanskrit but never in Pāli.
SANSKRIT_LETTERS = re.compile("[śṣṛṝḹŚṢṚ]")

APOSTROPHES = "'’ʼ`"


def nfc(s):
    return unicodedata.normalize("NFC", s)


def fold_niggahita(s):
    """Write every niggahīta as ṁ (ṃ, Ṃ and ŋ are other spellings of it)."""
    return s.replace("ṃ", "ṁ").replace("Ṃ", "Ṁ").replace("ŋ", "ṁ")


def is_pali_letter(ch):
    return ch.lower() in PALI_LETTERS


def pali_letters_only(s):
    """Lower case; keep Pāli letters and single spaces, drop everything else.

    Apostrophes are dropped without a space, so *sabb'ītiyo* stays one word.
    """
    s = TONE_MARKS.sub("", fold_niggahita(nfc(s))).lower()
    for a in APOSTROPHES:
        s = s.replace(a, "")
    s = "".join(ch if ch in PALI_LETTERS else " " for ch in s)
    return " ".join(s.split())


def norm_line(s):
    """A Pāli line reduced for comparison: letters only, no spaces.

    `(×3)` and other repeat marks are removed, square brackets are dropped
    with their words kept, and *…pe…* elision marks are removed. Spaces,
    hyphens and apostrophes do not count, so sandhi spelling and word
    division never make two lines differ.
    """
    s = fold_niggahita(nfc(s)).lower()
    s = re.sub(r"\((?:×|x)\d\)", "", s)
    s = re.sub(r"…?\s*pe\s*…|…|\.\.\.", "", s)
    return pali_letters_only(s).replace(" ", "")
