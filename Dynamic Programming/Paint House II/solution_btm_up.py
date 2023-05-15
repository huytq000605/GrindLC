class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        # can use costs as the dp to get amortize space
        dp = costs[0]
        for i in range(1, m):
            # previous min
            min1 = min(dp)
            idx = dp.index(min1)
            # second previous min
            min2 = min(dp[:idx] + dp[idx+1:])
            for j in range(n):
                # cannot take same 2 consecutive
                if j == idx:
                    dp[j] = min2 + costs[i][j]
                else:
                    dp[j] = min1 + costs[i][j]
        return min(dp)
