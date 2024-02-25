class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for target in set([nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]]):
            dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
            for i in range(n-2, -1, -1):
                for j in range(i + 1, n):
                    if nums[i] + nums[i+1] == target: dp[i][j] = max(dp[i][j], 1 + dp[i+2][j])
                    if nums[i] + nums[j] == target: dp[i][j] = max(dp[i][j], 1 + dp[i+1][j-1])
                    if nums[j-1] + nums[j] == target: dp[i][j] = max(dp[i][j], 1 + dp[i][j-2])
                    result = max(result, dp[i][j])
        return result
        
    
