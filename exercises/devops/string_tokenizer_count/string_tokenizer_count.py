import re
from collections import Counter


def tokenizer_counter(string: str) -> dict[str, int]:
    """Tokenizes string, counts word frequencies, and returns dictionary sorted alphabetically."""
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", string)
    words = cleaned.lower().split()
    counts = Counter(words)
    return dict(sorted(counts.items(), key=lambda item: item[0]))


if __name__ == "__main__":
    string = "This is a test sentence, with various words and 123 numbers!"
    print(tokenizer_counter(string))
