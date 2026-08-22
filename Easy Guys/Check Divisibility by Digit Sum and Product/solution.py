class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p, s = 1, 0
        num = n
        while n:
            d = n % 10
            p *= d
            s += d
            n //= 10
        return (num % (p + s)) == 0
