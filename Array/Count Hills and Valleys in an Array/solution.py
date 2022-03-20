class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = nums[0]
        i = 0
        j = 0
        result = 0
        while i < len(nums) - 1:
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j >= len(nums):
                break
            if nums[i] < prev and nums[i] < nums[j]:
                result += 1
            elif nums[i] > prev and nums[i] > nums[j]:
                result += 1
            prev = nums[i]
            i = j
        return result