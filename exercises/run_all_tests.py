#!/usr/bin/env python3
"""Unified test runner for all 01-Edu Python exercises and algorithms."""

import os
import sys
import unittest


def run_all_tests():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Walk all directories and discover test_*.py files, adding each dir to sys.path
    for dirpath, _, filenames in os.walk(root_dir):
        test_files = [f for f in filenames if f.startswith("test_") and f.endswith(".py")]
        if test_files:
            if dirpath not in sys.path:
                sys.path.insert(0, dirpath)
            for test_file in test_files:
                sub_suite = loader.discover(
                    start_dir=dirpath,
                    pattern=test_file,
                    top_level_dir=dirpath,
                )
                suite.addTests(sub_suite)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
