class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        max_columns = [-1 for _ in range(n)]
        for c in range(n):
            for r in range(m):
                max_columns[c] = max(max_columns[c], matrix[r][c])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == -1:
                    matrix[r][c] = max_columns[c]
        return matrix
