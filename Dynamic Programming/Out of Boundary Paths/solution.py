class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        @cache
        def dfs(r, c, s):
            if s > maxMove: return 0
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            return sum(dfs(r + dr, c + dc, s + 1) for dr, dc in ds) % MOD
        return dfs(startRow, startColumn, 0)

