class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        n = len(piles)
        dp = [-math.inf for _ in range(n)]
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(i, min(i+3, n)):
                s += piles[j]
                dp[i] = max(dp[i], s - (dp[j+1] if j+1 < n else 0))
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
