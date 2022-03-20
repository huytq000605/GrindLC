class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k % 2 == 1:
            return -1
        if len(nums) == 1 or k == 0:
            return nums[0]
        
        if k == 1:
            return nums[1]
        
        # We can take whatever we we want
        if k > len(nums):
            return max(nums)
        
        if k == len(nums):
            return max(nums[:k-1])
        nums = nums[:k+1]
        # Can remove k first elements to get nums[k+1]
        result = nums[-1]
        
        # Cannot get kth elements
        nums = nums[:k-1]
        return max(result, max(nums[:k-1]))