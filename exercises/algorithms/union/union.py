def union(s1: str, s2: str) -> str:
    """Returns unique characters from s1 followed by s2 in order of appearance."""
    seen = set()
    res = []
    for ch in s1 + s2:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    return "".join(res)
