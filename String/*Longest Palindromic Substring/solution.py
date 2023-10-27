class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def extend(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1
        result = ""
        for i in range(n):
            a, b = extend(i, i)
            if b - a + 1 > len(result): result = s[a:b+1]
            a, b = extend(i, i+1)
            if b - a + 1 > len(result): result = s[a:b+1]
        return result

