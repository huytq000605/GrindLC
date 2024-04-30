class Solution:
    OFFSET = ord('a')
    def wonderfulSubstrings(self, word: str) -> int:
        counter = [0 for _ in range(1 << 10)]
        counter[0] = 1
        mask = 0
        result = 0
        for c in word:
            bit = ord(c) - self.OFFSET
            mask ^= 1 << bit
            for bit in range(10):
                result += counter[mask ^ (1 << bit)]
            result += counter[mask]
            counter[mask] += 1
        return result
