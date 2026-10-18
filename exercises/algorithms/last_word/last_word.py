def last_word(s: str) -> str:
    """Returns the last word of a string, or empty string."""
    words = s.split()
    return words[-1] if words else ""
