class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        
        result = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = [*dp[j], nums[i]]
                    if len(dp[i]) > len(dp[result]):
                        result = i
                    
        return dp[result]