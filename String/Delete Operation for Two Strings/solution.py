class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def dfs(idx1, idx2):
            if idx1 >= n:
                return m - idx2
            elif idx2 >= m:
                return n - idx1
            
            if word1[idx1] == word2[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            return 1 + min(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
        return dfs(0, 0)