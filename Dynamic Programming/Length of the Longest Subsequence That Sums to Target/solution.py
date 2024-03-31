class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            for s in range(target + 1):
                if i > 0:
                    dp[i][s] = dp[i-1][s]
                if s - nums[i] >= 0 and (dp[i-1][s-nums[i]] or s == nums[i]):
                    dp[i][s] = max(dp[i][s], dp[i-1][s - nums[i]] + 1)
        if dp[n-1][target] == 0:
            return -1
        return dp[n-1][target]
        
            
