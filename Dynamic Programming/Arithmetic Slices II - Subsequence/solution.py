class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [dict() for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                if diff not in dp[i]: dp[i][diff] = 0
                dp[i][diff] += dp[j].get(diff, 0) + 1
                if dp[j].get(diff, 0) >= 1:
                    result += dp[j].get(diff, 0)
        return result
                
                