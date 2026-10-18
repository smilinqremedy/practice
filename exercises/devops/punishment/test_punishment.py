import unittest
from punishment import do_punishment


class TestPunishment(unittest.TestCase):
    def test_do_punishment(self):
        result = do_punishment("   The first half   ", "   and the second  ", 4)
        expected = (
            "The first half and the second.\n"
            "The first half and the second.\n"
            "The first half and the second.\n"
            "The first half and the second.\n"
        )
        self.assertEqual(result, expected)

    def test_zero_lines(self):
        self.assertEqual(do_punishment("Will not", "show", 0), "")

    def test_empty_strings(self):
        self.assertEqual(do_punishment("", "", 3), " .\n .\n .\n")


if __name__ == "__main__":
    unittest.main()
