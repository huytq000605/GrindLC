class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        MOD = 10**9 + 7
        dp[0] = 1
        result = 0
        for i in range(high+1):
            if i - zero >= 0:
                dp[i] += dp[i-zero]
            if i - one >= 0:
                dp[i] += dp[i-one]
            dp[i] %= MOD
            if low <= i <= high:
                result += dp[i]
                result %= MOD
        return result
