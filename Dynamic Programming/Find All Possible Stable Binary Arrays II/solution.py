class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # From Top Down solution
        # dp[z][o][0] = dp[z][o-t][1] for t in [1, limit]
        # dp[z][o][1] = dp[z-t][o][0] for t in [1, limit]
        #             = dp[z-1][o][0] + dp[z-2][o][0] + ... + dp[z-limit][o][0]
        # => dp[z+1][o][1] = dp[z][o][0] + dp[z][o][1] - dp[z-limit][o][0]
        # generalize =>
        # dp[z][o][1] = dp[z-1][o][0] + dp[z-1][o][1] - dp[z-1-limit][o][0]
        # dp[z][o][0] = dp[z][o-1][1] + dp[z][o-1][0] - dp[z][o-1-limit][1]
        dp = [[[0 for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        for t in range(1, min(zero, limit) + 1):
            dp[t][0][1] = 1
        for t in range(1, min(one, limit) + 1):
            dp[0][t][0] = 1
        for z in range(1, zero + 1):
            for o in range(1, one + 1):
                dp[z][o][0] = dp[z][o-1][1] + dp[z][o-1][0]
                if o-1-limit >= 0: dp[z][o][0] -= dp[z][o-1-limit][1]
                dp[z][o][0] %= MOD

                dp[z][o][1] = dp[z-1][o][0] + dp[z-1][o][1]
                if z-1-limit >= 0: dp[z][o][1] -= dp[z-1-limit][o][0]
                dp[z][o][1] %= MOD
        return sum(dp[zero][one]) % MOD
