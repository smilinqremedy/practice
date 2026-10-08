#!/usr/bin/env python3
"""
Learn2Earn Equipment Lending System
====================================
A command-line program that manages equipment inventory, handles borrowing
and returns for fellows, searches inventory, generates reports, and supports
JSON persistence.
"""

import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple


def get_default_resources() -> List[Dict[str, Any]]:
    """Return initial resource inventory."""
    return [
        {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
        {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
        {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
    ]


def get_default_fellows() -> Dict[str, str]:
    """Return initial fellows registry."""
    return {"F001": "Ada", "F002": "John", "F003": "Grace"}


def find_resource_by_id(resources: List[Dict[str, Any]], resource_id: str) -> Optional[Dict[str, Any]]:
    """
    Search for a resource by its unique identifier (case-insensitive).
    Returns the resource dictionary if found, or None if not found.
    """
    clean_id = resource_id.strip().upper()
    for resource in resources:
        if resource["id"].upper() == clean_id:
            return resource
    return None


def add_resource(
    resources: List[Dict[str, Any]],
    resource_id: str,
    name: str,
    category: str,
    total: int
) -> bool:
    """
    Add a new resource to inventory.
    Rejects duplicate IDs, non-positive integer totals, or empty fields.
    Initializes available units equal to total units.
    """
    clean_id = resource_id.strip().upper()
    clean_name = name.strip()
    clean_category = category.strip()

    if not clean_id or not clean_name or not clean_category:
        print("Error: Resource ID, name, and category cannot be empty.")
        return False

    if not isinstance(total, int) or total <= 0:
        print(f"Error: Total units must be a positive integer (> 0). Provided: {total}")
        return False

    if find_resource_by_id(resources, clean_id) is not None:
        print(f"Error: Resource with ID '{clean_id}' already exists. Duplicate IDs are rejected.")
        return False

    new_resource = {
        "id": clean_id,
        "name": clean_name,
        "category": clean_category,
        "total": total,
        "available": total
    }
    resources.append(new_resource)
    print(f"Success: Added '{clean_name}' (ID: {clean_id}) in '{clean_category}' with {total} units.")
    return True


def list_resources(resources: List[Dict[str, Any]]) -> None:
    """Display all resources in inventory with formatted columns."""
    if not resources:
        print("Inventory is currently empty.")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<8} | {'Name':<15} | {'Category':<15} | {'Total':<6} | {'Available':<9} | {'Borrowed':<8}")
    print("-" * 65)
    for res in resources:
        borrowed = res["total"] - res["available"]
        print(f"{res['id']:<8} | {res['name']:<15} | {res['category']:<15} | {res['total']:<6} | {res['available']:<9} | {borrowed:<8}")
    print("=" * 65)


def get_fellow_loan_quantity(borrow_records: List[Dict[str, Any]], fellow_id: str, resource_id: str) -> int:
    """Calculate the total units of a resource currently on loan to a specific fellow."""
    f_id = fellow_id.strip().upper()
    r_id = resource_id.strip().upper()
    return sum(
        rec["quantity"]
        for rec in borrow_records
        if rec["fellow_id"].upper() == f_id and rec["resource_id"].upper() == r_id
    )


def borrow_resource(
    resources: List[Dict[str, Any]],
    fellows: Dict[str, str],
    borrow_records: List[Dict[str, Any]],
    fellow_id: str,
    resource_id: str,
    quantity: int
) -> bool:
    """
    Issue equipment units to a fellow.
    Validations:
      - Fellow ID must exist.
      - Resource ID must exist.
      - Quantity must be a positive integer.
      - Quantity must not exceed available stock.
    On success: decrements resource available stock and logs the borrowing record.
    On failure: state remains unmutated.
    """
    clean_fellow_id = fellow_id.strip().upper()
    clean_resource_id = resource_id.strip().upper()

    # Validate fellow
    if clean_fellow_id not in fellows:
        print(f"Error: Fellow ID '{clean_fellow_id}' is not registered.")
        return False

    # Validate resource
    resource = find_resource_by_id(resources, clean_resource_id)
    if resource is None:
        print(f"Error: Resource ID '{clean_resource_id}' does not exist.")
        return False

    # Validate quantity
    if not isinstance(quantity, int) or quantity <= 0:
        print(f"Error: Borrow quantity must be a positive integer (> 0). Provided: {quantity}")
        return False

    # Validate stock availability
    if quantity > resource["available"]:
        print(
            f"Error: Insufficient stock. Fellow '{fellows[clean_fellow_id]}' requested {quantity} "
            f"units of '{resource['name']}', but only {resource['available']} unit(s) are available."
        )
        return False

    # Perform mutation only after all checks pass
    resource["available"] -= quantity

    # Log in borrow_records (update existing active loan or append new)
    for record in borrow_records:
        if record["fellow_id"].upper() == clean_fellow_id and record["resource_id"].upper() == resource["id"].upper():
            record["quantity"] += quantity
            break
    else:
        borrow_records.append({
            "fellow_id": clean_fellow_id,
            "resource_id": resource["id"],
            "quantity": quantity
        })

    print(
        f"Success: {fellows[clean_fellow_id]} ({clean_fellow_id}) borrowed {quantity} unit(s) of "
        f"{resource['name']} ({resource['id']}). Available units remaining: {resource['available']}."
    )
    return True


def return_resource(
    resources: List[Dict[str, Any]],
    fellows: Dict[str, str],
    borrow_records: List[Dict[str, Any]],
    fellow_id: str,
    resource_id: str,
    quantity: int
) -> bool:
    """
    Accept returns of borrowed equipment.
    Validations:
      - Fellow ID must exist.
      - Resource ID must exist.
      - Quantity must be a positive integer.
      - Quantity must not exceed the units the fellow currently has on loan for this item.
    On success: updates borrowing records and increments available inventory stock.
    On failure: state remains unmutated.
    """
    clean_fellow_id = fellow_id.strip().upper()
    clean_resource_id = resource_id.strip().upper()

    # Validate fellow
    if clean_fellow_id not in fellows:
        print(f"Error: Fellow ID '{clean_fellow_id}' is not registered.")
        return False

    # Validate resource
    resource = find_resource_by_id(resources, clean_resource_id)
    if resource is None:
        print(f"Error: Resource ID '{clean_resource_id}' does not exist.")
        return False

    # Validate quantity
    if not isinstance(quantity, int) or quantity <= 0:
        print(f"Error: Return quantity must be a positive integer (> 0). Provided: {quantity}")
        return False

    # Check active loan balance
    current_loan = get_fellow_loan_quantity(borrow_records, clean_fellow_id, resource["id"])
    if current_loan == 0:
        print(
            f"Error: Fellow '{fellows[clean_fellow_id]}' ({clean_fellow_id}) does not currently "
            f"have any units of '{resource['name']}' on loan."
        )
        return False

    if quantity > current_loan:
        print(
            f"Error: Return rejected. Fellow '{fellows[clean_fellow_id]}' tried to return {quantity} "
            f"unit(s) of '{resource['name']}', but currently only has {current_loan} on loan."
        )
        return False

    # Deduct from borrow records
    remaining_to_deduct = quantity
    for record in list(borrow_records):
        if record["fellow_id"].upper() == clean_fellow_id and record["resource_id"].upper() == resource["id"].upper():
            if record["quantity"] <= remaining_to_deduct:
                remaining_to_deduct -= record["quantity"]
                borrow_records.remove(record)
            else:
                record["quantity"] -= remaining_to_deduct
                remaining_to_deduct = 0
            if remaining_to_deduct == 0:
                break

    # Restore inventory stock
    resource["available"] += quantity

    print(
        f"Success: {fellows[clean_fellow_id]} ({clean_fellow_id}) returned {quantity} unit(s) of "
        f"{resource['name']} ({resource['id']}). Available units now: {resource['available']}."
    )
    return True


def search_resources_by_name(resources: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Case-insensitive search for resources by name (substring match).
    """
    clean_query = query.strip().lower()
    if not clean_query:
        return []
    return [r for r in resources if clean_query in r["name"].lower()]


def filter_resources_by_category(resources: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
    """
    Filter resources by category (case-insensitive exact match).
    """
    clean_cat = category.strip().lower()
    if not clean_cat:
        return []
    return [r for r in resources if clean_cat == r["category"].lower()]


def generate_reports(
    resources: List[Dict[str, Any]],
    borrow_records: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Generate inventory and borrowing reports:
      - Overall total units across all resources
      - Overall available units
      - Overall units currently borrowed
      - Resources with fewer than 3 available units (low stock)
      - Resource(s) with most units currently borrowed (identifies all tied leaders)
    """
    total_units = sum(r["total"] for r in resources)
    available_units = sum(r["available"] for r in resources)
    borrowed_units = total_units - available_units

    low_stock = [r for r in resources if r["available"] < 3]

    # Calculate borrowed units per resource
    resource_borrowed = {
        r["id"]: (r["total"] - r["available"])
        for r in resources
    }

    max_borrowed = max(resource_borrowed.values()) if resource_borrowed else 0

    if max_borrowed > 0:
        most_borrowed = [
            r for r in resources
            if (r["total"] - r["available"]) == max_borrowed
        ]
    else:
        most_borrowed = []

    print("\n" + "=" * 50)
    print("           LEARN2EARN INVENTORY REPORT")
    print("=" * 50)
    print(f"Overall Total Units   : {total_units}")
    print(f"Overall Available     : {available_units}")
    print(f"Units Currently Loaned: {borrowed_units}")
    print("-" * 50)

    print("Low Stock Resources (< 3 available):")
    if low_stock:
        for r in low_stock:
            print(f"  • {r['name']} ({r['id']}): {r['available']} available (Total: {r['total']})")
    else:
        print("  • None")

    print("-" * 50)
    print("Resource(s) with Most Units Currently Borrowed:")
    if most_borrowed:
        leaders_str = ", ".join(f"{r['name']} ({max_borrowed})" for r in most_borrowed)
        print(f"  • {leaders_str}")
    else:
        print("  • No units currently on loan")
    print("=" * 50 + "\n")

    return {
        "total_units": total_units,
        "available_units": available_units,
        "borrowed_units": borrowed_units,
        "low_stock": low_stock,
        "max_borrowed_units": max_borrowed,
        "most_borrowed_resources": most_borrowed
    }


def save_to_json(
    resources: List[Dict[str, Any]],
    fellows: Dict[str, str],
    borrow_records: List[Dict[str, Any]],
    filename: str = "learn2earn_data.json"
) -> bool:
    """
    Persist inventory, fellows registry, and loan records to a JSON file.
    (Bonus Feature)
    """
    data = {
        "resources": resources,
        "fellows": fellows,
        "borrow_records": borrow_records
    }
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Success: Data persisted to '{filename}'.")
        return True
    except IOError as e:
        print(f"Error: Unable to save data to '{filename}': {e}")
        return False


def load_from_json(
    filename: str = "learn2earn_data.json"
) -> Optional[Tuple[List[Dict[str, Any]], Dict[str, str], List[Dict[str, Any]]]]:
    """
    Reload inventory, fellows registry, and loan records from a JSON file.
    (Bonus Feature)
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        resources = data.get("resources", [])
        fellows = data.get("fellows", {})
        borrow_records = data.get("borrow_records", [])
        print(f"Success: Data reloaded from '{filename}'.")
        return resources, fellows, borrow_records
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error: Failed to load JSON from '{filename}': {e}")
        return None


def run_demonstration() -> None:
    """
    Execute the required 7-step demonstration sequence plus an additional invalid-input test.
    """
    print("\n" + "#" * 60)
    print("   LEARN2EARN REQUIRED DEMONSTRATION SEQUENCE")
    print("#" * 60)

    # Fresh starting data
    resources = get_default_resources()
    fellows = get_default_fellows()
    borrow_records: List[Dict[str, Any]] = []

    print("\nInitial Inventory:")
    list_resources(resources)

    # Step 1
    print("\n>>> STEP 1: F001 borrows 2 laptops")
    borrow_resource(resources, fellows, borrow_records, "F001", "R001", 2)
    laptop = find_resource_by_id(resources, "R001")
    print(f"Verification: Available laptop units = {laptop['available']}")

    # Step 2
    print("\n>>> STEP 2: F002 borrows 3 keyboards")
    borrow_resource(resources, fellows, borrow_records, "F002", "R002", 3)
    keyboard = find_resource_by_id(resources, "R002")
    print(f"Verification: Available keyboard units = {keyboard['available']}")

    # Step 3
    print("\n>>> STEP 3: F001 returns 1 laptop")
    return_resource(resources, fellows, borrow_records, "F001", "R001", 1)
    laptop = find_resource_by_id(resources, "R001")
    print(f"Verification: Available laptop units = {laptop['available']}")

    # Step 4
    print("\n>>> STEP 4: F003 requests 4 headsets (Available: 3)")
    headset = find_resource_by_id(resources, "R003")
    stock_before = headset["available"]
    borrow_resource(resources, fellows, borrow_records, "F003", "R003", 4)
    print(f"Verification: Headset stock before = {stock_before}, stock after = {headset['available']} (Unchanged)")

    # Step 5
    print("\n>>> STEP 5: F002 tries to return 4 keyboards (Borrowed: 3)")
    stock_before = keyboard["available"]
    return_resource(resources, fellows, borrow_records, "F002", "R002", 4)
    print(f"Verification: Keyboard stock before = {stock_before}, stock after = {keyboard['available']} (Unchanged)")

    # Step 6
    print("\n>>> STEP 6: Search for 'LAPtop' (case-insensitive)")
    results = search_resources_by_name(resources, "LAPtop")
    print(f"Search results for 'LAPtop' ({len(results)} found):")
    for r in results:
        print(f"  • Found: {r['name']} (ID: {r['id']}, Category: {r['category']}, Available: {r['available']}/{r['total']})")

    # Step 7
    print("\n>>> STEP 7: Generate Report")
    generate_reports(resources, borrow_records)

    # Additional Invalid-Input Test
    print("\n>>> ADDITIONAL INVALID-INPUT TEST: Fellow F999 (non-existent) tries to borrow 1 laptop")
    borrow_resource(resources, fellows, borrow_records, "F999", "R001", 1)

    print("\n>>> ADDITIONAL INVALID-INPUT TEST: F001 enters negative borrow quantity (-2)")
    borrow_resource(resources, fellows, borrow_records, "F001", "R001", -2)

    print("\n" + "#" * 60)
    print("   DEMONSTRATION COMPLETE")
    print("#" * 60 + "\n")


def display_menu() -> None:
    """Print the interactive main menu."""
    print("\n" + "=" * 40)
    print("   Learn2Earn Equipment Lending System")
    print("=" * 40)
    print("1. View Resource Inventory")
    print("2. Add New Resource")
    print("3. Borrow Resource")
    print("4. Return Resource")
    print("5. Search Resources by Name")
    print("6. Filter Resources by Category")
    print("7. Generate Inventory Reports")
    print("8. Save Data to JSON (Bonus)")
    print("9. Load Data from JSON (Bonus)")
    print("10. Run Required Demonstration")
    print("0. Exit")
    print("=" * 40)


def prompt_positive_int(prompt_text: str) -> Optional[int]:
    """Helper to safely prompt and parse a positive integer."""
    raw = input(prompt_text).strip()
    try:
        val = int(raw)
        if val <= 0:
            print("Error: Input must be a positive integer greater than zero.")
            return None
        return val
    except ValueError:
        print(f"Error: '{raw}' is not a valid integer.")
        return None


def main() -> None:
    """Main application loop with interactive menu."""
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demonstration()
        return

    resources = get_default_resources()
    fellows = get_default_fellows()
    borrow_records: List[Dict[str, Any]] = []

    print("\nWelcome to Learn2Earn Equipment Lending System!")

    while True:
        display_menu()
        choice = input("Enter choice (0-10): ").strip()

        if choice == "1":
            list_resources(resources)

        elif choice == "2":
            print("\n--- Add New Resource ---")
            r_id = input("Enter Resource ID (e.g. R004): ").strip()
            name = input("Enter Resource Name (e.g. Mouse): ").strip()
            category = input("Enter Category (e.g. Accessories): ").strip()
            total = prompt_positive_int("Enter Total Units: ")
            if total is not None:
                add_resource(resources, r_id, name, category, total)

        elif choice == "3":
            print("\n--- Borrow Resource ---")
            f_id = input("Enter Fellow ID (e.g. F001): ").strip()
            r_id = input("Enter Resource ID (e.g. R001): ").strip()
            qty = prompt_positive_int("Enter Quantity to Borrow: ")
            if qty is not None:
                borrow_resource(resources, fellows, borrow_records, f_id, r_id, qty)

        elif choice == "4":
            print("\n--- Return Resource ---")
            f_id = input("Enter Fellow ID (e.g. F001): ").strip()
            r_id = input("Enter Resource ID (e.g. R001): ").strip()
            qty = prompt_positive_int("Enter Quantity to Return: ")
            if qty is not None:
                return_resource(resources, fellows, borrow_records, f_id, r_id, qty)

        elif choice == "5":
            print("\n--- Search Resources by Name ---")
            query = input("Enter name search term: ").strip()
            results = search_resources_by_name(resources, query)
            if results:
                print(f"\nFound {len(results)} matching resource(s):")
                list_resources(results)
            else:
                print(f"No resources matched '{query}'.")

        elif choice == "6":
            print("\n--- Filter by Category ---")
            cat = input("Enter category name: ").strip()
            results = filter_resources_by_category(resources, cat)
            if results:
                print(f"\nFound {len(results)} resource(s) in category '{cat}':")
                list_resources(results)
            else:
                print(f"No resources found in category '{cat}'.")

        elif choice == "7":
            generate_reports(resources, borrow_records)

        elif choice == "8":
            filename = input("Enter JSON file path [default: learn2earn_data.json]: ").strip()
            if not filename:
                filename = "learn2earn_data.json"
            save_to_json(resources, fellows, borrow_records, filename)

        elif choice == "9":
            filename = input("Enter JSON file path [default: learn2earn_data.json]: ").strip()
            if not filename:
                filename = "learn2earn_data.json"
            loaded = load_from_json(filename)
            if loaded is not None:
                resources, fellows, borrow_records = loaded

        elif choice == "10":
            run_demonstration()

        elif choice == "0":
            print("\nThank you for using Learn2Earn. Goodbye!\n")
            break

        else:
            print("Invalid selection. Please choose an option from 0 to 10.")


if __name__ == "__main__":
    main()
