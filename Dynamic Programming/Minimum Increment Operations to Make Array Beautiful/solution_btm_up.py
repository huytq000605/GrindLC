class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [math.inf for i in range(n+1)]
        dp[0] = 0
        # can optimize where we only need len(dp) = 3
        for i in range(n):
            for j in range(4):
                if i + 1 - j >= 0:
                    dp[i+1] = min(dp[i+1], dp[i-j+1] + max(0, k - nums[i]))
        return min(dp[-3:])
