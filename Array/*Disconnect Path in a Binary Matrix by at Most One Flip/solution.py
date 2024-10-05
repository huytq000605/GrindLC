class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        # Since we only move right or down, we mark 0 at every cell we cannot pass through
        # Each time we move, we will move to another diagonal, so just check if any diagonal have <= 1 cell.
        # If we flip that cell, it would be disconnected
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 or (r,c) == (0,0): continue
                if (r == 0 or grid[r-1][c] == 0) and (c == 0 or grid[r][c-1] == 0):
                    grid[r][c] = 0
        
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if grid[r][c] == 0 or (r, c) == (m-1,n-1): continue
                if (r == m-1 or grid[r+1][c] == 0) and (c == n-1 or grid[r][c+1] == 0):
                    grid[r][c] = 0
        
        diagonals = [0 for _ in range(m+n-1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: diagonals[r+c] += 1
        for d in range(1, m+n-2):
            if diagonals[d] <= 1: return True
        return False
