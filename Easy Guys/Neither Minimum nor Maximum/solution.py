class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return -1
        nums = sorted(nums)
        return nums[1]
        
