import os
import subprocess
import sys
import unittest


class TestSkipSecrets(unittest.TestCase):
    def setUp(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, "file.txt")
        self.out_path = os.path.join(self.script_dir, "out.txt")
        self._clean()

    def tearDown(self):
        self._clean()

    def _clean(self):
        for f in [self.file_path, self.out_path]:
            if os.path.exists(f):
                os.remove(f)

    def test_missing_argument(self):
        proc = subprocess.run(
            [sys.executable, "skip_secrets.py"],
            cwd=self.script_dir,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)

    def test_unreadable_file(self):
        proc = subprocess.run(
            [sys.executable, "skip_secrets.py", "nonexistent_file_xyz.txt"],
            cwd=self.script_dir,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)

    def test_filter_pineapple(self):
        content = (
            "A normal pizza \n"
            "Another normal pizza\n"
            "A pizza with pineapple\n"
            "Yet another very normal and delicious pizza\n"
        )
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(content)

        proc = subprocess.run(
            [sys.executable, "skip_secrets.py", "file.txt"],
            cwd=self.script_dir,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(os.path.exists(self.out_path))

        with open(self.out_path, "r", encoding="utf-8") as f:
            out_content = f.read()

        expected = (
            "A normal pizza \n"
            "Another normal pizza\n"
            "Yet another very normal and delicious pizza\n"
        )
        self.assertEqual(out_content, expected)


if __name__ == "__main__":
    unittest.main()
