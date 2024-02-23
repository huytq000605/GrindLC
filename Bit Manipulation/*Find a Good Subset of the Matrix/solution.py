class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # because n <= 5 so that means at x column, there is maximum 2 of 1s
        # considering a subset S, len(S) > 2
        # that means if we take only 2 rows from this subset, it still works
        # another case we should consider is a row have all 0s.
        for r in range(m):
            num = 0
            for c in range(n):
                if grid[r][c]: num |= 1 << c
            if num == 0:
                return [r]
            grid[r] = num

        for r1 in range(m):
            for r2 in range(r1+1, m):
                if grid[r1] & grid[r2] == 0:
                    return [r1, r2]
        return []
