class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = (1 << (n-1)) * m
        for c in range(1, n):
            ones = 0
            for r in range(m):
                ones += grid[r][c] == grid[r][0]
            result += (1 << (n-1-c)) * max(ones, m - ones)
        return result
