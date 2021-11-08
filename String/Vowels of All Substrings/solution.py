class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        result = 0
        for i in range(len(word)):
            if word[i] in vowels:
                result += (i + 1) * (len(word) - i)
        return result