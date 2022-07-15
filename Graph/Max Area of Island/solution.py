class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        dirs = [(0,1), (1,0), (-1,0), (0, -1)]
        def dfs(r, c):
            result = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 0:
                    continue
                grid[nr][nc] = 0
                result += dfs(nr, nc)
            return result

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    result = max(result, dfs(i, j))
        return result
