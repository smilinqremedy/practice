import unittest
from numerical_operations_the_return import modulo, divide, integer_division


class TestNumericalOperationsTheReturn(unittest.TestCase):
    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 0), 0)
        self.assertEqual(modulo(15, 5), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 3), 10 / 3)
        self.assertEqual(divide(10, 0), 0)
        self.assertEqual(divide(0, 5), 0)

    def test_integer_division(self):
        self.assertEqual(integer_division(10, 3), 3)
        self.assertEqual(integer_division(10, 0), 0)
        self.assertEqual(integer_division(7, 2), 3)


if __name__ == "__main__":
    unittest.main()
