import sys


def check_candidates():
    if len(sys.argv) != 2:
        print("Error: wrong number of arguments")
        sys.exit(1)

    try:
        count = int(sys.argv[1])
    except ValueError:
        print("Error: wrong number of arguments")
        sys.exit(1)

    candidates: list[dict[str, str | int]] = []

    for _ in range(count):
        print("Add a new candidate:")
        name = input("name: ")
        age_str = input("age: ")
        age = int(age_str)
        candidates.append({"name": name, "age": age})

    for candidate in candidates:
        name = candidate["name"]
        age = candidate["age"]
        if age < 18:
            print(f"{name} is not eligible (underaged)")
        elif age > 60:
            print(f"{name} is not eligible (over the legal age)")
        else:
            print(f"{name} is eligible")


if __name__ == "__main__":
    check_candidates()
