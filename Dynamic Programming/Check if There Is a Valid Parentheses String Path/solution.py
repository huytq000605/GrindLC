class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        dirs = [(0,1), (1,0)]
        m, n = len(grid), len(grid[0])
        
        @cache
        def dfs(i, j, stack):
            if grid[i][j] == ")":
                if stack == 0:
                    return False
                stack -= 1
            else:
                stack += 1
            
            if i == m - 1 and j == n-1:
                if stack == 0:
                    return True
                else:
                    return False
            
            for d in dirs:
                nr, nc = i + d[0], j + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if dfs(nr, nc, stack):
                    return True
            return False
        
        return dfs(0, 0, 0)