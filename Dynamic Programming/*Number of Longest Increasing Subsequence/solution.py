class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        max_len = 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = [1, 1]
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
            
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                result = dp[i][1]
            elif dp[i][0] == max_len:
                result += dp[i][1]
        return result
