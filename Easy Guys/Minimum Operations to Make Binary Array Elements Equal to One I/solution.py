class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                if i + 2 >= len(nums): return -1
                nums[i+1] = not nums[i+1]
                nums[i+2] = not nums[i+2]
                result += 1
        return result
        
                
