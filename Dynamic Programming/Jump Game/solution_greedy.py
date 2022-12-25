class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        for i in range(n):
            if max_jump >= i:
                max_jump = max(max_jump, i + nums[i])
        return max_jump >= n-1
        
