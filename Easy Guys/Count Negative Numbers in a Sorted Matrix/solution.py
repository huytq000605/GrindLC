class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c  = 0, n-1
        result = 0
        for r in range(m):
            while c >= 0 and grid[r][c] < 0:
                c -= 1
            result += n-c-1
        return result
