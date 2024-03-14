class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        j = 0
        result = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i-1]:
                j = i
            result += i - j + 1
        return result
