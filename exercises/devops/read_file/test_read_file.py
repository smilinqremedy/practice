import json
import os
import tempfile
import unittest
from read_file import get_recipes


class TestReadFile(unittest.TestCase):
    def test_get_recipes(self):
        sample_data = [
            {"title": "Vegetable Lasagna", "people": 6},
            {"title": "Spicy Chicken Tacos", "people": 4},
        ]
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as f:
            json.dump(sample_data, f)
            temp_path = f.name

        try:
            recipes = get_recipes(temp_path)
            self.assertEqual(recipes, sample_data)
        finally:
            os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
