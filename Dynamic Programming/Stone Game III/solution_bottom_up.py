class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        n = len(piles)
        dp = [-math.inf for _ in range(n+1)]
        dp[-1] = 0
        for i in reversed(range(n)):
            s = 0
            for j in range(i, min(n, i + 3)):
                s += piles[j]
                dp[i] = max(dp[i], s - dp[j+1])
        if dp[0] > 0: return "Alice"
        elif dp[0] < 0: return "Bob"
        return "Tie"
