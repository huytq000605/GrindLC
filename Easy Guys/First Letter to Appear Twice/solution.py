class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for letter in s:
            if letter in seen:
                return letter
            seen.add(letter)
        return ""
