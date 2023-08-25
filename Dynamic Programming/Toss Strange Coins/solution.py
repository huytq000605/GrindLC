class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j] = percentage of having j heads when tossed i coins
        dp = [[0 for j in range(target + 1)] for i in range(n+1)]
        dp[0][0] = 1
        for i, p in enumerate(prob):
            for j in range(target + 1):
                if j > 0: dp[i+1][j] += dp[i][j-1] * p
                dp[i+1][j] += dp[i][j] * (1 - p)
        return dp[-1][target]
            
