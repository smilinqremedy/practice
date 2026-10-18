def first_word(s: str) -> str:
    """Returns the first word of a string, or empty string."""
    words = s.split()
    return words[0] if words else ""
