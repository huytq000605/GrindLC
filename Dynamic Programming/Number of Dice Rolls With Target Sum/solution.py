class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, cur):
            if cur == target and i == n:
                return 1
            if cur > target or i == n:
                return 0
            res = 0
            for val in range(1, k+1):
                res += dfs(i+1, cur+val)
            return res % MOD
        return dfs(0, 0)
