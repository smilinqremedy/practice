import unittest
from last_word import last_word


class TestLastWord(unittest.TestCase):
    def test_last_word(self):
        self.assertEqual(last_word("hello world"), "world")
        self.assertEqual(last_word("   spaced   out words  "), "words")
        self.assertEqual(last_word("single"), "single")
        self.assertEqual(last_word(""), "")


if __name__ == "__main__":
    unittest.main()
