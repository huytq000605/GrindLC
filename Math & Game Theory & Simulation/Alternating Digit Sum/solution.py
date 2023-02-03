class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        result = 0
        while n:
            sign = -sign
            result += sign * (n % 10)
            n //= 10
        return result * sign
