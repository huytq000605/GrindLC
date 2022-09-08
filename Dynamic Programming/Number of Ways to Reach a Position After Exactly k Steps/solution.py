class Solution:
    def numberOfWays(self, start: int, end: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(pos, k):
            if k == 0:
                if pos == end:
                    return 1
                return 0
            return (dfs(pos + 1, k - 1) + dfs(pos - 1, k - 1)) % MOD
        return dfs(start, k)
