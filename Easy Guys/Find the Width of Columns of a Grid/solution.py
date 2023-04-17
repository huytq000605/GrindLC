class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0 for _ in range(n)]
        for c in range(n):
            for r in range(m):
                l = len(str(grid[r][c]))
                result[c] = max(result[c], l)
        return result
