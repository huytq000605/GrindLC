class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = 0
        i = 0
        while i < len(nums) and i <= maxPos:
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= len(nums) - 1: return True
            i += 1
        return False