class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def prefix_grid(v):
            prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
            for r in range(m):
                for c in range(n):
                    prefix[r+1][c+1] = prefix[r][c+1] + prefix[r+1][c] - prefix[r][c] + (grid[r][c] == v)
            return prefix
        
        xs = prefix_grid("X")
        ys = prefix_grid("Y")
        result = 0
        for r in range(m):
            for c in range(n):
                if xs[r+1][c+1] and xs[r+1][c+1] == ys[r+1][c+1]:
                    result += 1
        return result
                
                
                
                
