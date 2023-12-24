class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        w = 0
        expected = 0
        for i in range(n):
            c = int(s[i])
            w += c == expected
            expected = 1 - expected
        return min(w, n - w)
