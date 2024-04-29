class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        bits = [0 for _ in range(47)]
        for num in nums:
            bit = 0
            while num:
                bits[bit] += num & 1
                num >>= 1
                bit += 1
        result = 0
        for bit in range(46):
            if bits[bit]: result += 1 << bit
            bits[bit+1] += bits[bit] >> 1
        return result
