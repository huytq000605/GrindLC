class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ds = [(0,1), (1,0), (-1,0), (0, -1)]
        m, n = len(grid), len(grid[0])
        result = 0
        def dfs(r, c):
            grid[r][c] = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if grid[nr][nc] == 0: continue
                dfs(nr, nc)
        
        for r in range(m):
            for c in [0, n-1]:
                if grid[r][c]: dfs(r, c)
        
        for r in [0, m-1]:
            for c in range(n):
                if grid[r][c]: dfs(r, c)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    result += 1
        return result
