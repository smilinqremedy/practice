from typing import Any


def create_person(
    first_name: str,
    last_name: str,
    /,
    age: int | None = None,
    gender: str | None = None,
    *,
    size: float = 1.83,
    job: str = "taxidermist",
) -> dict[str, Any]:
    """Creates person dict with positional-only, positional/keyword, and keyword-only params."""
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "size": size,
        "job": job,
    }


if __name__ == "__main__":
    person = create_person("Kevin", "Boulin", 34, "male")
    print(person)
