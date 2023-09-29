class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(1, len(nums)):
            increasing = increasing and (nums[i] >= nums[i-1])
            decreasing = decreasing and (nums[i] <= nums[i-1])
        return increasing or decreasing
