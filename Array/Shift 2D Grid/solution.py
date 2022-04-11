class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= (m*n)
        
        def get_idx(r, c):
            return r * n + c
        
        def get_row_col(idx):
            idx %= (m*n)
            return idx // n, idx % n
        
        result = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                idx = get_idx(i, j)
                nr, nc = get_row_col(idx + k)
                result[nr][nc] = grid[i][j]
        
        return result
