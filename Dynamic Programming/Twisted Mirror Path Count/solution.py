class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        @cache
        def dfs(r, c, d):
            if r >= m or c >= n: return 0
            if r == m-1 and c == n-1:
                return 1
            if not grid[r][c]:
                return (dfs(r+1, c, 0) + dfs(r, c+1, 1)) % MOD
            else:
                if d:
                    return dfs(r+1, c, 0) % MOD
                else:
                    return dfs(r, c+1, 1) % MOD
        return dfs(0, 0, 0) % MOD
