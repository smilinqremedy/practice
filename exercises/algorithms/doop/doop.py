INT64_MIN = -(2**63)
INT64_MAX = 2**63 - 1


def doop(val1_str: str, op: str, val2_str: str) -> str:
    """Performs safe 64-bit integer arithmetic with division/modulo by zero handling."""
    try:
        a = int(val1_str)
        b = int(val2_str)
    except ValueError:
        return ""

    if not (INT64_MIN <= a <= INT64_MAX and INT64_MIN <= b <= INT64_MAX):
        return ""

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            return "No division by 0"
        res = int(a / b)
    elif op == "%":
        if b == 0:
            return "No modulo by 0"
        res = a % b
    else:
        return ""

    if not (INT64_MIN <= res <= INT64_MAX):
        return ""

    return str(res)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        out = doop(sys.argv[1], sys.argv[2], sys.argv[3])
        if out:
            print(out)
