class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        result = 0
        k = 2
        for target in range(k):
            # dp[mod] = longest length of subsequent end with mod
            dp = [0 for _ in range(k)]
            for num in nums:
                num %= k
                dp[num] = max(dp[num], dp[(target - num + k) % k] + 1)
                result = max(result, dp[num])
        return result
