def modulo(a: int | float, b: int | float) -> int | float:
    if b == 0:
        return 0
    return a % b


def divide(a: int | float, b: int | float) -> float | int:
    if b == 0:
        return 0
    return a / b


def integer_division(a: int | float, b: int | float) -> int:
    if b == 0:
        return 0
    return int(a // b)


if __name__ == "__main__":
    print(modulo(10, 3))
    print(divide(10, 3))
    print(divide(10, 0))
    print(integer_division(10, 3))
