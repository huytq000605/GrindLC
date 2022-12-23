class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, holding):
            if i >= n:
                return 0
            res = dfs(i+1, holding)
            if holding:
                res = max(res, dfs(i + 2, False) + prices[i])
            else:
                res = max(res, dfs(i+1, True) - prices[i])
            return res
        return dfs(0, False)
