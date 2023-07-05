class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        start = 0
        k = 0
        for i, num in enumerate(nums):
            if num == 0:
                k += 1
            while k > 1:
                if nums[start] == 0:
                    k -= 1
                start += 1
            result = max(result, i - start)
        return result
