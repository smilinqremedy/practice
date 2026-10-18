def rot13(s: str) -> str:
    """Rotates letters by 13 positions preserving case."""
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            result.append(chr(ord("a") + (ord(ch) - ord("a") + 13) % 26))
        elif "A" <= ch <= "Z":
            result.append(chr(ord("A") + (ord(ch) - ord("A") + 13) % 26))
        else:
            result.append(ch)
    return "".join(result)
