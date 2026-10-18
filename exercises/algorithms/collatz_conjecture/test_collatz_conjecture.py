import unittest
from collatz_conjecture import collatz_conjecture


class TestCollatzConjecture(unittest.TestCase):
    def test_collatz_conjecture(self):
        # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
        self.assertEqual(collatz_conjecture(6), 8)
        self.assertEqual(collatz_conjecture(1), 0)
        self.assertEqual(collatz_conjecture(0), 0)


if __name__ == "__main__":
    unittest.main()
