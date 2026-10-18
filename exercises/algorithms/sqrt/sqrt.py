def integer_sqrt(n: int) -> int:
    """Returns integer square root if n is a perfect square, else 0."""
    if n <= 0:
        return 0
    root = int(n**0.5)
    return root if root * root == n else 0
