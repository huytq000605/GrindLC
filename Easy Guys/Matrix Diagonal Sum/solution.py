class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for r in range(n):
            result += mat[r][r]
            if n-1-r != r:
                result += mat[r][n-1-r]
        return result
