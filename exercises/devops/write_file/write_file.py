import datetime as dt


def to_do(to_do_list: list[tuple[dt.date, str]]) -> None:
    """Formats date and task into 'output.txt' as 'Weekday DD Month YYYY: task'."""
    with open("output.txt", "w", encoding="utf-8") as f:
        for date_val, task in to_do_list:
            formatted_date = date_val.strftime("%A %d %B %Y")
            f.write(f"{formatted_date}: {task}\n")


if __name__ == "__main__":
    sample_list = [
        (dt.date(2022, 6, 1), "fix the seat"),
        (dt.date(2022, 6, 2), "take the trash"),
    ]
    to_do(sample_list)
