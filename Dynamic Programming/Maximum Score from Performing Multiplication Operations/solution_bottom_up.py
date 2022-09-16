class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)
        dp = [[0 for j in range(m+1)] for i in range(m+1)]
        for k in range(m-1, -1, -1):
            for left in range(k, -1, -1):
                dp[k][left] = max(dp[k+1][left] + nums[n-1-k+left] * muls[k],
                                 dp[k+1][left+1] + nums[left] * muls[k])
        return dp[0][0]
"""" More optimize
class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)
        dp = [0 for j in range(m+1)]
        for k in range(m-1, -1, -1):
            new_dp = [0 for j in range(m+1)]
            for left in range(k, -1, -1):
                new_dp[left] = max(dp[left] + nums[n-1-k+left] * muls[k],
                                 dp[left+1] + nums[left] * muls[k])
            dp = new_dp
        return dp[0]
""""
