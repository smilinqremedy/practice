import unittest
from custom_calendar import day_from_number, day_to_number


class TestCustomCalendar(unittest.TestCase):
    def test_day_from_number(self):
        self.assertEqual(day_from_number(1), "Monday")
        self.assertEqual(day_from_number(2), "Tuesday")
        self.assertEqual(day_from_number(7), "Sunday")
        self.assertIsNone(day_from_number(0))
        self.assertIsNone(day_from_number(8))
        self.assertIsNone(day_from_number(1000))

    def test_day_to_number(self):
        self.assertEqual(day_to_number("Monday"), 1)
        self.assertEqual(day_to_number("Sunday"), 7)
        self.assertIsNone(day_to_number("invalid day"))
        self.assertIsNone(day_to_number(""))


if __name__ == "__main__":
    unittest.main()
