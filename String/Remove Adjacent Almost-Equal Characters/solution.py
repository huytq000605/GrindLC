class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        result = 0
        word = [ord(word[i]) for i in range(n)]
        for i in range(n):
            if i - 1 >= 0 and abs(word[i] - word[i-1]) < 2:
                word[i] = 0
                result += 1
            if i + 1 < n and abs(word[i] - word[i+1]) < 2:
                word[i+1] = 0
                result += 1
        return result
