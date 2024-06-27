class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bx, bn = 1, 1
        # x is a valid num
        # so need to find (n-1) nums larger than x
        # just need to keep all the 1-bits alone, set 0-bits in x as the sequence bits of (n-1)
        while bn < n:
            if (n-1) & bn == 0:
                while x & bx:
                    bx <<= 1
                bx <<= 1
            else:
                while x & bx:
                    bx <<= 1
                x |= bx
            bn <<= 1
        return x
