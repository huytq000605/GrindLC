class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        mn = -1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if mn != -1:
                    return -1
                mn = i+1
        if mn == -1: return 0
        nums = nums[mn:] + nums[:mn]
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return -1
        return n-mn
            
