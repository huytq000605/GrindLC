class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            while nums[i] == 0 and i > j: 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        k = len(nums) - 1 
        for i in range(len(nums)):
            while nums[i] == 2 and i < k:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            
            
