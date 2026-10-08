#!/usr/bin/env python3
"""
Learn2Earn Required Demonstration Runner
========================================
Executes the exact 7-step demonstration required by the assignment specification,
in order, plus an additional invalid-input test.
"""

from app import (
    get_default_resources,
    get_default_fellows,
    list_resources,
    borrow_resource,
    return_resource,
    search_resources_by_name,
    generate_reports,
    find_resource_by_id,
)

def main():
    print("=" * 70)
    print("LEARN2EARN: REQUIRED DEMONSTRATION & TEST EVIDENCE")
    print("=" * 70)

    # Initial state
    resources = get_default_resources()
    fellows = get_default_fellows()
    borrow_records = []

    print("\n[INITIAL STATE]")
    print(f"Fellows registered: {fellows}")
    list_resources(resources)

    # 1. F001 borrows 2 laptops — available laptop units = 8.
    print("\n----------------------------------------------------------------------")
    print("STEP 1: F001 borrows 2 laptops — available laptop units = 8.")
    print("----------------------------------------------------------------------")
    borrow_resource(resources, fellows, borrow_records, "F001", "R001", 2)
    laptop = find_resource_by_id(resources, "R001")
    print(f"Status Check: Laptop available = {laptop['available']} (Total: {laptop['total']})")
    print(f"Active Borrow Records: {borrow_records}")

    # 2. F002 borrows 3 keyboards — available keyboard units = 2.
    print("\n----------------------------------------------------------------------")
    print("STEP 2: F002 borrows 3 keyboards — available keyboard units = 2.")
    print("----------------------------------------------------------------------")
    borrow_resource(resources, fellows, borrow_records, "F002", "R002", 3)
    keyboard = find_resource_by_id(resources, "R002")
    print(f"Status Check: Keyboard available = {keyboard['available']} (Total: {keyboard['total']})")
    print(f"Active Borrow Records: {borrow_records}")

    # 3. F001 returns 1 laptop — available laptop units = 9.
    print("\n----------------------------------------------------------------------")
    print("STEP 3: F001 returns 1 laptop — available laptop units = 9.")
    print("----------------------------------------------------------------------")
    return_resource(resources, fellows, borrow_records, "F001", "R001", 1)
    laptop = find_resource_by_id(resources, "R001")
    print(f"Status Check: Laptop available = {laptop['available']} (Total: {laptop['total']})")
    print(f"Active Borrow Records: {borrow_records}")

    # 4. F003 requests 4 headsets — rejected without changing stock.
    print("\n----------------------------------------------------------------------")
    print("STEP 4: F003 requests 4 headsets — rejected without changing stock.")
    print("----------------------------------------------------------------------")
    headset = find_resource_by_id(resources, "R003")
    print(f"Before Attempt: Headset available = {headset['available']}")
    borrow_resource(resources, fellows, borrow_records, "F003", "R003", 4)
    print(f"After Attempt:  Headset available = {headset['available']} (State Unchanged)")

    # 5. F002 tries to return 4 keyboards — rejected without changing stock.
    print("\n----------------------------------------------------------------------")
    print("STEP 5: F002 tries to return 4 keyboards — rejected without changing stock.")
    print("----------------------------------------------------------------------")
    keyboard = find_resource_by_id(resources, "R002")
    print(f"Before Attempt: Keyboard available = {keyboard['available']}")
    return_resource(resources, fellows, borrow_records, "F002", "R002", 4)
    print(f"After Attempt:  Keyboard available = {keyboard['available']} (State Unchanged)")

    # 6. Search for LAPtop — find Laptop, ignoring case.
    print("\n----------------------------------------------------------------------")
    print("STEP 6: Search for LAPtop — find Laptop, ignoring case.")
    print("----------------------------------------------------------------------")
    results = search_resources_by_name(resources, "LAPtop")
    print(f"Search query: 'LAPtop'")
    print(f"Matches found: {len(results)}")
    for item in results:
        print(f"  • Matched: ID={item['id']}, Name={item['name']}, Category={item['category']}, Available={item['available']}/{item['total']}")

    # 7. Generate the report — overall units 18, available 14, borrowed 4, Keyboard low stock (2); Keyboard is most borrowed (3).
    print("\n----------------------------------------------------------------------")
    print("STEP 7: Generate the report — overall units 18, available 14, borrowed 4,")
    print("        Keyboard low stock (2); Keyboard is most borrowed (3).")
    print("----------------------------------------------------------------------")
    generate_reports(resources, borrow_records)

    # ADDITIONAL INVALID-INPUT TESTS
    print("----------------------------------------------------------------------")
    print("ADDITIONAL INVALID-INPUT TEST 1: Borrow with unregistered Fellow ID 'F999'")
    print("----------------------------------------------------------------------")
    borrow_resource(resources, fellows, borrow_records, "F999", "R001", 1)

    print("\n----------------------------------------------------------------------")
    print("ADDITIONAL INVALID-INPUT TEST 2: Borrow with non-positive quantity (-3)")
    print("----------------------------------------------------------------------")
    borrow_resource(resources, fellows, borrow_records, "F001", "R001", -3)

    print("\n----------------------------------------------------------------------")
    print("ADDITIONAL INVALID-INPUT TEST 3: Return item with 0 active loan balance")
    print("----------------------------------------------------------------------")
    return_resource(resources, fellows, borrow_records, "F003", "R001", 1)

    print("\n" + "=" * 70)
    print("END OF DEMONSTRATION")
    print("=" * 70)

if __name__ == "__main__":
    main()
