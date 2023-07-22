class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        ds = [(-2, 1), (-2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        @cache
        def dfs(r, c, k):
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0
            if k == 0:
                return 1
            result = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                result += 0.125 * dfs(nr, nc, k-1)
            return result
        return dfs(row, column, k)
