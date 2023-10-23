class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n > 0
        # n = 2^x
        # x % 2 == 0
        return n > 0 and \
        n & (n-1) == 0 and \
        0b101010101010101010101010101010101 & n == n
