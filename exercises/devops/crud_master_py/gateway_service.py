import json
from queue import Queue
from typing import Any
from billing_service import BillingDB
from inventory_service import InventoryDB


class ApiGateway:
    def __init__(
        self, inventory_db: InventoryDB | None = None, billing_db: BillingDB | None = None
    ):
        self.inventory = inventory_db or InventoryDB()
        self.billing = billing_db or BillingDB()
        self.billing_queue: Queue[str] = Queue()

    def route_request(
        self, method: str, path: str, query: str | None = None, body: dict[str, Any] | None = None
    ) -> tuple[int, dict[str, Any] | list[Any] | str]:
        # Handle /api/movies
        if path == "/api/movies":
            if method == "GET":
                return 200, self.inventory.get_movies(title_query=query)
            elif method == "POST":
                if not body or "title" not in body or "description" not in body:
                    return 400, {"error": "Missing title or description"}
                movie = self.inventory.create_movie(body["title"], body["description"])
                return 201, movie
            elif method == "DELETE":
                count = self.inventory.delete_all_movies()
                return 200, {"deleted_count": count}

        # Handle /api/movies/:id
        elif path.startswith("/api/movies/"):
            try:
                movie_id = int(path.split("/")[-1])
            except ValueError:
                return 400, {"error": "Invalid movie id"}

            if method == "GET":
                movie = self.inventory.get_movie(movie_id)
                if not movie:
                    return 404, {"error": "Movie not found"}
                return 200, movie
            elif method == "PUT":
                title = body.get("title") if body else None
                desc = body.get("description") if body else None
                updated = self.inventory.update_movie(movie_id, title, desc)
                if not updated:
                    return 404, {"error": "Movie not found"}
                return 200, updated
            elif method == "DELETE":
                success = self.inventory.delete_movie(movie_id)
                if not success:
                    return 404, {"error": "Movie not found"}
                return 200, {"message": f"Movie {movie_id} deleted"}

        # Handle /api/billing
        elif path in ("/api/billing", "/api/billing/"):
            if method == "POST":
                if not body:
                    return 400, {"error": "Missing billing order body"}
                # Post to queue
                msg_str = json.dumps(body)
                self.billing_queue.put(msg_str)
                # Process message asynchronously or directly into billing DB
                self.billing.process_order_message(msg_str)
                return 200, {"message": "Message posted"}

        return 404, {"error": "Not found"}
