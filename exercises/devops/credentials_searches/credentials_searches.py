import json
import os
from typing import Any


def credentials_search() -> None:
    """Searches for 'password' and 'secret' keys in logs.json (including nested) and saves to credentials.json."""
    if not os.path.exists("logs.json"):
        return

    try:
        with open("logs.json", "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return
            data = json.loads(content)
    except Exception:
        return

    found_credentials: dict[str, Any] = {}

    def extract_keys(node: Any):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "password" and "password" not in found_credentials:
                    found_credentials["password"] = v
                elif k == "secret" and "secret" not in found_credentials:
                    found_credentials["secret"] = v
                extract_keys(v)
        elif isinstance(node, list):
            for item in node:
                extract_keys(item)

    extract_keys(data)

    if found_credentials:
        with open("credentials.json", "w", encoding="utf-8") as f:
            json.dump(found_credentials, f, indent=2)


if __name__ == "__main__":
    credentials_search()
