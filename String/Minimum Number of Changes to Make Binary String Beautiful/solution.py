class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                result += 1
        return result
