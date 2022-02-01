class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        result = 0
        for price in prices:
            result = max(result, price - cur_min)
            cur_min = min(cur_min, price)
        return result