def wdmatch(s1: str, s2: str) -> str:
    """Returns s1 if all characters of s1 appear in s2 in sequential order, else ''."""
    it = iter(s2)
    return s1 if all(ch in it for ch in s1) else ""
