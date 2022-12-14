class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        @cache
        def dfs(i1, i2):
            if i1 >= m or i2 >= n:
                return 0
            if text1[i1] == text2[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            return max(dfs(i1 + 1, i2), dfs(i1, i2+1))
        return dfs(0, 0)
