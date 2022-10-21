class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        result = -1
        for num in nums:
            if num > result and -num in s:
                result = num
        return result
