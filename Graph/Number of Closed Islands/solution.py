class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        seen = [[0 for j in range(n)] for i in range(m)]
        def dfs(r, c):
            seen[r][c] = 1
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                if grid[nr][nc] or seen[nr][nc]: continue
                dfs(nr, nc)
        
        for r in [0, m-1]:
            for c in range(n):
                if grid[r][c] == 0: dfs(r, c)
        for r in range(m):
            for c in [0, n-1]:
                if grid[r][c] == 0: dfs(r, c)
        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and seen[r][c] == 0:
                    dfs(r, c)
                    result += 1
        return result
        
