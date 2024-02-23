class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1 = k*num2 + (2**i1 + 2**i2 + ... + 2**ik with i can be any in [0, 61])
        # => (2**i1 + 2**i2 + ... + 2**ik) = num = num1 - k*num2
        for k in range(61):
            num = num1 - k*num2
            bc = num.bit_count()
            # each operation can set only 1 more bit: bc <= k
            # each operation add at least 1 (2^0): k <= num
            if bc <= k <= num:
                return k
        return -1
