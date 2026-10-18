import os
import subprocess
import sys
import unittest


class TestCandidatesChecker(unittest.TestCase):
    def test_wrong_number_of_arguments(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        proc = subprocess.run(
            [sys.executable, "candidates_checker.py"],
            cwd=script_dir,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Error: wrong number of arguments", proc.stdout)

    def test_candidates_evaluation(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        inputs = "Edoardo\n17\nMichele\n60\nLea\n61\n"
        proc = subprocess.run(
            [sys.executable, "candidates_checker.py", "3"],
            cwd=script_dir,
            input=inputs,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Edoardo is not eligible (underaged)", proc.stdout)
        self.assertIn("Michele is eligible", proc.stdout)
        self.assertIn("Lea is not eligible (over the legal age)", proc.stdout)


if __name__ == "__main__":
    unittest.main()
