from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(row: int, col1: int, col2: int) -> int:
            if row >= len(grid) or col1 < 0 or col2 < 0 or col1 >= len(grid[0]) or col2 >= len(grid[0]):
                return 0
            if col1 == col2:
                thisRow = grid[row][col1]
            else:
                thisRow = grid[row][col1] + grid[row][col2]
                
            belowThisRow = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    belowThisRow = max(belowThisRow, dfs(row + 1, col1 + i, col2 + j))
            
            return thisRow + belowThisRow
        return dfs(0, 0, len(grid[0]) -1)