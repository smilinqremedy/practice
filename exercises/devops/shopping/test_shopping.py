import unittest
from shopping import remember_the_apple


class TestShopping(unittest.TestCase):
    def test_list_with_apple(self):
        shopping_list = ["tomatoes", "pastas", "apple", "salt"]
        self.assertEqual(remember_the_apple(shopping_list), shopping_list)

    def test_list_without_apple(self):
        shopping_list = ["tomatoes", "pastas", "salt"]
        expected = ["tomatoes", "pastas", "salt", "apple"]
        self.assertEqual(remember_the_apple(shopping_list), expected)

    def test_empty_list(self):
        self.assertEqual(remember_the_apple([]), [])


if __name__ == "__main__":
    unittest.main()
