import unittest
from doop import doop


class TestDoop(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(doop("1", "+", "1"), "2")
        self.assertEqual(doop("10", "-", "3"), "7")
        self.assertEqual(doop("3", "*", "4"), "12")
        self.assertEqual(doop("10", "/", "3"), "3")
        self.assertEqual(doop("10", "%", "3"), "1")

    def test_divide_and_modulo_by_zero(self):
        self.assertEqual(doop("1", "/", "0"), "No division by 0")
        self.assertEqual(doop("1", "%", "0"), "No modulo by 0")

    def test_invalid_and_overflow(self):
        self.assertEqual(doop("hello", "+", "1"), "")
        self.assertEqual(doop("1", "p", "1"), "")
        self.assertEqual(doop(str(2**63 - 1), "+", "1"), "")


if __name__ == "__main__":
    unittest.main()
