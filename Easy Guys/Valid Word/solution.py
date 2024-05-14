class Solution:
    def isValid(self, word: str) -> bool:
        vowel = False
        consonant = False
        for c in word:
            if not (c.isdigit() or c.isalpha()): return False
            if c.isalpha():
                vowel = vowel or c in "UEOAIueoai"
                consonant = consonant or c not in "ueoaiUEOAI"
        return len(word) >= 3 and vowel and consonant 
