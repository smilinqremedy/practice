# 01-Edu Python Curriculum Solutions & Algorithms

This directory contains clean, dependency-free Python solutions and test suites for the 01-Edu curriculum challenges and foundational algorithmic problems.

---

## 🗂 Structure

```
exercises/
├── run_all_tests.py                 # Unified test discovery and runner
├── devops/                          # 01-Edu DevOps Python Track
│   ├── hello_python/                # Hello Python (hello_python.py)
│   ├── numerical_operations/        # Arithmetic operations (numerical_operations.py)
│   ├── numerical_operations_the_return/ # Division, modulo, zero handling
│   ├── concat_string/               # String concatenation with delimiter
│   ├── string_processing/           # Tokenization and normalization
│   ├── string_tokenizer_count/      # Word frequency counter (sorted)
│   ├── flex_function/               # Positional, keyword, default parameters
│   ├── clean_the_list/              # List cleaning, capitalization, numbering
│   ├── candidates_checker/          # Age eligibility validation CLI
│   ├── merge_two/                   # Interactive dictionary merger to JSON
│   ├── shopping/                    # List management (remember the apple)
│   ├── object_to_json/              # User class and JSON serialization
│   ├── read_file/                   # JSON recipe loader
│   ├── write_file/                  # Formatted date to-do list writer
│   ├── credentials_searches/        # Deep JSON credential scanner
│   ├── custom_calendar/             # Day index <-> weekday converter
│   ├── punishment/                  # Repetitive sentence generator
│   ├── skip_secrets/                # Line filtering and stream processing
│   ├── backup_manager/              # Scheduled archive manager and daemon
│   └── crud_master_py/              # Microservices architecture (Gateway, Inventory, Billing)
└── algorithms/                      # Core 01-Edu Algorithmic Challenges
    ├── algorithms.py                # Implementations of core piscine problems
    └── test_algorithms.py           # Comprehensive unit tests
```

---

## 🚀 Running the Tests

To run the entire test suite across all 21 modules (57+ unit tests):

```bash
python3 exercises/run_all_tests.py
```

To run tests for a specific module:

```bash
# DevOps exercise example
python3 exercises/devops/hello_python/test_hello_python.py

# Algorithmic challenges
python3 exercises/algorithms/test_algorithms.py
```

---

## 📋 Solved Modules Summary

### 1. DevOps Python Modules
| Module | Main Function / Script | Description |
|---|---|---|
| `hello_python` | `say_hello_python()` | Returns standard greeting string. |
| `numerical_operations` | `add`, `subtract`, `multiply`, `power`, `square_root` | Fundamental arithmetic functions. |
| `numerical_operations_the_return` | `modulo`, `divide`, `integer_division` | Division and modulo with zero-division safety. |
| `concat_string` | `concat(s1, s2)` | Merges two strings with comma separation. |
| `string_processing` | `tokenize(sentence)` | Removes punctuation, lowercases, and splits words. |
| `string_tokenizer_count` | `tokenizer_counter(text)` | Produces sorted dictionary of word counts. |
| `flex_function` | `create_person(...)` | Demonstrates positional-only, keyword, and defaults. |
| `clean_the_list` | `clean_list(items)` | Normalizes list, formats indexed strings, ensures item presence. |
| `candidates_checker` | `candidates_checker.py` | Command-line tool evaluating candidate eligibility by age. |
| `merge_two` | `merge_two(dict)` | Interactive dictionary merger serialized as JSON. |
| `shopping` | `remember_the_apple(items)` | Idempotent list updates. |
| `object_to_json` | `create_new_user`, `user_to_json` | OOP instantiation and dynamic attribute serialization. |
| `read_file` | `get_recipes(path)` | Robust JSON file deserialization. |
| `write_file` | `to_do(tasks)` | Formats dates and tasks into structured output text file. |
| `credentials_searches` | `credentials_search()` | Recursively traverses JSON structures to extract secret keys. |
| `custom_calendar` | `day_from_number`, `day_to_number` | Bi-directional day/number mappings. |
| `punishment` | `do_punishment(...)` | Multi-line text generator using string multiplication. |
| `skip_secrets` | `skip_secrets.py` | CLI filter removing specified patterns from input files. |
| `backup_manager` | `backup_manager.py`, `backup_service.py` | Full background backup service and scheduler with audit logs. |
| `crud_master_py` | `ApiGateway`, `InventoryDB`, `BillingDB` | Microservices REST API & message queue architecture. |

### 2. Core Algorithmic Challenges (`exercises/algorithms/`)
- `is_positive` & `abs_val`: Absolute value calculation without built-ins.
- `fibonacci`: Recursive Fibonacci number calculator.
- `is_prime` & `find_next_prime`: Fast primality testing and next-prime finder.
- `integer_sqrt`: Exact integer square root.
- `alphamirror`: Opposite alphabet cipher preserving case.
- `rot13`: Standard ROT13 Caesar cipher.
- `first_word` & `last_word`: Whitespace-delimited word extraction.
- `reverse_string`: String reversal.
- `wdmatch`: Subsequence existence in target text.
- `inter` & `union`: Ordered set operations on strings.
- `binary_addition`: Arbitrary-precision binary addition.
- `collatz_conjecture`: Collatz $3n + 1$ step counter.
