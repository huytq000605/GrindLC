class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # a & b + a | b = set_bits(a) + set_bits(b)
        nums = set(nums)
        count = [0 for i in range(31)]
        for num in nums:
            bits = 0
            while num:
                bits += (num & 1)
                num >>= 1
            count[bits] += 1
        i, j = 1, 30
        result = 0
        prefix = 0
        while i <= 30:
            while i + j >= k and j >= 0:
                prefix += count[j]
                j -= 1
            result += prefix * count[i]
            i += 1
        return result
