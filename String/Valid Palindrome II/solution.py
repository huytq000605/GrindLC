class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right, k):
            if left >= right:
                return True
            if s[left] == s[right]:
                return is_palindrome(left + 1, right - 1, k)
            if s[left] != s[right] and k == 0:
                return is_palindrome(left + 1, right, k + 1) or is_palindrome(left, right - 1, k + 1)
            return False
        return is_palindrome(0, len(s) - 1, 0)