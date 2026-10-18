import json
import os
import unittest
from credentials_searches import credentials_search


class TestCredentialsSearches(unittest.TestCase):
    def tearDown(self):
        for f in ["logs.json", "credentials.json"]:
            if os.path.exists(f):
                os.remove(f)

    def test_both_keys_found(self):
        data = {
            "password": "test_password",
            "other": "value",
            "secret": "test_secret",
        }
        with open("logs.json", "w") as f:
            json.dump(data, f)

        credentials_search()
        self.assertTrue(os.path.exists("credentials.json"))
        with open("credentials.json", "r") as f:
            res = json.load(f)
        self.assertEqual(res["password"], "test_password")
        self.assertEqual(res["secret"], "test_secret")

    def test_nested_keys(self):
        data = {"server": {"auth": {"password": "nested_pass"}}}
        with open("logs.json", "w") as f:
            json.dump(data, f)

        credentials_search()
        self.assertTrue(os.path.exists("credentials.json"))
        with open("credentials.json", "r") as f:
            res = json.load(f)
        self.assertEqual(res, {"password": "nested_pass"})

    def test_missing_file_or_keys(self):
        credentials_search()
        self.assertFalse(os.path.exists("credentials.json"))

        with open("logs.json", "w") as f:
            json.dump({"other": 123}, f)
        credentials_search()
        self.assertFalse(os.path.exists("credentials.json"))


if __name__ == "__main__":
    unittest.main()
