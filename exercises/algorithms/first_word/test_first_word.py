import unittest
from first_word import first_word


class TestFirstWord(unittest.TestCase):
    def test_first_word(self):
        self.assertEqual(first_word("hello world"), "hello")
        self.assertEqual(first_word("   spaced   out words  "), "spaced")
        self.assertEqual(first_word(""), "")


if __name__ == "__main__":
    unittest.main()
