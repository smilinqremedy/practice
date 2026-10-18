import unittest
from hello_python import say_hello_python


class TestHelloPython(unittest.TestCase):
    def test_say_hello_python(self):
        self.assertEqual(say_hello_python(), "Hello Python!")


if __name__ == "__main__":
    unittest.main()
