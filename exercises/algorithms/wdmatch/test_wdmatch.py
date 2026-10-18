import unittest
from wdmatch import wdmatch


class TestWdmatch(unittest.TestCase):
    def test_wdmatch(self):
        self.assertEqual(wdmatch("123", "123"), "123")
        self.assertEqual(wdmatch("faya", "fgvvfdxcacpolhyghbreda"), "faya")
        self.assertEqual(wdmatch("faya", "fgvvfdxcacpolhyghbred"), "")
        self.assertEqual(
            wdmatch("quarante deux", "qfqfsudf arzgsayns tsregfdgs sjytdekuoixq "),
            "quarante deux",
        )


if __name__ == "__main__":
    unittest.main()
