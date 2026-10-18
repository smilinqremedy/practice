def inter(s1: str, s2: str) -> str:
    """Returns characters present in both s1 and s2 without duplicates, preserving s1 order."""
    s2_set = set(s2)
    seen = set()
    res = []
    for ch in s1:
        if ch in s2_set and ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)
