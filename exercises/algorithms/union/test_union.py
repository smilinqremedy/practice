import unittest
from union import union


class TestUnion(unittest.TestCase):
    def test_union(self):
        self.assertEqual(
            union("zpadinton", "paqefwtdjetyiytjneytjoeyjnejeyj"),
            "zpadintoqefwjy",
        )
        self.assertEqual(union("abc", "def"), "abcdef")
        self.assertEqual(union("", ""), "")


if __name__ == "__main__":
    unittest.main()
