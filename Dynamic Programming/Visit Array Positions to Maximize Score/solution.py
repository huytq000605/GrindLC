class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, parity):
            if i >= n:
                return 0
            result = dfs(i+1, parity)
            if parity == nums[i] % 2:
                result = max(result, nums[i] + dfs(i+1, nums[i] % 2))
            else:
                result = max(result, -x + nums[i] + dfs(i+1, nums[i] % 2))
            return result
        return dfs(1, nums[0] % 2) + nums[0]
