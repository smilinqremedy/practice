import unittest
from eightqueens import solve_eight_queens


class TestEightQueens(unittest.TestCase):
    def test_solve_eight_queens(self):
        solutions = solve_eight_queens()
        # There are exactly 92 distinct solutions to the 8-queens problem
        self.assertEqual(len(solutions), 92)
        # Verify first and second solutions match standard order
        self.assertEqual(solutions[0], "15863724")
        self.assertEqual(solutions[1], "16837425")
        self.assertEqual(solutions[2], "17468253")
        # Ensure list is strictly sorted ascending
        self.assertEqual(solutions, sorted(solutions))


if __name__ == "__main__":
    unittest.main()
