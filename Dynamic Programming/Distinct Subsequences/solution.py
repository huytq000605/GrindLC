class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        dp = [0 for _ in range(nt + 1)]
        dp[0] = 1
        for i in range(ns):
            for j in range(nt-1, -1, -1):
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
        return dp[-1] 

"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(idx1, idx2):
            if idx2 >= len(t):
                return 1
            if idx1 >= len(s):
                return 0
            result = 0
            if s[idx1] == t[idx2]:
                result += dfs(idx1 + 1, idx2 + 1)
            result += dfs(idx1 + 1, idx2)
            return result
        return dfs(0, 0)
"""
