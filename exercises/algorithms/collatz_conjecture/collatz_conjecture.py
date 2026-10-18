def collatz_conjecture(n: int) -> int:
    """Returns number of steps to reach 1 under the 3n + 1 problem."""
    if n <= 0:
        return 0
    steps = 0
    current = n
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        steps += 1
    return steps
