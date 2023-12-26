class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        MOD = 10**9 + 7
        for _ in range(n):
            for v in range(target, -1, -1):
                dp[v] = 0
                for prev in range(max(0,v-k), v):
                    dp[v] += dp[prev]
                    dp[v] %= MOD
        return dp[-1]
