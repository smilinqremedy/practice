DAYS: dict[int, str] = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

REV_DAYS: dict[str, int] = {v: k for k, v in DAYS.items()}


def day_from_number(day_number: int) -> str | None:
    """Converts day index (1-7) to day word, or None if invalid."""
    return DAYS.get(day_number, None)


def day_to_number(day: str) -> int | None:
    """Converts day word to day index (1-7), or None if invalid."""
    return REV_DAYS.get(day, None)


if __name__ == "__main__":
    print(day_from_number(2))
    print(day_from_number(1))
    print(day_from_number(1000))
    print(day_to_number("Sunday"))
    print(day_to_number("invalid day"))
