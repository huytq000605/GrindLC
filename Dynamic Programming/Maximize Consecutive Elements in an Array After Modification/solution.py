class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        result = 0
        for num in nums:
            dp[num+1] = dp[num] + 1
            dp[num] = dp[num-1] + 1
            result = max(result, dp[num])
            result = max(result, dp[num+1])
        return result
            
            
                
                
