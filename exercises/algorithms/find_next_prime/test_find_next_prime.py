import unittest
from find_next_prime import find_next_prime


class TestFindNextPrime(unittest.TestCase):
    def test_find_next_prime(self):
        self.assertEqual(find_next_prime(-5), 2)
        self.assertEqual(find_next_prime(0), 2)
        self.assertEqual(find_next_prime(2), 2)
        self.assertEqual(find_next_prime(4), 5)
        self.assertEqual(find_next_prime(14), 17)
        self.assertEqual(find_next_prime(17), 17)


if __name__ == "__main__":
    unittest.main()
