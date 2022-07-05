class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        @cache
        def dfs(num):
            nonlocal nums
            if num not in nums:
                return 0
            return 1 + dfs(num-1)
        result = 0
        for num in nums:
            result = max(result, dfs(num))
        return result
 
