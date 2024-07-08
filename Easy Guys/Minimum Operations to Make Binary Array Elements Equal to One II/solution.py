class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums)):
            if (nums[i] + flips) & 1 == 0:
                flips += 1
        return flips
