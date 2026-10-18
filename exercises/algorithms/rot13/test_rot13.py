import unittest
from rot13 import rot13


class TestRot13(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot13("abc"), "nop")
        self.assertEqual(rot13("Hello, World!"), "Uryyb, Jbeyq!")
        self.assertEqual(rot13("Uryyb, Jbeyq!"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
