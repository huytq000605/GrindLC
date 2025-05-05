class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, prev_gap):
            if i > n: return 0
            if i == n: return 1 if not prev_gap else 0
            if prev_gap:
                return (dfs(i+1, False) + dfs(i+1, True)) % MOD
            else:
                return (dfs(i+1, False) + dfs(i+2, False) + 2*dfs(i+2, True))%MOD
        return dfs(0, False)
