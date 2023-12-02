class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        for bit in range(n-1, -1, -1):
            # if a bit and b bit are equal, choose value for both of them to be 1
            if (a >> bit) & 1 == (b >> bit) & 1:
                a |= 1 << bit
                b |= 1 << bit
            else:
                # because we need a * b
                # so result will be bigger if difference between a & b is smaller
                # so check which number is smaller, makes it 1 at that bit
                prefix_a = (a >> bit) & ~1
                prefix_b = (b >> bit) & ~1
                if prefix_a < prefix_b:
                    a |= 1 << bit
                    b &= ~(1 << bit)
                elif prefix_a > prefix_b:
                    a &= ~(1 << bit)
                    b |= (1 << bit)
                else:
                    suffix_a = a & ((1 << bit) - 1)
                    suffix_b = b & ((1 << bit) - 1)
                    if suffix_a < suffix_b:
                        a |= 1 << bit
                        b &= ~(1 << bit)
                    else:
                        a &= ~(1 << bit)
                        b |= (1 << bit)
        return (a*b) % MOD
