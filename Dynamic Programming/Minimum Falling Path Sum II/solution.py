class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = []
        dp = grid[0]
        for c in range(n):
            heappush(pq, (-grid[0][c], c))
            if len(pq) > 2: heappop(pq)
        for r in range(1, m):
            mn2 = heappop(pq)
            mn = heappop(pq)
            for c in range(n):
                if mn[1] == c:
                    dp[c] = -mn2[0] + grid[r][c]
                else:
                    dp[c] = -mn[0] + grid[r][c]
                heappush(pq, (-dp[c], c))
                if len(pq) > 2: heappop(pq)
        return min(dp)
                
