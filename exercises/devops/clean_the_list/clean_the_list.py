def clean_list(shopping_list: list[str]) -> list[str]:
    """Cleans a shopping list: strips whitespace, capitalizes, adds milk if missing, and numbers items."""
    if not shopping_list:
        return []

    # Copy list so we don't mutate input unexpectedly
    items = list(shopping_list)

    # Check if milk is present (case-insensitive and stripped)
    has_milk = any(item.strip().lower() == "milk" for item in items)
    if not has_milk:
        items.append("milk")

    result = []
    for idx, item in enumerate(items, start=1):
        cleaned_item = item.strip().capitalize()
        result.append(f"{idx}/ {cleaned_item}")

    return result


if __name__ == "__main__":
    shopping_list = ["tomatoes", "pastas", "milk", "salt"]
    print(clean_list(shopping_list))
