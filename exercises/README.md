# 01-Edu Python Curriculum Solutions & Algorithms

This directory contains dependency-free Python solutions and test suites for the 01-Edu curriculum challenges and foundational algorithmic problems. **Every problem resides in its own isolated folder with dedicated implementation and unit tests.**

---

## 🗂 Project Layout

```
exercises/
├── run_all_tests.py                         # Unified test discovery and runner
├── README.md                                # Catalog & execution documentation
├── devops/                                  # 20 01-Edu Python DevOps Modules
│   ├── hello_python/                        # say_hello_python()
│   ├── numerical_operations/                # add, subtract, multiply, power, square_root
│   ├── numerical_operations_the_return/     # modulo, divide, integer_division (zero-safe)
│   ├── concat_string/                       # concat()
│   ├── string_processing/                   # tokenize()
│   ├── string_tokenizer_count/              # tokenizer_counter()
│   ├── flex_function/                       # create_person()
│   ├── clean_the_list/                      # clean_list()
│   ├── candidates_checker/                  # candidates_checker.py
│   ├── merge_two/                           # merge_two()
│   ├── shopping/                            # remember_the_apple()
│   ├── object_to_json/                      # User, create_new_user(), user_to_json()
│   ├── read_file/                           # get_recipes()
│   ├── write_file/                          # to_do()
│   ├── credentials_searches/                # credentials_search()
│   ├── custom_calendar/                     # day_from_number(), day_to_number()
│   ├── punishment/                          # do_punishment()
│   ├── skip_secrets/                        # skip_secrets.py
│   ├── backup_manager/                      # backup_manager.py & backup_service.py
│   └── crud_master_py/                      # ApiGateway, InventoryDB, BillingDB
└── algorithms/                              # 20 Foundational Algorithmic Challenges
    ├── abs/                                 # is_positive, abs_val
    ├── alphamirror/                         # alphamirror
    ├── binary_addition/                     # binary_addition
    ├── collatz_conjecture/                 # collatz_conjecture
    ├── doop/                                # safe 64-bit CLI calculator
    ├── eightqueens/                         # recursive 8-queens backtracking solver
    ├── fibonacci/                           # recursive fibonacci
    ├── find_next_prime/                     # find_next_prime
    ├── first_word/                          # first_word
    ├── inter/                               # ordered set intersection
    ├── is_prime/                            # primality test
    ├── last_word/                           # last_word
    ├── printcomb/                           # unique combinations of 3 digits
    ├── printcomb2/                          # combinations of two 2-digit numbers
    ├── reverse_string/                      # reverse_string
    ├── rot13/                               # Caesar cipher ROT13
    ├── splitwhitespaces/                    # whitespace token splitter
    ├── sqrt/                                # exact integer square root
    ├── union/                               # ordered set union
    └── wdmatch/                             # ordered subsequence verification
```

---

## 🚀 Running the Tests

To run the complete test suite across all 40 independent modules (70 unit tests):

```bash
python3 exercises/run_all_tests.py
```

To run tests for any individual module:

```bash
# Example 1: DevOps module
python3 exercises/devops/hello_python/test_hello_python.py

# Example 2: 8-Queens solver
python3 exercises/algorithms/eightqueens/test_eightqueens.py

# Example 3: Doop calculator
python3 exercises/algorithms/doop/test_doop.py
```

---

## 📋 Catalog Summary

