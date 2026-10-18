import unittest
from abs import is_positive, abs_val


class TestAbs(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(is_positive(10))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-5))

    def test_abs_val(self):
        self.assertEqual(abs_val(42), 42)
        self.assertEqual(abs_val(-42), 42)
        self.assertEqual(abs_val(0), 0)


if __name__ == "__main__":
    unittest.main()
