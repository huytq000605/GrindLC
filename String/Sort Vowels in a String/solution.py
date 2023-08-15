class Solution:
    def sortVowels(self, s: str) -> str:
        vowels, non_vowels = [], []
        for c in s:
            if c in "ueoaiUEOAI":
                vowels.append(c)
            else:
                non_vowels.append(c)
        vowels.sort()
        vowels = vowels[::-1]
        non_vowels = non_vowels[::-1]
        result = ""
        for c in s:
            if c in "ueoaiUEOAI":
                result += vowels.pop()
            else:
                result += non_vowels.pop()
        return result
                
