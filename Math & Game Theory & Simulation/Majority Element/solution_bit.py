class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0 for _ in range(32)]
        max_freq = 0
        for num in nums:
            if num < 0:
                num = -num
                bits[31] += 1
            bit = 0
            while num:
                bits[bit] += (num & 1)
                num >>= 1
                bit += 1
                max_freq = max(max_freq, bits[bit])
        result = 0
        half = (len(nums) + 1) // 2
        for bit in range(30):
            if bits[bit] >= half:
                result |=  1 << bit
        if bits[31] >= half:
            result = -result
        return result
