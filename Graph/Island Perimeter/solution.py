class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]: continue
                result += 4
                for dr, dc in ds:
                    ar, ac = r + dr, c + dc
                    if ar < 0 or ar >= m or ac < 0 or ac >= n: continue
                    result -= grid[ar][ac]
        return result