### 1. DevOps Modules (`exercises/devops/`)
| Module Folder | Main Function / Script | Description |
|---|---|---|
| [`hello_python/`](devops/hello_python/) | `say_hello_python()` | Returns standard greeting string. |
| [`numerical_operations/`](devops/numerical_operations/) | `add`, `subtract`, `multiply`, `power`, `square_root` | Fundamental arithmetic functions. |
| [`numerical_operations_the_return/`](devops/numerical_operations_the_return/) | `modulo`, `divide`, `integer_division` | Arithmetic with zero-division safety. |
| [`concat_string/`](devops/concat_string/) | `concat(s1, s2)` | String joining with comma and space. |
| [`string_processing/`](devops/string_processing/) | `tokenize(sentence)` | Sentence punctuation removal and word splitting. |
| [`string_tokenizer_count/`](devops/string_tokenizer_count/) | `tokenizer_counter(text)` | Alphabetically sorted word frequency map. |
| [`flex_function/`](devops/flex_function/) | `create_person(...)` | Positional-only, keyword, and default parameters. |
| [`clean_the_list/`](devops/clean_the_list/) | `clean_list(items)` | List cleaning, item capitalization, numbering, milk check. |
| [`candidates_checker/`](devops/candidates_checker/) | `candidates_checker.py` | CLI tool validating candidate eligibility by age. |
| [`merge_two/`](devops/merge_two/) | `merge_two(dict)` | Interactive dictionary merger serialized as JSON. |
| [`shopping/`](devops/shopping/) | `remember_the_apple(items)` | Idempotent list updates. |
| [`object_to_json/`](devops/object_to_json/) | `create_new_user`, `user_to_json` | OOP class instantiation and dynamic JSON conversion. |
| [`read_file/`](devops/read_file/) | `get_recipes(path)` | Robust JSON file deserialization. |
| [`write_file/`](devops/write_file/) | `to_do(tasks)` | Formatted date and task file generator. |
| [`credentials_searches/`](devops/credentials_searches/) | `credentials_search()` | Deep traversal extracting secret keys from JSON. |
| [`custom_calendar/`](devops/custom_calendar/) | `day_from_number`, `day_to_number` | Bi-directional day/number mappings. |
| [`punishment/`](devops/punishment/) | `do_punishment(...)` | Multi-line text generator using string multiplication. |
| [`skip_secrets/`](devops/skip_secrets/) | `skip_secrets.py` | CLI filter removing specified patterns from input files. |
| [`backup_manager/`](devops/backup_manager/) | `backup_manager.py`, `backup_service.py` | Scheduled archive manager and daemon with audit logs. |
| [`crud_master_py/`](devops/crud_master_py/) | `ApiGateway`, `InventoryDB`, `BillingDB` | Microservices REST API & message queue architecture. |

### 2. Algorithmic Modules (`exercises/algorithms/`)
| Module Folder | Main Function | Description |
|---|---|---|
| [`abs/`](algorithms/abs/) | `abs_val`, `is_positive` | Absolute value without built-ins. |
| [`alphamirror/`](algorithms/alphamirror/) | `alphamirror(s)` | Opposite letter mapping preserving case. |
| [`binary_addition/`](algorithms/binary_addition/) | `binary_addition(a, b)` | Arbitrary-precision binary addition. |
| [`collatz_conjecture/`](algorithms/collatz_conjecture/) | `collatz_conjecture(n)` | Collatz $3n + 1$ step counter. |
| [`doop/`](algorithms/doop/) | `doop(v1, op, v2)` | Safe 64-bit calculator with error handling. |
| [`eightqueens/`](algorithms/eightqueens/) | `solve_eight_queens()` | Backtracking puzzle solver returning all 92 solutions. |
| [`fibonacci/`](algorithms/fibonacci/) | `fibonacci(n)` | Pure recursive Fibonacci calculator. |
| [`find_next_prime/`](algorithms/find_next_prime/) | `find_next_prime(n)` | Prime finder returning smallest prime $\ge n$. |
| [`first_word/`](algorithms/first_word/) | `first_word(s)` | First word extraction. |
| [`inter/`](algorithms/inter/) | `inter(s1, s2)` | Ordered character intersection without duplicates. |
| [`is_prime/`](algorithms/is_prime/) | `is_prime(n)` | Primality test function. |
| [`last_word/`](algorithms/last_word/) | `last_word(s)` | Last word extraction. |
| [`printcomb/`](algorithms/printcomb/) | `print_comb()` | 3-digit unique ascending combinations (120 items). |
| [`printcomb2/`](algorithms/printcomb2/) | `print_comb2()` | Combinations of two 2-digit numbers (4,950 items). |
| [`reverse_string/`](algorithms/reverse_string/) | `reverse_string(s)` | String reversal. |
| [`rot13/`](algorithms/rot13/) | `rot13(s)` | ROT13 Caesar cipher. |
| [`splitwhitespaces/`](algorithms/splitwhitespaces/) | `split_white_spaces(s)` | Tokenizer splitting on spaces, tabs, and newlines. |
| [`sqrt/`](algorithms/sqrt/) | `integer_sqrt(n)` | Exact integer square root. |
| [`union/`](algorithms/union/) | `union(s1, s2)` | Ordered unique character union. |
| [`wdmatch/`](algorithms/wdmatch/) | `wdmatch(s1, s2)` | Subsequence verification. |
