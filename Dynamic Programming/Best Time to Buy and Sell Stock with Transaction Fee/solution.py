class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dfs(idx, hold):
            if idx >= n:
                return 0
            action = 0
            if hold:
                action = prices[idx] + dfs(idx + 1, False)
            else:
                action = -prices[idx] - fee + dfs(idx + 1, True)
            doNothing = dfs(idx + 1, hold)
            return max(action, doNothing)
        return dfs(0, False)