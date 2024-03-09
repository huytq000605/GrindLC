class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for r in range(m):
            for c in range(n):
                if r: grid[r][c] += grid[r-1][c]
                if c: grid[r][c] += grid[r][c-1]
                if r and c: grid[r][c] -= grid[r-1][c-1]
                if grid[r][c] <= k:
                    result += 1
        return result
