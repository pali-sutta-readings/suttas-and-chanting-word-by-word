import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))


class SmokeTest(unittest.TestCase):
    def test_import_chantlib(self):
        import chantlib

        self.assertTrue(chantlib.__doc__)


if __name__ == "__main__":
    unittest.main()
