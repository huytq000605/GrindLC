class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(row, col):
            if row >= m-1:
                return 0
            result = math.inf
            for ncol in range(n):
                if row < m-1:
                    next_value = grid[row+1][ncol]
                else:
                    next_value = 0
                result = min(result, dfs(row + 1, ncol) + moveCost[grid[row][col]][ncol] + next_value)
            return result
        ans = math.inf
        for i in range(n):
            ans = min(ans, dfs(0, i) + grid[0][i])
        return ans