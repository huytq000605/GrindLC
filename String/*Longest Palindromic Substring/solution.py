class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""
        
        def extend(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
    
        for i in range(n):
            st = extend(i, i + 1)
            if len(st) > len(result):
                result = st
            st = extend(i, i)
            if len(st) > len(result):
                result = st

        return result