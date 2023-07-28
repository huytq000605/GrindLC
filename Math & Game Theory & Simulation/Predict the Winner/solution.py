class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            return max(-dfs(i+1, j) + nums[i], -dfs(i, j-1) + nums[j])
        return dfs(0, len(nums) - 1) >= 0
