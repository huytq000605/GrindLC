class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        MOD = 10**9 + 7
        msb = 0
        for i in range(1, n+1):
            if 1 << msb == i:
                msb += 1
            result <<= msb
            result += i
            result %= MOD
        return result
