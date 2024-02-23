class Solution:
    def new21Game(self, n: int, k: int, w: int) -> float:
        if k == 0 or k + w < n:
            return 1 
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        # dp[i] = dp[i-1] * 1/n + dp[i-2] * 1/n + ... + dp[i-w] * 1/n
        # => dp[i] = 1/n * sum(dp[i] for i in range(1, w+1))
        s = 1
        for i in range(1, n+1):
            dp[i] = s * 1/w
            if i < k:
                s += dp[i]
            if i >= w:
                s -= dp[i-w]
        return sum(dp[i] for i in range(k, n+1))
