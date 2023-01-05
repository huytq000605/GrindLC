class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            next_n = 0
            factors = 2
            cur = n
            while cur > 1:
                if cur % factors == 0:
                    next_n += factors
                    cur = cur // factors
                else:
                    factors += 1
            if next_n == n:
                return n
            n = next_n
        return 0
