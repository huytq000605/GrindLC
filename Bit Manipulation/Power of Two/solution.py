class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # Power of two is number have only 1 bit as MSB
        return not n&(n-1)
