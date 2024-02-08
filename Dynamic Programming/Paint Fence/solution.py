class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0 for _ in range(2)]
        dp[1] = k
        for i in range(1, n):
            next_dp = [0 for _ in range(2)]
            # Choose different number than before
            next_dp[1] = (dp[0] + dp[1]) * (k-1)
            # Choose the same number from before
            next_dp[0] = dp[1]
            dp = next_dp
        return sum(dp)
                
