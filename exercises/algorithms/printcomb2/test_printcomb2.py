import unittest
from printcomb2 import print_comb2


class TestPrintComb2(unittest.TestCase):
    def test_print_comb2(self):
        res = print_comb2()
        parts = res.split(", ")
        # 100 choose 2 = 4950
        self.assertEqual(len(parts), 4950)
        self.assertEqual(parts[0], "00 01")
        self.assertEqual(parts[-1], "98 99")


if __name__ == "__main__":
    unittest.main()
