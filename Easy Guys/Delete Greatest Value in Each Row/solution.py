class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        rows = [sorted(grid[i], reverse = True) for i in range(m)]
        result = 0
        for col in range(n):
            result += max([rows[i][col] for i in range(m)])
        return result
