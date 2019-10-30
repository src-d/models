import json
from pathlib import Path
import unittest

class TestIndexSanity(unittest.TestCase):

    def setUp(self):
        self.root = Path(".")
        with (self.root / "index.json").open() as fin:
            self.index = json.load(fin)

    def test_meta_dir(self):
        for model_kind in self.index["meta"]:
            self.assertTrue((self.root / model_kind).exists())

if __name__ == '__main__':
    unittest.main()
