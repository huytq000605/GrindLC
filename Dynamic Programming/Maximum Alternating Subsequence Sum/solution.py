class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = [[None for i in range(2)] for i in range(len(nums))]
        def dfs(idx, isEvenIdx):
            if idx >= len(nums):
                return 0
            if dp[idx][isEvenIdx] is not None: return dp[idx][isEvenIdx]
            
            result = 0
            if isEvenIdx:
                result = nums[idx] + dfs(idx + 1, 0)
            else:
                result = -nums[idx] + dfs(idx + 1, 1)
            result = max(result, dfs(idx + 1, isEvenIdx))
            dp[idx][isEvenIdx] = result
            return result
        
        return dfs(0, 1)