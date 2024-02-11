class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-math.inf for _ in range(m)] for _ in range(m)]
        dp[0][m-1] = grid[0][0] + grid[0][m-1]
        result = 0
        for r in range(1, n):
            next_dp = [[0 for _ in range(m)] for _ in range(m)]
            for c1 in range(m):
                for c2 in range(m):
                    mx = -math.inf
                    for dc1 in range(-1, 2):
                        for dc2 in range(-1, 2):
                            pc1, pc2 = c1 + dc1, c2 + dc2
                            if pc1 < 0 or pc1 >= m or pc2 < 0 or pc2 >= m:
                                continue
                            mx = max(mx, dp[pc1][pc2])
                    next_dp[c1][c2] = mx + grid[r][c1]
                    if c1 != c2: next_dp[c1][c2] += grid[r][c2]
                    result = max(result, next_dp[c1][c2])
            dp = next_dp
        return result
                    
