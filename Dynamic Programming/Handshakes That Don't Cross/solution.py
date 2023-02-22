class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(n):
            if n <= 2: return 1
            result = 0
            for i in range(0, n-2+1, 2):
                result += dfs(i) * dfs(n-2-i)
            return result % MOD
        return dfs(numPeople)
