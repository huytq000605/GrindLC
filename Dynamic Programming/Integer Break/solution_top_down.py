class Solution:
    def integerBreak(self, e: int) -> int:
        dp = [None for i in range(e + 1)]
        def dfs(n):
            if n == 1: return 1
            if dp[n] != None: return dp[n]
            res = n
            if n == e: res = 0
            for i in range(1, n):
                res = max(res, i * dfs(n - i))
            dp[n] = res
            return res
        return dfs(e)
        