import json


def merge_two(first_dict: dict[str, int]) -> str:
    """Prompts for key/value pairs until key=='exit', merges with first_dict, and returns JSON string."""
    new_dict: dict[str, int] = {}

    while True:
        print("Add a new entry:")
        key = input("key: ")
        if key == "exit":
            break
        val_str = input("value: ")
        new_dict[key] = int(val_str)

    merged = {**first_dict, **new_dict}
    return json.dumps(merged)


if __name__ == "__main__":
    first = {"Bob": 36, "Louise": 23, "Lea": 34}
    print(merge_two(first))
