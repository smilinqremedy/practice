import datetime as dt
import os
import unittest
from write_file import to_do


class TestWriteFile(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")

    def test_to_do(self):
        sample_list = [
            (dt.date(2022, 6, 1), "fix the seat"),
            (dt.date(2022, 6, 2), "take the trash"),
        ]
        to_do(sample_list)
        self.assertTrue(os.path.exists("output.txt"))

        with open("output.txt", "r", encoding="utf-8") as f:
            content = f.read()

        expected = (
            "Wednesday 01 June 2022: fix the seat\n"
            "Thursday 02 June 2022: take the trash\n"
        )
        self.assertEqual(content, expected)


if __name__ == "__main__":
    unittest.main()
