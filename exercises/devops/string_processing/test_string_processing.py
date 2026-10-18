import unittest
from string_processing import tokenize


class TestStringProcessing(unittest.TestCase):
    def test_tokenize(self):
        sentence = "It's not possible, you can't ask for a raise"
        expected = [
            "it",
            "s",
            "not",
            "possible",
            "you",
            "can",
            "t",
            "ask",
            "for",
            "a",
            "raise",
        ]
        self.assertEqual(tokenize(sentence), expected)

    def test_tokenize_numbers_and_symbols(self):
        self.assertEqual(
            tokenize("it's not 3"),
            ["it", "s", "not", "3"],
        )

    def test_empty_string(self):
        self.assertEqual(tokenize(""), [])


if __name__ == "__main__":
    unittest.main()
