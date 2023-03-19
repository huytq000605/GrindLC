class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        steps = [None for _ in range(n * n)]
        for r in range(n):
            for c in range(n):
                steps[grid[r][c]] = (r, c)
        if steps[0] != (0, 0): return False
        for i in range(n*n-1):
            r, c = steps[i]
            nr, nc = steps[i+1]
            if abs(r - nr) == 2 and abs(c - nc) == 1:
                continue
            if abs(r - nr) == 1 and abs(c - nc) == 2:
                continue
            return False
        return True
