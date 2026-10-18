def binary_addition(a: str, b: str) -> str:
    """Returns the sum of two binary strings as a binary string."""
    if not a and not b:
        return "0"
    val_a = int(a, 2) if a else 0
    val_b = int(b, 2) if b else 0
    return bin(val_a + val_b)[2:]
