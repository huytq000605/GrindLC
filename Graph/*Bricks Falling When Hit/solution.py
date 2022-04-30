class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])
        result = [0 for i in range(len(hits))]
        
        for r, c in hits:
            grid[r][c] -= 1
            
        def dfs(r, c):
            grid[r][c] = 2
            result = 1
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != 1:
                    continue
                result += dfs(nr, nc)
            return result
        
        def is_stable(r, c):
            if r == 0:
                return True
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2:
                    return True
            return False
        
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
                
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            grid[r][c] += 1
            if grid[r][c] == 1 and is_stable(r, c):
                result[i] = dfs(r, c) - 1
        return result