def print_comb2() -> str:
    """Generates all combinations of two two-digit numbers in ascending order."""
    combinations = []
    for i in range(100):
        for j in range(i + 1, 100):
            combinations.append(f"{i:02d} {j:02d}")
    return ", ".join(combinations)


if __name__ == "__main__":
    print(print_comb2())
