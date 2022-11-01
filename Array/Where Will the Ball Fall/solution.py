class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # cols[i] = which column the ball[i] is at
        cols = [i for i in range(n)]
        for r in range(m):
            for c in range(n):
                if cols[c] == -1:
                    continue
                nc = cols[c] + grid[r][cols[c]]
                if nc < 0 or nc >= n or grid[r][nc] + grid[r][cols[c]] == 0:
                    cols[c] = -1
                else:
                    cols[c] = nc
        return cols
