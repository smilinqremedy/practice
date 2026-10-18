import json
from typing import Any


class User:
    username = "user"
    email = "something@mail.com"


def create_new_user(data: dict[str, Any] | str) -> User:
    """Creates a User instance with username/email if valid, otherwise returns default User."""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            return User()

    user = User()
    if isinstance(data, dict) and "username" in data and "email" in data:
        user.username = data["username"]
        user.email = data["email"]
    return user


def user_to_json(user: User) -> str:
    """Serializes user instance attributes to JSON string."""
    return json.dumps(user.__dict__)


if __name__ == "__main__":
    registration_0 = '{"username": "mario", "email": "mario@me.it"}'
    registration_1 = '{"city": "Rome", "country": "Italy"}'

    user_0 = create_new_user(registration_0)
    user_1 = create_new_user(registration_1)

    print(user_to_json(user_0))
    print(user_to_json(user_1))
