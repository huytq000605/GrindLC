class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result = 1
        cur = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                cur += 1
            else:
                cur = 1
            result = max(result, cur)
        return result
