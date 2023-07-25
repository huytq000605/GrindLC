class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        for i in range(n-1, 0, -1):
            if nums[i] >= nums[i-1]:
                nums[i-1] += nums[i]
            result = max(result, nums[i], nums[i-1])
        return result
