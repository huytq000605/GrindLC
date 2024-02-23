class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0, *cuts, n]
        m = len(cuts)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        
        for d in range(2, m):
            for i in range(m - d):
                j = i + d
                # Recognize through equation: dp[i][i + d] = cuts[i+d] - cuts[j] + dp[i][k] + dp[k][j] with k in [i+1, i+d)
                # Need the loop for i and d

                dp[i][j] = min([cuts[j] - cuts[i] + dp[i][k] + dp[k][j] for k in range(i+1, j)])
        return dp[0][-1]
