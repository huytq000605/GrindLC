class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, cost, max_val):
            if i >= n:
                if cost == k:
                    return 1
                return 0
            result = max_val * dfs(i+1, cost, max_val)
            result %= MOD
            for val in range(max_val + 1, m+1):
                result += dfs(i+1, cost + 1, val)
                result %= MOD
            return result
        return dfs(0, 0, 0)
