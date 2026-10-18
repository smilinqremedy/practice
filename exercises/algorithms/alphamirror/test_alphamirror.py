import unittest
from alphamirror import alphamirror


class TestAlphaMirror(unittest.TestCase):
    def test_alphamirror(self):
        self.assertEqual(alphamirror("abc"), "zyx")
        self.assertEqual(
            alphamirror("My horse is Amazing."), "Nb slihv rh Znzarmt."
        )
        self.assertEqual(alphamirror(""), "")


if __name__ == "__main__":
    unittest.main()
