def remember_the_apple(shopping_list: list[str]) -> list[str]:
    """Ensures 'apple' is in the shopping list if not empty."""
    if not shopping_list:
        return []

    items = list(shopping_list)
    if "apple" not in items:
        items.append("apple")
    return items


if __name__ == "__main__":
    list_with_apple = ["tomatoes", "pastas", "apple", "salt"]
    list_without_apple = ["tomatoes", "pastas", "salt"]
    print(remember_the_apple(list_with_apple))
    print(remember_the_apple(list_without_apple))
