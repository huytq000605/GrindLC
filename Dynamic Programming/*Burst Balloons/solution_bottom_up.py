class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n - 2, 0, -1):
            for j in range(i, n-1):
                result = 0
                for last in range(i, j + 1):
                    result = max(result, nums[i - 1] * nums[j + 1] * nums[last] + dp[i][last - 1] + dp[last + 1][j])
                dp[i][j] = result
        
        return dp[1][n-2]
