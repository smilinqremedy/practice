import json
from typing import Any


def get_recipes(file_name: str) -> list[dict[str, Any]]:
    """Reads a JSON file and loads recipes into a list of dictionaries."""
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    import sys

    fname = sys.argv[1] if len(sys.argv) > 1 else "recipes_data.json"
    print(get_recipes(fname))
