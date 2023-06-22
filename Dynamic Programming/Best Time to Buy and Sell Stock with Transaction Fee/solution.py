class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(i, hold):
            if i >= len(prices):
                return 0
            result = dfs(i+1, hold)
            if hold:
                result = max(result, dfs(i+1, False) + prices[i] - fee)
            else:
                result = max(result, dfs(i+1, True) - prices[i])
            return result
        return dfs(0, False)
