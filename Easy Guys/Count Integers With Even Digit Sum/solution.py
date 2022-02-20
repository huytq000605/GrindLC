class Solution:
    def countEven(self, num: int) -> int:
        result = 0
        for n in range(1, num + 1):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            if s % 2 == 0:
                result += 1
        return result