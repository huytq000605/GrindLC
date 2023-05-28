class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # dp[i][j] longest path to cell (i, j) 
        d = [[0 for j in range(n)] for i in range(m)]
        # dr[r] = current longest path to row r 
        dr = [0 for _ in range(m)]
        # dr[c] = current longest path to col c
        dc = [0 for _ in range(n)]
        values = defaultdict(list)
        for r in range(m):
            for c in range(n):
                values[mat[r][c]].append((r, c))
        for k in sorted(values.keys()):
            for r, c in values[k]:
                d[r][c] = max(dr[r], dc[c]) + 1
            for r, c in values[k]:
                dr[r] = max(dr[r], d[r][c])
                dc[c] = max(dc[c], d[r][c])
        return max(max(dr), max(dc))
