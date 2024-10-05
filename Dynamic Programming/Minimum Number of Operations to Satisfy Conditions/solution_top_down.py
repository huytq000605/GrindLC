class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(c, prev):
            if c >= n: return 0
            counter = Counter([grid[r][c] for r in range(m)])
            result = math.inf
            for v in range(10):
                if v == prev: continue
                result = min(result, m - counter[v] + dfs(c+1, v))
            return result
        return dfs(0, -1)
