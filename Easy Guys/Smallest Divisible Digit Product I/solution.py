class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num = n
            p = 1
            while num:
                d = num % 10
                p *= d
                num //= 10
            if p % t == 0:
                return n
            n += 1
        return 0
