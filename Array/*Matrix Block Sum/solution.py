class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0 for j in range(n)] for i in range(m)]
        prefix = [[0 for j in range(n+1)] for i in range(m + 1)]
        for i in range(0, m):
            for j in range(0, n):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + mat[i][j]
        
        
        for i in range(m):
            startRow = max(0, i - k)
            endRow = min(m - 1, i + k)
            for j in range(n):
                startCol = max(0, j - k)
                endCol = min(n - 1, j + k)
                result[i][j] = prefix[endRow + 1][endCol + 1] + prefix[startRow][startCol] - prefix[startRow][endCol + 1] - prefix[endRow + 1][startCol]
            
            
        return result
                