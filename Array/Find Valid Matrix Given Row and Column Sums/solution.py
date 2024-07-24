class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        result = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                result[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= result[r][c]
                colSum[c] -= result[r][c]
        return result
