class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        arrLen = min(steps, arrLen)
        dp = [0 for _ in range(arrLen)]
        dp[0] = 1
        while steps:
            next_dp = dp[:]
            for i in range(arrLen):
                if i > 0:
                    next_dp[i] += dp[i-1]
                if i < arrLen-1:
                    next_dp[i] += dp[i+1]
                next_dp[i] %= MOD
            dp = next_dp
            steps -= 1
        return dp[0]
