class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_col = [[0 for _ in range(m+1)] for _ in range(n)]
        for col in range(n):
            for row in range(m):
                prefix_col[col][row+1] = prefix_col[col][row] + matrix[row][col]

        result = 0
        for row_start in range(m):
            for row_end in range(row_start, m):
                counter = defaultdict(int)
                counter[0] = 1
                submatrix = 0
                for c in range(n):
                    submatrix += prefix_col[c][row_end+1] - prefix_col[c][row_start]
                    result += counter[submatrix - target]
                    counter[submatrix] += 1
        return result
