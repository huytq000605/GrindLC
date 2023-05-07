class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        j = 1
        for i in range(n):
            while j < n and nums[i] == nums[j]:
                j += 1
            if j < n:
                j += 1
                result += 1
        return result
