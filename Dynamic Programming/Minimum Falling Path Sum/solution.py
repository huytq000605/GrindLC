class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [matrix[0][c] for c in range(n)]
        for r in range(1, m):
            ndp = [math.inf for _ in range(n)]
            for c in range(n):
                for dc in range(max(0,c-1), min(n, c+2)):
                    ndp[c] = min(ndp[c], dp[dc] + matrix[r][c])
            dp = ndp
        return min(dp)
