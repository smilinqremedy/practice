import unittest
from binary_addition import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_binary_addition(self):
        self.assertEqual(binary_addition("1010", "1011"), "10101")
        self.assertEqual(binary_addition("1", "1"), "10")
        self.assertEqual(binary_addition("0", "0"), "0")


if __name__ == "__main__":
    unittest.main()
