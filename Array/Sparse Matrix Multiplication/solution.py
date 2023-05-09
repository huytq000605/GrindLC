class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mA, nA, nB = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0 for j in range(nB)] for i in range(mA)]
        for r in range(mA):
            for c in range(nA):
                if mat1[r][c]:
                    for k in range(nB):
                        result[r][k] += mat1[r][c] * mat2[c][k]
        return result
