class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = 0
        for c in s[:n//2]:
            vowels += c in "ueoaiUEOAI"
        for c in s[n//2:]:
            vowels -= c in "ueoaiUEOAI"
        return vowels == 0
            
