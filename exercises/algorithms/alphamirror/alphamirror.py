def alphamirror(s: str) -> str:
    """Replaces each alphabetical character with the opposite letter preserving case."""
    result = []
    for ch in s:
        if "a" <= ch <= "z":
            result.append(chr(ord("z") - (ord(ch) - ord("a"))))
        elif "A" <= ch <= "Z":
            result.append(chr(ord("Z") - (ord(ch) - ord("A"))))
        else:
            result.append(ch)
    return "".join(result)
