import unittest
from clean_the_list import clean_list


class TestCleanTheList(unittest.TestCase):
    def test_clean_list_with_milk(self):
        shopping_list = ["tomatoes", "pastas", "milk", "salt"]
        expected = ["1/ Tomatoes", "2/ Pastas", "3/ Milk", "4/ Salt"]
        self.assertEqual(clean_list(shopping_list), expected)

    def test_clean_list_without_milk(self):
        shopping_list = ["  apple ", "banana  "]
        expected = ["1/ Apple", "2/ Banana", "3/ Milk"]
        self.assertEqual(clean_list(shopping_list), expected)

    def test_empty_list(self):
        self.assertEqual(clean_list([]), [])


if __name__ == "__main__":
    unittest.main()
