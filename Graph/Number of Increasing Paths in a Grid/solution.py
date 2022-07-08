class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @cache
        def count(r, c):
            result = 1
            for i, j in dirs:
                nr, nc = r + i, c + j
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] <= grid[r][c]:
                    continue
                result += count(nr, nc)
            return result % MOD

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += count(i, j)
        return ans % MOD
