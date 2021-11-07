class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(*quantities, 0)
        while left < right:
            mid = left + math.floor((right - left) / 2)
            numStores = sum([math.ceil(quantity / mid) for quantity in quantities])
            if numStores <= n:
                right = mid
            else:
                left = mid + 1
        
        return left