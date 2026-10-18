import json
import sqlite3
from typing import Any


class InventoryDB:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL
                )
            """
            )

    def get_movies(self, title_query: str | None = None) -> list[dict[str, Any]]:
        cursor = self.conn.cursor()
        if title_query:
            cursor.execute(
                "SELECT * FROM movies WHERE title LIKE ?",
                (f"%{title_query}%",),
            )
        else:
            cursor.execute("SELECT * FROM movies")
        return [dict(row) for row in cursor.fetchall()]

    def get_movie(self, movie_id: int) -> dict[str, Any] | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def create_movie(self, title: str, description: str) -> dict[str, Any]:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO movies (title, description) VALUES (?, ?)",
                (title, description),
            )
            movie_id = cursor.lastrowid
        return {"id": movie_id, "title": title, "description": description}

    def update_movie(
        self,
        movie_id: int,
        title: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any] | None:
        current = self.get_movie(movie_id)
        if not current:
            return None
        new_title = title if title is not None else current["title"]
        new_desc = (
            description if description is not None else current["description"]
        )
        with self.conn:
            self.conn.execute(
                "UPDATE movies SET title = ?, description = ? WHERE id = ?",
                (new_title, new_desc, movie_id),
            )
        return {"id": movie_id, "title": new_title, "description": new_desc}

    def delete_movie(self, movie_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM movies WHERE id = ?", (movie_id,)
            )
            return cursor.rowcount > 0

    def delete_all_movies(self) -> int:
        with self.conn:
            cursor = self.conn.execute("DELETE FROM movies")
            return cursor.rowcount
