import json
import unittest
from unittest.mock import patch
from merge_two import merge_two


class TestMergeTwo(unittest.TestCase):
    def test_merge_two(self):
        first = {"Bob": 36, "Louise": 23, "Lea": 34}
        user_inputs = ["Louise", "44", "Romolo", "30", "Lea", "22", "exit"]

        with patch("builtins.input", side_effect=user_inputs):
            result = merge_two(first)

        parsed = json.loads(result)
        expected = {"Bob": 36, "Louise": 44, "Lea": 22, "Romolo": 30}
        self.assertEqual(parsed, expected)


if __name__ == "__main__":
    unittest.main()
