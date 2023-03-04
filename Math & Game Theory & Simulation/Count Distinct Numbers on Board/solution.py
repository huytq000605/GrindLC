class Solution:
    def distinctIntegers(self, n: int) -> int:
        # n % (n-1) = 1 for every n > 2
        if n <= 2: return 1
        return n - 1
                        
