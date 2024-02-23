class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dirs = [(0,1), (1,0)]
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [[[0 for l in range(k)] for j in range(n+1)] for i in range(m+1)]
        dp[0][1][0] = 1
        for r in range(m):
            for c in range(n):
                for l in range(k):
                    dp[r+1][c+1][(l + grid[r][c]) % k] = (dp[r][c+1][l] + dp[r+1][c][l]) % MOD
                    
        return dp[-1][-1][0]
