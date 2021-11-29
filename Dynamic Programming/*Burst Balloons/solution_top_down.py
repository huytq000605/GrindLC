class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]
        # dfs(start, end) is mean burst baloons the way that nums[start] => nums[end] are the last baloons to burst
        @cache
        def dfs(start, end):
            if start > end:
                return 0
            result = 0
            left = nums[start - 1]
            right = nums[end + 1]
            for i in range(start, end + 1):
                result = max(result, left * nums[i] * right + dfs(start, i - 1) + dfs(i + 1, end))
            return result
        return dfs(1, len(nums) - 2)