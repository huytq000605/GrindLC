class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        cur, result = 0, 0
        for num in nums:
            if num == max_num:
                cur += 1
            else:
                cur = 0
            result = max(cur, result)
        return result
