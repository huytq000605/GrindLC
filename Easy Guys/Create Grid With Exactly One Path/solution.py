class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]
        c = 0
        for r in range(m):
            grid[r][c] = '.'
            if c + 1 < n:
                grid[r][c+1] = '.'
                c += 1
        while c < n:
            grid[m-1][c] = '.'
            c += 1
        return ["".join(r) for r in grid]
