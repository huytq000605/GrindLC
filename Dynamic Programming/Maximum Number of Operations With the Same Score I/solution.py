class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        target = nums[0] + nums[1]
        ops = 0
        i = 0
        while i + 1 < len(nums) and nums[i] + nums[i+1] == target:
            i += 2
            ops += 1
        return ops
