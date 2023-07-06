class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        start = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            while s - nums[start] >= target:
                s -= nums[start]
                start += 1
            if s >= target:
                result = min(result, i - start + 1)
        if result == len(nums) + 1:
            return 0
        return result
