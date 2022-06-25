class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        def is_non_decreasing(start):
            for i in range(max(0, start), n-1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                original = nums[i]
                nums[i] = nums[i+1]
                if is_non_decreasing(i-1):
                    return True
                nums[i] = original
                nums[i+1] = nums[i]
                if is_non_decreasing(i+1):
                    return True
                return False
        return True
                
