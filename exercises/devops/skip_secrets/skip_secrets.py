import os
import sys


def filter_secrets() -> None:
    if len(sys.argv) != 2:
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as fin:
            lines = fin.readlines()

        with open("out.txt", "w", encoding="utf-8") as fout:
            for line in lines:
                if "pineapple" not in line:
                    fout.write(line)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    filter_secrets()
