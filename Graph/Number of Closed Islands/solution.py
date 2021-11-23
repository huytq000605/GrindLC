class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        seen = [[False for j in range(n)] for i in range(m)]
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def dfs(row, col):
            seen[row][col] = True
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]
                if nrow < 0 or nrow >= m or ncol < 0 or ncol >= n or seen[nrow][ncol] == True or grid[nrow][ncol] == 1:
                    continue
                dfs(nrow, ncol)
            
        for row in range(m):
            for col in [0, n-1]:
                if grid[row][col] == 0:
                    dfs(row, col)
        
        for col in range(n):
            for row in [0, m-1]:
                if grid[row][col] == 0:
                    dfs(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not seen[i][j]:
                    result += 1
                    dfs(i, j)
        return result