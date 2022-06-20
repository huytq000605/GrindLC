class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [math.inf for i in range(n + 1)]
        dp[0] = 0
        result = 0
        for i in range(n):
            for j in range(i+1, 0, -1):
                value = dp[j-1] * 2 + int(s[i])
                if value <= k:
                    dp[j] = min(dp[j], value)
                    if dp[j] <= k:
                        result = max(result, j)
        return result