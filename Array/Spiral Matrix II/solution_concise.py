class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            result[i][j] = k + 1
            ni, nj = i + di, j + dj
            if result[ni % n][nj % n]:
                di, dj = dj, -di
                ni, nj = i + di, j + dj
            i, j = ni, nj
        return result