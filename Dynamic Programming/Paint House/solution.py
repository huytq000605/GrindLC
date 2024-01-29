class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0, 0, 0]
        for house in costs:
            dp = [house[j] + min(dp[k] for k in range(3) if k != j) for j in range(3)]
        return min(dp)
