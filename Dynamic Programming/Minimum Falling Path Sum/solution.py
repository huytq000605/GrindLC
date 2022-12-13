class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(r, c):
            if r + 1 == m:
                return 0
            result = math.inf
            for nc in range(c-1, c+2):
                if nc < 0 or nc >= n:
                    continue
                result = min(result, dfs(r + 1, nc) + matrix[r+1][nc])
            return result
        return min([dfs(0, i) + matrix[0][i] for i in range(n)])
