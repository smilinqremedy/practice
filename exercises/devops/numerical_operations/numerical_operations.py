import math


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def power(a: int | float, b: int | float) -> int | float:
    return a**b


def square_root(a: int | float) -> float:
    return math.sqrt(a)


if __name__ == "__main__":
    print(add(2, 2))
    print(subtract(10, 5))
    print(multiply(3, 4))
    print(power(3, 3))
    print(square_root(3))
