import unittest
from concat_string import concat


class TestConcatString(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(concat("Hello", "World"), "Hello, World")
        self.assertEqual(concat("Foo", "Bar"), "Foo, Bar")


if __name__ == "__main__":
    unittest.main()
