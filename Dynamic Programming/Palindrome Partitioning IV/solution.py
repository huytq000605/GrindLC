class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def is_palindrome(start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return is_palindrome(start + 1, end - 1)
        
        for i in range(1, n-1):
            for j in range(i, n-1):
                if not is_palindrome(0, i-1):
                    break
                if is_palindrome(i, j) and is_palindrome(j+1, n-1):
                    return True
        return False
