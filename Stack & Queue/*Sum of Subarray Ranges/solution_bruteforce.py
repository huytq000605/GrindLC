class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # [1,2,3,4,5]
        n = len(nums)
        result = 0
        for start in range(0, n):
            curMax = nums[start]
            curMin = nums[start]
            for end in range(start + 1, n):
                curMax = max(curMax, nums[end])
                curMin = min(curMin, nums[end])
                result += curMax - curMin
        
        return result
            