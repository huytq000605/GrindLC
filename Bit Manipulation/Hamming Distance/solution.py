class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        for i in range(32):
            if ((x >> i) ^ (y >> i)) & 0b1 == 1:
                result += 1
        return result

    def alternative(self, x: int, y: int) -> int:
        xor = x^y
        result = 0
        while xor > 0:
            result += 1
            xor &= (xor-1)
        return result
