def do_punishment(first_part: str, second_part: str, nb_lines: int) -> str:
    """Concatenates trimmed parts with space and period, repeating for nb_lines times."""
    first = first_part.strip()
    second = second_part.strip()
    sentence = f"{first} {second}.\n"
    return sentence * nb_lines


if __name__ == "__main__":
    print(do_punishment("   The first half   ", "   and the second  ", 4), end="")
    print(do_punishment("Will not", "show", 0), end="")
    print(do_punishment("", "", 3), end="")
