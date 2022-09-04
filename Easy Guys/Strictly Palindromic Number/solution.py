class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # The number n > 4 in base (n - 2) is always 12, which is not palindromic.
        # base 2 of 4 is 100
        return False
