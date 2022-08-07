class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1, n):
            dp[i+1] = nums[i] == nums[i-1] and dp[i-1]
            if i > 1:
                dp[i+1] = dp[i+1] or (nums[i] == nums[i-1] == nums[i-2] and dp[i-2])
                dp[i+1] = dp[i+1] or (nums[i] == nums[i-1] + 1 == nums[i-2] + 2 and dp[i-2])
        return dp[-1]
            
