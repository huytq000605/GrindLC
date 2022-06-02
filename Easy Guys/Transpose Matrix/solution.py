class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[matrix[j][i] for j in range(m)] for i in range(n)]
        return result