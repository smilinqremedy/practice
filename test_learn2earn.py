#!/usr/bin/env python3
"""
Unit Test Suite for Learn2Earn Equipment Lending System
=======================================================
Verifies all functional requirements, edge cases, state non-mutation,
and bonus JSON persistence.
"""

import os
import unittest
from app import (
    get_default_resources,
    get_default_fellows,
    find_resource_by_id,
    add_resource,
    borrow_resource,
    return_resource,
    search_resources_by_name,
    filter_resources_by_category,
    generate_reports,
    get_fellow_loan_quantity,
    save_to_json,
    load_from_json,
)


class TestLearn2EarnSystem(unittest.TestCase):

    def setUp(self):
        self.resources = get_default_resources()
        self.fellows = get_default_fellows()
        self.borrow_records = []

    # ---------------------------------------------------------
    # 1. Resource Inventory Tests (10 marks)
    # ---------------------------------------------------------
    def test_default_inventory_structure(self):
        self.assertEqual(len(self.resources), 3)
        for r in self.resources:
            self.assertIn("id", r)
            self.assertIn("name", r)
            self.category = r["category"]
            self.assertEqual(r["total"], r["available"])

    def test_add_resource_success(self):
        success = add_resource(self.resources, "R004", "Mouse", "Accessories", 10)
        self.assertTrue(success)
        added = find_resource_by_id(self.resources, "R004")
        self.assertIsNotNone(added)
        self.assertEqual(added["name"], "Mouse")
        self.assertEqual(added["total"], 10)
        self.assertEqual(added["available"], 10)

    def test_add_resource_reject_duplicate_id(self):
        count_before = len(self.resources)
        success = add_resource(self.resources, "R001", "Gaming Laptop", "Electronics", 5)
        self.assertFalse(success)
        self.assertEqual(len(self.resources), count_before)

    def test_add_resource_reject_invalid_inputs(self):
        # Non-positive total
        self.assertFalse(add_resource(self.resources, "R005", "Monitor", "Electronics", 0))
        self.assertFalse(add_resource(self.resources, "R005", "Monitor", "Electronics", -5))
        # Empty fields
        self.assertFalse(add_resource(self.resources, "", "Monitor", "Electronics", 5))
        self.assertFalse(add_resource(self.resources, "R005", "", "Electronics", 5))

    # ---------------------------------------------------------
    # 2. Borrowing Tests (15 marks)
    # ---------------------------------------------------------
    def test_borrow_resource_success(self):
        success = borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 2)
        self.assertTrue(success)
        laptop = find_resource_by_id(self.resources, "R001")
        self.assertEqual(laptop["available"], 8)
        self.assertEqual(len(self.borrow_records), 1)
        self.assertEqual(self.borrow_records[0]["quantity"], 2)

    def test_borrow_reject_unknown_fellow(self):
        stock_before = self.resources[0]["available"]
        success = borrow_resource(self.resources, self.fellows, self.borrow_records, "F999", "R001", 1)
        self.assertFalse(success)
        self.assertEqual(self.resources[0]["available"], stock_before)
        self.assertEqual(len(self.borrow_records), 0)

    def test_borrow_reject_unknown_resource(self):
        success = borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R999", 1)
        self.assertFalse(success)
        self.assertEqual(len(self.borrow_records), 0)

    def test_borrow_reject_non_positive_quantity(self):
        stock_before = self.resources[0]["available"]
        self.assertFalse(borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 0))
        self.assertFalse(borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", -2))
        self.assertEqual(self.resources[0]["available"], stock_before)

    def test_borrow_reject_insufficient_stock(self):
        headset = find_resource_by_id(self.resources, "R003")
        self.assertEqual(headset["available"], 3)
        success = borrow_resource(self.resources, self.fellows, self.borrow_records, "F003", "R003", 4)
        self.assertFalse(success)
        self.assertEqual(headset["available"], 3)
        self.assertEqual(len(self.borrow_records), 0)

    # ---------------------------------------------------------
    # 3. Return Tests (10 marks)
    # ---------------------------------------------------------
    def test_return_resource_success(self):
        # F001 borrows 2 laptops then returns 1
        borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 2)
        success = return_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 1)
        self.assertTrue(success)
        laptop = find_resource_by_id(self.resources, "R001")
        self.assertEqual(laptop["available"], 9)
        self.assertEqual(get_fellow_loan_quantity(self.borrow_records, "F001", "R001"), 1)

    def test_return_reject_more_than_borrowed(self):
        # F002 borrows 3 keyboards, attempts to return 4
        borrow_resource(self.resources, self.fellows, self.borrow_records, "F002", "R002", 3)
        keyboard = find_resource_by_id(self.resources, "R002")
        self.assertEqual(keyboard["available"], 2)

        success = return_resource(self.resources, self.fellows, self.borrow_records, "F002", "R002", 4)
        self.assertFalse(success)
        self.assertEqual(keyboard["available"], 2)  # Unchanged
        self.assertEqual(get_fellow_loan_quantity(self.borrow_records, "F002", "R002"), 3)

    def test_return_reject_zero_loan_balance(self):
        success = return_resource(self.resources, self.fellows, self.borrow_records, "F003", "R001", 1)
        self.assertFalse(success)

    # ---------------------------------------------------------
    # 4. Search and Filter Tests (10 marks)
    # ---------------------------------------------------------
    def test_search_by_name_case_insensitive(self):
        res1 = search_resources_by_name(self.resources, "LAPtop")
        self.assertEqual(len(res1), 1)
        self.assertEqual(res1[0]["name"], "Laptop")

        res2 = search_resources_by_name(self.resources, "board")
        self.assertEqual(len(res2), 1)
        self.assertEqual(res2[0]["name"], "Keyboard")

    def test_filter_by_category(self):
        accessories = filter_resources_by_category(self.resources, "Accessories")
        self.assertEqual(len(accessories), 2)
        names = [r["name"] for r in accessories]
        self.assertIn("Keyboard", names)
        self.assertIn("Headset", names)

    # ---------------------------------------------------------
    # 5. Reports Tests (15 marks)
    # ---------------------------------------------------------
    def test_reports_values_and_tie_handling(self):
        # Run standard demo steps
        borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 2)
        borrow_resource(self.resources, self.fellows, self.borrow_records, "F002", "R002", 3)
        return_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 1)

        rep = generate_reports(self.resources, self.borrow_records)
        self.assertEqual(rep["total_units"], 18)
        self.assertEqual(rep["available_units"], 14)
        self.assertEqual(rep["borrowed_units"], 4)
        self.assertEqual(len(rep["low_stock"]), 1)
        self.assertEqual(rep["low_stock"][0]["name"], "Keyboard")
        self.assertEqual(rep["low_stock"][0]["available"], 2)
        self.assertEqual(len(rep["most_borrowed_resources"]), 1)
        self.assertEqual(rep["most_borrowed_resources"][0]["name"], "Keyboard")
        self.assertEqual(rep["max_borrowed_units"], 3)

        # Test tie condition: F001 borrows 2 more laptops (total 3 laptops borrowed)
        borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 2)
        rep_tied = generate_reports(self.resources, self.borrow_records)
        self.assertEqual(len(rep_tied["most_borrowed_resources"]), 2)
        tied_names = [r["name"] for r in rep_tied["most_borrowed_resources"]]
        self.assertIn("Laptop", tied_names)
        self.assertIn("Keyboard", tied_names)

    # ---------------------------------------------------------
    # 6. JSON Persistence Bonus Tests
    # ---------------------------------------------------------
    def test_json_save_and_load(self):
        temp_file = "test_persistence.json"
        try:
            borrow_resource(self.resources, self.fellows, self.borrow_records, "F001", "R001", 2)
            saved = save_to_json(self.resources, self.fellows, self.borrow_records, temp_file)
            self.assertTrue(saved)
            self.assertTrue(os.path.exists(temp_file))

            loaded = load_from_json(temp_file)
            self.assertIsNotNone(loaded)
            loaded_res, loaded_fellows, loaded_records = loaded
            self.assertEqual(len(loaded_res), 3)
            laptop = find_resource_by_id(loaded_res, "R001")
            self.assertEqual(laptop["available"], 8)
            self.assertEqual(len(loaded_records), 1)
            self.assertEqual(loaded_records[0]["quantity"], 2)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()
