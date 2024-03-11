class Solution:
    def customSortString(self, order: str, s: str) -> str:
        keys = {c:i for i, c in enumerate(order)}
        return "".join(sorted(s, key = lambda e: keys.get(e, 0)))
