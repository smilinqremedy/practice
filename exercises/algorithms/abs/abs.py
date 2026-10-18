def is_positive(n: int | float) -> bool:
    """Returns True if number is strictly positive, False otherwise."""
    return n > 0


def abs_val(n: int | float) -> int | float:
    """Returns absolute value of n without using built-in abs()."""
    if n < 0:
        return -n
    return n
