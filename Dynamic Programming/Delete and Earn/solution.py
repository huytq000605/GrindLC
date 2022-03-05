class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        dp = [0 for i in range(10**4 + 1)]
        dp[0] = counter[0] * 0
        dp[1] = max(dp[0], counter[1])
        for i in range(2, 10**4 + 1):
            dp[i] = max(dp[i-2] + counter[i] * i, dp[i-1])
        return dp[-1]