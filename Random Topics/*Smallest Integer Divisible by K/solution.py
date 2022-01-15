class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        seen = set()
        n = 0
        while True:
            n += 1
            remainder = (remainder * 10) % k + (1 % k)
            remainder %= k
            if remainder == 0:
                return n
            if remainder in seen:
                return -1
            seen.add(remainder)
