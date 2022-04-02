class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        xor = start ^ goal
        for i in range(32):
            if (xor >> i) & 1:
                result += 1
        return result