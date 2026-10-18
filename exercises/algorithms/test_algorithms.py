import unittest
from algorithms import (
    abs_val,
    alphamirror,
    binary_addition,
    collatz_conjecture,
    fibonacci,
    find_next_prime,
    first_word,
    integer_sqrt,
    inter,
    is_positive,
    is_prime,
    last_word,
    reverse_string,
    rot13,
    union,
    wdmatch,
)


class TestAlgorithms(unittest.TestCase):
    def test_abs_and_positive(self):
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-3))
        self.assertEqual(abs_val(-42), 42)
        self.assertEqual(abs_val(0), 0)
        self.assertEqual(abs_val(17), 17)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(-2), -1)

    def test_prime_functions(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(15))
        self.assertEqual(find_next_prime(14), 17)
        self.assertEqual(find_next_prime(17), 17)

    def test_integer_sqrt(self):
        self.assertEqual(integer_sqrt(4), 2)
        self.assertEqual(integer_sqrt(9), 3)
        self.assertEqual(integer_sqrt(5), 0)

    def test_alphamirror(self):
        self.assertEqual(alphamirror("abc"), "zyx")
        self.assertEqual(
            alphamirror("My horse is Amazing."), "Nb slihv rh Znzarmt."
        )

    def test_rot13(self):
        self.assertEqual(rot13("abc"), "nop")
        self.assertEqual(rot13("Hello, World!"), "Uryyb, Jbeyq!")

    def test_words_and_reversal(self):
        self.assertEqual(first_word("  hello world  "), "hello")
        self.assertEqual(last_word("  hello world  "), "world")
        self.assertEqual(reverse_string("antigravity"), "ytivargitna")

    def test_wdmatch(self):
        self.assertEqual(wdmatch("faya", "fgvvfdxcacpolhyghbreda"), "faya")
        self.assertEqual(wdmatch("faya", "fgvvfdxcacpolhyghbred"), "")
        self.assertEqual(
            wdmatch("quarante deux", "qfqfsudf arzgsayns tsregfdgs sjytdekuoixq "),
            "quarante deux",
        )

    def test_inter_and_union(self):
        self.assertEqual(inter("padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"), "padinto")
        self.assertEqual(union("zpadinton", "paqefwtdjetyiytjneytjoeyjnejeyj"), "zpadintoqefwjy")

    def test_binary_addition(self):
        self.assertEqual(binary_addition("1010", "1011"), "10101")
        self.assertEqual(binary_addition("0", "0"), "0")

    def test_collatz_conjecture(self):
        # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
        self.assertEqual(collatz_conjecture(6), 8)
        self.assertEqual(collatz_conjecture(1), 0)


if __name__ == "__main__":
    unittest.main()
