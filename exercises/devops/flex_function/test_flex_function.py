import unittest
from flex_function import create_person


class TestFlexFunction(unittest.TestCase):
    def test_create_person_positional(self):
        person = create_person("Kevin", "Boulin", 34, "male")
        expected = {
            "first_name": "Kevin",
            "last_name": "Boulin",
            "age": 34,
            "gender": "male",
            "size": 1.83,
            "job": "taxidermist",
        }
        self.assertEqual(person, expected)

    def test_create_person_keywords(self):
        person = create_person(
            "Alice",
            "Smith",
            age=28,
            gender="female",
            size=1.70,
            job="developer",
        )
        self.assertEqual(person["first_name"], "Alice")
        self.assertEqual(person["job"], "developer")
        self.assertEqual(person["size"], 1.70)

    def test_first_name_positional_only(self):
        with self.assertRaises(TypeError):
            # first_name must be positional only
            create_person(first_name="Kevin", last_name="Boulin")


if __name__ == "__main__":
    unittest.main()
