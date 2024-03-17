class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # 1. 3D Top Down
        # @cache
        # def dfs(i, s, picked):
        #     if s > k: return 0
        #     if i >= n:
        #         if s == k: return pow(2, n - picked, MOD)
        #         return 0
        #     return (dfs(i+1, s+nums[i], picked + 1) + dfs(i+1, s, picked)) % MOD
        # return dfs(0, 0, 0)

        # 2. Can be optimize more into DP 2D
        # @cache
        # def dfs(i, s):
        #     if s > k: return 0
        #     if i >= n:
        #         if s == k: return 1
        #         return 0
        #     return (dfs(i+1, s+nums[i]) + 2 * dfs(i+1, s)) % MOD
        # return dfs(0, 0)

        # 3. Bottom Up
        dp = [0 for _ in range(k + 1)]
        dp[0] = 1
        for i in range(n):
            next_dp = [0 for _ in range(k + 1)]
            for s in range(k+1):
                next_dp[s] = (2 * dp[s]) % MOD
                if s - nums[i] >= 0:
                    next_dp[s] += dp[s - nums[i]]
                    next_dp[s] %= MOD
            dp = next_dp
        return dp[k]
            
