def print_comb() -> str:
    """Generates all unique combinations of three different digits (i < j < k)."""
    combinations = []
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                combinations.append(f"{i}{j}{k}")
    return ", ".join(combinations)


if __name__ == "__main__":
    print(print_comb())
