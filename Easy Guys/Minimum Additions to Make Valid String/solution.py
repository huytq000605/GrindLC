class Solution:
    def addMinimum(self, word: str) -> int:
        i = 0
        n = len(word)
        result = 0
        chrs = "abc"
        while i < len(word):
            for c in chrs:
                if i >= n or word[i] != c:
                    result += 1
                else:
                    i += 1
        return result
