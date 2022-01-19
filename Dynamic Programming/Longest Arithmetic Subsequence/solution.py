class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(lambda: 1) for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j][diff] + 1
                result = max(result, dp[i][diff])
                    
        return result