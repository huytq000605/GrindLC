class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [(0,1), (1,0), (-1, 0), (0,-1)]
        MOD = 10**9 + 7
        @cache
        def dfs(r, c, moves):
            if moves > maxMove:
                return 0
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            result = 0
            for dr, dc in dirs:
                result += dfs(r + dr, c + dc, moves + 1)
            return result % MOD
        return dfs(startRow, startColumn, 0)
