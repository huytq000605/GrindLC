class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        seen = set()
        m = len(grid)
        n = len(grid[0])
        
        def getId(row, col):
            return row * n + col
        
        start = (0,0)
        end = (0,0)
        obstacles = 0
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i ,j)
                elif grid[i][j] == 2:
                    end = (i ,j)
                elif grid[i][j] == -1:
                    obstacles += 1
        seen.add(getId(start[0], start[1]))
        
        def dfs(r, c):
            nonlocal result
            if (r, c) == end:
                if len(seen) + obstacles == m * n:
                    result += 1
                return
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == -1 or getId(nr, nc) in seen:
                    continue
                seen.add(getId(nr, nc))
                dfs(nr, nc)
                seen.remove(getId(nr, nc))
                
        dfs(start[0], start[1])
        
        return result