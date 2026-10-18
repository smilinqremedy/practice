import re


def tokenize(sentence: str) -> list[str]:
    """Tokenizes a sentence: removes punctuation/special characters, lowercases, and splits words."""
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", sentence)
    return cleaned.lower().split()


if __name__ == "__main__":
    my_sentence = "It's not possible, you can't ask for a raise"
    print(tokenize(my_sentence))
