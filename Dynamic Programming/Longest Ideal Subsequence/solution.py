class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0 for i in range(26)]
        for c in s:
            l = ord(c) - ord('a')
            dp[l] = max(dp[max(0, l - k):min(26, l + k + 1)]) + 1
        return max(dp)
