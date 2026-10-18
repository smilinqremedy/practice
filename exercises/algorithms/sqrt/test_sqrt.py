import unittest
from sqrt import integer_sqrt


class TestSqrt(unittest.TestCase):
    def test_integer_sqrt(self):
        self.assertEqual(integer_sqrt(4), 2)
        self.assertEqual(integer_sqrt(9), 3)
        self.assertEqual(integer_sqrt(16), 4)
        self.assertEqual(integer_sqrt(25), 5)
        self.assertEqual(integer_sqrt(5), 0)
        self.assertEqual(integer_sqrt(-4), 0)
        self.assertEqual(integer_sqrt(0), 0)


if __name__ == "__main__":
    unittest.main()
