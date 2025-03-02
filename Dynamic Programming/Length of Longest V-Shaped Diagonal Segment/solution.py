class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [(1,1), (1, -1), (-1, -1), (-1,1), ]
        result = 0
        
        @cache
        def dfs(r, c, v, d, turned):
            result = 0
            dr, dc = ds[d]
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == v:
                result = max(result, 1 + dfs(nr, nc, 2-v, d, turned))
            if not turned:
                nd = (d+1+4)%4
                dr, dc = ds[nd]
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == v:
                    result = max(result, 1 + dfs(nr, nc, 2-v, nd, True))
            return result
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    for d in range(len(ds)):
                        result = max(result, 1 + dfs(r, c, 2, d, False))
        return result
       
