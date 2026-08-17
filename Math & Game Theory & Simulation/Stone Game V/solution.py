class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            s = stones[i]
            for j in range(i+1, n):
                s += stones[j]
                pref = 0
                for k in range(i, j):
                    pref += stones[k]
                    suff = s - pref
                    if pref < suff:
                        dp[i][j] = max(dp[i][j], pref + dp[i][k])
                    elif pref > suff:
                        dp[i][j] = max(dp[i][j], suff + dp[k+1][j])
                        # pruning logic: if pref > suff, move k further only increase pref
                        # max point is suff*2
                        if suff * 2 < dp[i][j]: break 
                    else:
                        dp[i][j] = max(dp[i][j], pref + dp[i][k], pref + dp[k+1][j])
        return dp[0][n-1]
