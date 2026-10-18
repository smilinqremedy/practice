import json
import unittest
from object_to_json import User, create_new_user, user_to_json


class TestObjectToJson(unittest.TestCase):
    def test_valid_user_from_json(self):
        registration = '{"username": "mario", "email": "mario@me.it"}'
        user = create_new_user(registration)
        self.assertEqual(user.username, "mario")
        self.assertEqual(user.email, "mario@me.it")
        self.assertEqual(user_to_json(user), registration)

    def test_valid_user_from_dict(self):
        registration = {"username": "luigi", "email": "luigi@me.it"}
        user = create_new_user(registration)
        self.assertEqual(user.username, "luigi")
        self.assertEqual(user.email, "luigi@me.it")
        self.assertEqual(json.loads(user_to_json(user)), registration)

    def test_invalid_user(self):
        registration = '{"city": "Rome", "country": "Italy"}'
        user = create_new_user(registration)
        self.assertEqual(user_to_json(user), "{}")


if __name__ == "__main__":
    unittest.main()
