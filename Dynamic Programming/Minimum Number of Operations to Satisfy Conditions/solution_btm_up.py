class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [(0, 0), (0, 1)]
        for c in range(n):
            counter = [0 for _ in range(10)]
            for r in range(m):
                counter[grid[r][c]] += 1
            pq = []
            for next_col, count in enumerate(counter):
                for ops, col in dp[::-1]:
                    ops = -ops
                    if col == next_col: continue
                    heappush(pq, (-(ops + m - count), next_col))
                    if len(pq) > 2:
                        heappop(pq)
                    break
            dp = pq
        return min(-dp[0][0], -dp[1][0])
