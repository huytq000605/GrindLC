class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_col = [[0 for j in range(m)] for i in range(n)]
        for col in range(n):
            for row in range(m):
                if row > 0:
                    prefix_col[col][row] = prefix_col[col][row-1]
                prefix_col[col][row] += matrix[row][col]

        result = 0
        for row_start in range(m):
            for row_end in range(row_start, m):
                seen = defaultdict(int)
                seen[0] = 1
                cur = 0
                for col in range(n):
                    if row_start > 0:
                        cur += prefix_col[col][row_end] - prefix_col[col][row_start- 1]
                    else:
                        cur += prefix_col[col][row_end]
                    if cur - target in seen:
                        result += seen[cur-target]
                    seen[cur] += 1

        return result
