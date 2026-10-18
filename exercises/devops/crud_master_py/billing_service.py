import json
import sqlite3
from typing import Any


class BillingDB:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    number_of_items INTEGER NOT NULL,
                    total_amount REAL NOT NULL
                )
            """
            )

    def process_order_message(self, message: str | dict[str, Any]) -> dict[str, Any]:
        if isinstance(message, str):
            payload = json.loads(message)
        else:
            payload = message

        user_id = str(payload.get("user_id", ""))
        number_of_items = int(payload.get("number_of_items", 0))
        total_amount = float(payload.get("total_amount", 0.0))

        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO orders (user_id, number_of_items, total_amount) VALUES (?, ?, ?)",
                (user_id, number_of_items, total_amount),
            )
            order_id = cursor.lastrowid

        return {
            "id": order_id,
            "user_id": user_id,
            "number_of_items": number_of_items,
            "total_amount": total_amount,
        }

    def get_orders(self) -> list[dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders")
        return [dict(row) for row in cursor.fetchall()]
