import unittest
import math
from numerical_operations import add, subtract, multiply, power, square_root


class TestNumericalOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-1, 5), 4)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_power(self):
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(2, 0), 1)

    def test_square_root(self):
        self.assertAlmostEqual(square_root(3), math.sqrt(3))
        self.assertAlmostEqual(square_root(9), 3.0)


if __name__ == "__main__":
    unittest.main()
