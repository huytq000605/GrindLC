class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        seen = set()
        j = 0
        result = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.discard(s[j])
                j += 1
            seen.add(s[i])
            result += i - j + 1
        return result
