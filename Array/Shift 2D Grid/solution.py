class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m*n
        if not k: return grid
        result = [[grid[(i*n+j-k)//n][(i*n+j-k)%n] for j in range(n)] for i in range(m)]
        return result
        
