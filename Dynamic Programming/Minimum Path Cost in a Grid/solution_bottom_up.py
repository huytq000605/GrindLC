class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = grid[0]
        for i in range(1, m):
            cur = [math.inf for i in range(n)]
            for col in range(n):
                for ncol in range(n):
                    cur[ncol] = min(cur[ncol], prev[col] + grid[i][ncol] + moveCost[grid[i-1][col]][ncol])
            prev = cur
        return min(prev)