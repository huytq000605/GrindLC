class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ds = [(0,1), (1,0), (0, -1), (-1, 0)]
        MOD = 10**9 + 7
        result = 0
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            result = 1
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if grid[nr][nc] <= grid[r][c]:
                    continue
                result += dfs(nr, nc)
            return result
        for r in range(m):
            for c in range(n):
                result = (result + dfs(r, c)) % MOD
        return result
