class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def is_palindrome(i, j):
            if i >= j: return True
            return s[i] == s[j] and is_palindrome(i+1, j-1)
        
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                result += is_palindrome(i, j)
        return result
