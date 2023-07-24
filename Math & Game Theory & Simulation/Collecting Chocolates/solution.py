class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        result = sum(nums)
        
        prices = [nums[i] for i in range(n)]
        for op in range(1, n):
            new_prices = [prices[i] for i in range(n)]
            for i in range(n):
                new_prices[i] = min(new_prices[i], prices[(i - 1 + n) % n])
            prices = new_prices
            result = min(result, sum(prices) + op * x)
        return result
        
