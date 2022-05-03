class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        left = 0
        right = -1
        
        for i, num in enumerate(nums):
            if num >= prev:
                prev = num
            else:
                right = i
        
        prev = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                left = i
        
        return right - left + 1