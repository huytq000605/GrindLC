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