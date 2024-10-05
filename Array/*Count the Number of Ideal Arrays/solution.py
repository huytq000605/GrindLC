class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        # The last value that array end with, k is number of increasing point
        @cache
        def dfs(value, k):
            result = math.comb(n-1, k)
            if k == n-1:
                return result
            nxt = value + value
            while nxt <= maxValue:
                result += dfs(nxt, k+1)
                nxt += value
            return result % MOD
        result = 0
        for i in range(1, maxValue + 1):
            result += dfs(i, 0)
        return result % MOD
