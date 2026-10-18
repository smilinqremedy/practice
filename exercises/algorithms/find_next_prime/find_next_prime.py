def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_next_prime(n: int) -> int:
    """Returns smallest prime greater than or equal to n."""
    if n <= 2:
        return 2
    candidate = n
    while not is_prime(candidate):
        candidate += 1
    return candidate
