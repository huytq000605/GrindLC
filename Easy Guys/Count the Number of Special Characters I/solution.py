class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set()
        result = 0
        for c in word:
            if c in seen: continue
            if c.upper() in seen: result += 1
            elif c.lower() in seen: result += 1
            seen.add(c)
        return result
