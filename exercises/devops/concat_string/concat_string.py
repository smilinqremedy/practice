def concat(string1: str, string2: str) -> str:
    """Concatenates two strings with a comma and space between them."""
    return f"{string1}, {string2}"


if __name__ == "__main__":
    s1 = "Hello"
    s2 = "World"
    print(concat(s1, s2))
