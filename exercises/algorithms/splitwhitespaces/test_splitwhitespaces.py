import unittest
from splitwhitespaces import split_white_spaces


class TestSplitWhiteSpaces(unittest.TestCase):
    def test_split_white_spaces(self):
        self.assertEqual(
            split_white_spaces("Hello how are you?"),
            ["Hello", "how", "are", "you?"],
        )
        self.assertEqual(
            split_white_spaces("Tab\tSeparated\nAnd\rNewline"),
            ["Tab", "Separated", "And", "Newline"],
        )
        self.assertEqual(split_white_spaces(""), [])


if __name__ == "__main__":
    unittest.main()
