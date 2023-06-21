class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        start, end = min(nums), max(nums)
        result = sum([abs(nums[i] - start) * cost[i] for i in range(n)])
        while start < end:
            mid = start + (end - start) // 2
            c = sum([abs(mid - nums[i]) * cost[i] for i in range(n)])
            c_next = sum([abs(mid + 1 - nums[i]) * cost[i] for i in range(n)])
            if c < c_next:
                end = mid
            # in case it's equal, we can think of it as 2 medians situations
            # it will have only up to 2 medians. so the answer's moving to the right.
            else:
                start = mid + 1
            result = min(result, c, c_next)
        return result
