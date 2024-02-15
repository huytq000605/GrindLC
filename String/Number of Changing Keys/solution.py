class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        cur = s[0]
        result = 0
        for c in s:
            if c != cur:
                result += 1
                cur = c
        return result
