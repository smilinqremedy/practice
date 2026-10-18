import unittest
from string_tokenizer_count import tokenizer_counter


class TestStringTokenizerCount(unittest.TestCase):
    def test_tokenizer_counter(self):
        s = "This is a test sentence, with various words and 123 numbers!"
        expected = {
            "123": 1,
            "a": 1,
            "and": 1,
            "is": 1,
            "numbers": 1,
            "sentence": 1,
            "test": 1,
            "this": 1,
            "various": 1,
            "with": 1,
            "words": 1,
        }
        result = tokenizer_counter(s)
        self.assertEqual(result, expected)
        # Ensure alphabetical ordering of keys
        self.assertEqual(list(result.keys()), sorted(result.keys()))


if __name__ == "__main__":
    unittest.main()
