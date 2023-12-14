class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = [0 for i in range(m)]
        onesCol = [0 for i in range(n)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    onesRow[r] += 1
                    onesCol[c] += 1
        result = [[onesRow[r] + onesCol[c] - (n - onesRow[r]) - (m - onesCol[c]) for c in range(n)] for r in range(m)]
        return result

