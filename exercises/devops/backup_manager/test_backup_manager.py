import os
import shutil
import subprocess
import sys
import unittest


class TestBackupManager(unittest.TestCase):
    def setUp(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def cleanup(self):
        pid_file = os.path.join(self.script_dir, ".service.pid")
        if os.path.exists(pid_file):
            subprocess.run(
                [sys.executable, "backup_manager.py", "stop"],
                cwd=self.script_dir,
            )
        for p in ["backup_schedules.txt", ".service.pid"]:
            full_path = os.path.join(self.script_dir, p)
            if os.path.exists(full_path):
                os.remove(full_path)
        for d in ["logs", "backups", "dummy_dir"]:
            full_dir = os.path.join(self.script_dir, d)
            if os.path.exists(full_dir):
                shutil.rmtree(full_dir)

    def test_create_and_list_and_delete(self):
        # Create schedules
        subprocess.run(
            [sys.executable, "backup_manager.py", "create", "test;14:00;backup1"],
            cwd=self.script_dir,
        )
        subprocess.run(
            [sys.executable, "backup_manager.py", "create", "test2;15:00;backup2"],
            cwd=self.script_dir,
        )

        # List schedules
        proc = subprocess.run(
            [sys.executable, "backup_manager.py", "list"],
            cwd=self.script_dir,
            capture_output=True,
            text=True,
        )
        self.assertIn("0: test;14:00;backup1", proc.stdout)
        self.assertIn("1: test2;15:00;backup2", proc.stdout)

        # Delete schedule
        subprocess.run(
            [sys.executable, "backup_manager.py", "delete", "0"],
            cwd=self.script_dir,
        )
        proc = subprocess.run(
            [sys.executable, "backup_manager.py", "list"],
            cwd=self.script_dir,
            capture_output=True,
            text=True,
        )
        self.assertNotIn("backup1", proc.stdout)
        self.assertIn("0: test2;15:00;backup2", proc.stdout)

    def test_service_backup_execution(self):
        if self.script_dir not in sys.path:
            sys.path.insert(0, self.script_dir)
        import backup_service

        dummy_path = os.path.join(self.script_dir, "dummy_dir")
        os.makedirs(dummy_path, exist_ok=True)
        with open(os.path.join(dummy_path, "sample.txt"), "w") as f:
            f.write("hello world")

        old_cwd = os.getcwd()
        try:
            os.chdir(self.script_dir)
            backup_service.perform_backup("dummy_dir", "sample_backup")
            self.assertTrue(os.path.exists(os.path.join(self.script_dir, "backups/sample_backup.tar")))

            proc = subprocess.run(
                [sys.executable, "backup_manager.py", "backups"],
                cwd=self.script_dir,
                capture_output=True,
                text=True,
            )
            self.assertIn("sample_backup.tar", proc.stdout)
        finally:
            os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
