def solve_eight_queens() -> list[str]:
    """Solves the 8-queens puzzle using recursive backtracking, returning solutions in ascending order."""
    solutions: list[str] = []

    def is_safe(queens: list[int], col: int, row: int) -> bool:
        for c, r in enumerate(queens):
            if r == row or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(queens: list[int]):
        col = len(queens)
        if col == 8:
            solutions.append("".join(str(r) for r in queens))
            return

        for row in range(1, 9):
            if is_safe(queens, col, row):
                queens.append(row)
                backtrack(queens)
                queens.pop()

    backtrack([])
    solutions.sort()
    return solutions


def eight_queens():
    for sol in solve_eight_queens():
        print(sol)


if __name__ == "__main__":
    eight_queens()
