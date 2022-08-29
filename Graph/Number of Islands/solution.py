class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            grid[r][c] = "0"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == "0":
                    continue
                dfs(nr, nc)

        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1
        return result
