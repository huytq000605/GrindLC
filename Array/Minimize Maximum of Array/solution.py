class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = 0
        total = 0
        for i, num in enumerate(nums):
            total += num
            result = max(result, math.ceil(total / (i+1)))
        return result
