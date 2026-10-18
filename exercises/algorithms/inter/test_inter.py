import unittest
from inter import inter


class TestInter(unittest.TestCase):
    def test_inter(self):
        self.assertEqual(
            inter("padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"), "padinto"
        )
        self.assertEqual(inter("abc", "def"), "")
        self.assertEqual(inter("", "abc"), "")


if __name__ == "__main__":
    unittest.main()
