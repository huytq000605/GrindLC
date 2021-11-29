class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(idx1, idx2):
            if idx1 >= len(word1) and idx2 >= len(word2):
                return 0
            if idx1 >= len(word1):
                return len(word2) - idx2
            if idx2 >= len(word2):
                return len(word1) - idx1
            if word1[idx1] == word2[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            else:
                add = 1 + dfs(idx1, idx2 + 1)
                replace = 1 + dfs(idx1 + 1, idx2 + 1)
                delete = 1 + dfs(idx1 + 1, idx2)
                result = min(add, replace, delete)
                return result
        return dfs(0, 0)