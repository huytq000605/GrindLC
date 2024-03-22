class Solution:
    def removeVowels(self, s: str) -> str:
        result = ""
        for c in s:
            if c in "ueoai": continue
            result += c
        return result
