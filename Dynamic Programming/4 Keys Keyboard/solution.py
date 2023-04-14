class Solution:
    def maxA(self, n: int) -> int:
        if n < 7: return n
        dp = [0 for _ in range(n+1)]
        for i in range(1, 6+1):
            dp[i] = i
        for i in range(7, n+1):
            # takes 2 moves to select and copy
            dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4)
        return dp[-1]
            
