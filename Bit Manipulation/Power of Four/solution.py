class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n > 0
        # Is power of 2
        # Log2(n) % 2 == 0
        return n > 0 and n & (n-1) == 0 and 0b1010101010101010101010101010101 & n == n