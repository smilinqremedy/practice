import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("antigravity"), "ytivargitna")
        self.assertEqual(reverse_string(""), "")


if __name__ == "__main__":
    unittest.main()
