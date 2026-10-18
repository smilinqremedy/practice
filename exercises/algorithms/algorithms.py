"""Foundational 01-Edu algorithmic challenges implemented in idiomatic Python."""


def is_positive(n: int | float) -> bool:
    """Returns True if number is strictly positive, False otherwise."""
    return n > 0


def abs_val(n: int | float) -> int | float:
    """Returns absolute value of n without using built-in abs()."""
    if n < 0:
        return -n
    return n


def fibonacci(index: int) -> int:
    """Recursive Fibonacci implementation. Negative index returns -1."""
    if index < 0:
        return -1
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)


def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, False otherwise."""
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
    """Returns the smallest prime number greater than or equal to n."""
    if n <= 2:
        return 2
    candidate = n
    while not is_prime(candidate):
        candidate += 1
    return candidate


def integer_sqrt(n: int) -> int:
    """Returns integer square root if n is a perfect square, else 0."""
    if n <= 0:
        return 0
    root = int(n**0.5)
    return root if root * root == n else 0


def alphamirror(s: str) -> str:
    """Replaces each alphabetical character with opposite letter preserving case."""
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            result.append(chr(ord("z") - (ord(ch) - ord("a"))))
        elif "A" <= ch <= "Z":
            result.append(chr(ord("Z") - (ord(ch) - ord("A"))))
        else:
            result.append(ch)
    return "".join(result)


def rot13(s: str) -> str:
    """Rotates letters by 13 positions preserving case."""
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            result.append(chr(ord("a") + (ord(ch) - ord("a") + 13) % 26))
        elif "A" <= ch <= "Z":
            result.append(chr(ord("A") + (ord(ch) - ord("A") + 13) % 26))
        else:
            result.append(ch)
    return "".join(result)


def first_word(s: str) -> str:
    """Returns the first word of a string, or empty string."""
    words = s.split()
    return words[0] if words else ""


def last_word(s: str) -> str:
    """Returns the last word of a string, or empty string."""
    words = s.split()
    return words[-1] if words else ""


def reverse_string(s: str) -> str:
    """Reverses a string."""
    return s[::-1]


def wdmatch(s1: str, s2: str) -> str:
    """Returns s1 if all characters of s1 appear in s2 in sequential order, else ''."""
    it = iter(s2)
    return s1 if all(ch in it for ch in s1) else ""


def inter(s1: str, s2: str) -> str:
    """Returns characters present in both s1 and s2 without duplicates, preserving s1 order."""
    s2_set = set(s2)
    seen = set()
    res = []
    for ch in s1:
        if ch in s2_set and ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)


def union(s1: str, s2: str) -> str:
    """Returns unique characters from s1 followed by s2 in order of appearance."""
    seen = set()
    res = []
    for ch in s1 + s2:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)


def binary_addition(a: str, b: str) -> str:
    """Returns the sum of two binary strings as a binary string."""
    if not a and not b:
        return "0"
    val_a = int(a, 2) if a else 0
    val_b = int(b, 2) if b else 0
    return bin(val_a + val_b)[2:]


def collatz_conjecture(n: int) -> int:
    """Returns number of steps to reach 1 under the 3n + 1 problem."""
    if n <= 0:
        return 0
    steps = 0
    current = n
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        steps += 1
    return steps
