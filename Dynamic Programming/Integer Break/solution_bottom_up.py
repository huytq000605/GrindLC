class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)]
        dp[0] = 1
        for i in range(2, n):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        result = 0
        for i in range(1, n):
            result = max(result, dp[i] * dp[n - i])
        return result