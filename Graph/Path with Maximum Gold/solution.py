class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        s = set()
        def dfs(r, c):     
            nonlocal s
            s.add((r, c))
            mx = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if grid[nr][nc] == 0 or (nr, nc) in s: continue
                mx = max(mx, dfs(nr, nc))
            s.remove((r, c))
            return grid[r][c] + mx
        
        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    result = max(result, dfs(r, c))
        return result
            
