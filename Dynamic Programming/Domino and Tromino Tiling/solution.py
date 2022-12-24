class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, j):
            print(i, j)
            if i == n and j == n:
                return 1
            if i > n or j > n:
                return 0
            if j > i:
                return dfs(j, i)
            res = 0
            if i - j == 1:
                res += dfs(i + 1, j + 2)
            if i == j:
                res += dfs(i+1, j+1)
                res += dfs(i+2, j+1)
                res += dfs(i+1, j+2)
            res += dfs(i, j+2)
            return res % MOD
        return dfs(0, 0)
