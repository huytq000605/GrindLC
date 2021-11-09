class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(idx, currentValue):
            if idx == len(nums):
                if currentValue == target:
                    return 1
                return 0
            result = 0
            result = dfs(idx + 1, currentValue + nums[idx]) + dfs(idx + 1, currentValue - nums[idx])
            return result
        return dfs(0, 0)