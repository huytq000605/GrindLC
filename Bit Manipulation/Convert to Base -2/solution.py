class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        result = ""
        while n != 0:
            result += str(n % 2)
            n = -(n >> 1)
        return result[::-1]