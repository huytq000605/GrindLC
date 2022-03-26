class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_right_array = min(arrLen, steps)
        dp = [[0 for j in range(steps + 1)] for i in range(max_right_array)]
        
        dp[0][0] = 1
        for step in range(1, steps + 1):
            for i in range(max_right_array):
                if i > 0:
                    dp[i][step] += dp[i-1][step - 1]
                dp[i][step] += dp[i][step - 1]
                if i < max_right_array - 1:
                    dp[i][step] += dp[i+1][step - 1]
                dp[i][step] %= (10**9 + 7)
        return dp[0][steps]