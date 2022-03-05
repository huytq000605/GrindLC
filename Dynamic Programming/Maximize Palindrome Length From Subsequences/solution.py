class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        ans = 0
        @cache
        def LPS(idx1, idx2):
            nonlocal word, ans
            if idx1 > idx2:
                result = 0
            elif idx1 == idx2:
                result = 1
            elif word[idx1] == word[idx2]:
                result = 2 + LPS(idx1 + 1, idx2 - 1)
                if idx1 < len(word1) and idx2 >= len(word1):
                    ans = max(result, ans)
            else:
                result = max(LPS(idx1 + 1, idx2), LPS(idx1, idx2 - 1))
            
            return result
        LPS(0, len(word) - 1)
        return ans