class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for r in range(m):
            for c in range(n):
                if grid[r][c]: 
                    rows[r] += 1
                    cols[c] += 1
        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (rows[r] > 1 or cols[c] > 1):
                    result += 1
        return result
