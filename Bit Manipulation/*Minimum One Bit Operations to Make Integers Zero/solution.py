class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result = 0
        # transform from 100_000 -> 0: takes 2^6 - 1 steps
        # transform from 0 -> 100_000 also took the same

        # example
        # transform for example 111_001 to 0
        # assume that we need to transform from 100_000 to 0
        # eventually we will have a step where we need to transform from 111_001 to 0
        # transform from 100_000 to 111_001 takes the same as 11_001 to 0
        # that means fn(111_001) = fn(100_000) - fn(11_001)
        if n <= 1: return n
        msb = 0
        for bit in range(32, -1, -1):
            if (n >> bit) & 1:
                msb = bit
                break
        return (1<<(msb+1)) - 1 - self.minimumOneBitOperations(n & ~(1 << msb))
