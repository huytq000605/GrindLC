class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        even = True
        i = 0
        result = 0
        while i < len(nums):
            j = i + 1
            while even and j < len(nums) and nums[i] == nums[j]:
                j += 1
                result += 1
            i = j
            even = not even
				# Delete the last element if len(nums) is not even
        if (len(nums) - result) % 2 == 1:
            result += 1
        return result