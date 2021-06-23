from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def helper(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            deleteWord1 = 1 + helper(i+1, j)
            deleteWord2 = 1 + helper(i, j + 1)
            result = min(deleteWord1, deleteWord2)
            return result
        return helper(0,0)