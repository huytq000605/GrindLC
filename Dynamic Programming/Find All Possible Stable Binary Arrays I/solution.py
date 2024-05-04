class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(zero, one, prev):
            if not zero and not one: return 1
            if (not zero or not one) and zero + one > limit: return 0
            result = 0
            if prev != 0:
                for t in range(1, min(limit, zero) + 1):
                    result = (result + dfs(zero - t, one, 0)) % MOD
            if prev != 1:
                for t in range(1, min(limit, one) + 1):
                    result = (result + dfs(zero, one - t, 1)) % MOD
            return result
        return dfs(zero, one, -1)
