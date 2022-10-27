class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        result = 1
        start = 0
        for end, num in enumerate(nums):
            while s | num != s + num:
                s -= nums[start]
                start += 1
            s += num
            result = max(end - start + 1, result)
        return result
