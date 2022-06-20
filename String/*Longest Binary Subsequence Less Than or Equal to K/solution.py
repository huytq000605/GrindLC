class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        cost = 1
        result = 0
        for i in range(n-1, -1, -1):
            if s[i] == "0" or cost <= k:
                k -= cost * int(s[i])
                result += 1
            if cost <= k:
                cost *= 2
        return result