class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None for j in range(2)] for i in range(len(prices))]
        def dfs(day, holdStock):
            if day >= len(prices):
                return 0
            if dp[day][holdStock] is not None: return dp[day][holdStock]
            result = 0
            if holdStock:
                result = prices[day] + dfs(day + 1, 0)
            else:
                result = -prices[day] + dfs(day + 1, 1)
            result = max(result, dfs(day + 1, holdStock))
            dp[day][holdStock] = result
            return result
        return dfs(0, 0)
            