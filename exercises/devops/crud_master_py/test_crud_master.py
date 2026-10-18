import unittest
from billing_service import BillingDB
from gateway_service import ApiGateway
from inventory_service import InventoryDB


class TestCrudMaster(unittest.TestCase):
    def setUp(self):
        self.gateway = ApiGateway()

    def test_inventory_crud_flow(self):
        # 1. Create movies
        code, m1 = self.gateway.route_request(
            "POST",
            "/api/movies",
            body={"title": "Inception", "description": "Mind-bending heist"},
        )
        self.assertEqual(code, 201)
        self.assertEqual(m1["title"], "Inception")

        code, m2 = self.gateway.route_request(
            "POST",
            "/api/movies",
            body={"title": "Interstellar", "description": "Space exploration"},
        )
        self.assertEqual(code, 201)

        # 2. Retrieve all movies
        code, movies = self.gateway.route_request("GET", "/api/movies")
        self.assertEqual(code, 200)
        self.assertEqual(len(movies), 2)

        # 3. Retrieve movies filtered by title
        code, filtered = self.gateway.route_request(
            "GET", "/api/movies", query="Inter"
        )
        self.assertEqual(code, 200)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["title"], "Interstellar")

        # 4. Get movie by id
        movie_id = m1["id"]
        code, single = self.gateway.route_request(
            "GET", f"/api/movies/{movie_id}"
        )
        self.assertEqual(code, 200)
        self.assertEqual(single["title"], "Inception")

        # 5. Update movie
        code, updated = self.gateway.route_request(
            "PUT",
            f"/api/movies/{movie_id}",
            body={"description": "Updated dream within a dream"},
        )
        self.assertEqual(code, 200)
        self.assertEqual(
            updated["description"], "Updated dream within a dream"
        )

        # 6. Delete movie by id
        code, del_res = self.gateway.route_request(
            "DELETE", f"/api/movies/{movie_id}"
        )
        self.assertEqual(code, 200)

        # 7. Delete all movies
        code, del_all = self.gateway.route_request("DELETE", "/api/movies")
        self.assertEqual(code, 200)
        code, empty_list = self.gateway.route_request("GET", "/api/movies")
        self.assertEqual(len(empty_list), 0)

    def test_billing_queue_flow(self):
        order_payload = {
            "user_id": "3",
            "number_of_items": "5",
            "total_amount": "180",
        }
        code, res = self.gateway.route_request(
            "POST", "/api/billing", body=order_payload
        )
        self.assertEqual(code, 200)
        self.assertEqual(res, {"message": "Message posted"})

        orders = self.gateway.billing.get_orders()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["user_id"], "3")
        self.assertEqual(orders[0]["number_of_items"], 5)
        self.assertEqual(orders[0]["total_amount"], 180.0)


if __name__ == "__main__":
    unittest.main()
