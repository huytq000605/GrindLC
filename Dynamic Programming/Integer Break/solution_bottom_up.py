class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] = maximum of product if use i as the break one
        dp = [i for i in range(n + 1)]
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        result = 0
        for i in range(1, n):
            result = max(result, dp[i] * dp[n-i])
        return result
