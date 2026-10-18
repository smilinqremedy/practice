import unittest
from printcomb import print_comb


class TestPrintComb(unittest.TestCase):
    def test_print_comb(self):
        res = print_comb()
        parts = res.split(", ")
        # Number of combinations is 10 choose 3 = 120
        self.assertEqual(len(parts), 120)
        self.assertEqual(parts[0], "012")
        self.assertEqual(parts[-1], "789")
        for item in parts:
            self.assertEqual(len(item), 3)
            self.assertTrue(item[0] < item[1] < item[2])


if __name__ == "__main__":
    unittest.main()
