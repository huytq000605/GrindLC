class Solution:
    def minimumTime(self, s: str) -> int:
        left = 0
        n = len(s)
        result = n
        for i, c in enumerate(s):
            if c == "1":
                left = min(i + 1, left + 2)
            result = min(result, left + n - 1 - i)
        return result