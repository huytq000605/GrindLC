class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        bits = [0 for _ in range(32)]
        def put(num, v):
            bit = 0
            while num:
                bits[bit] += v * (num & 1)
                num >>= 1
                bit += 1

        def val(bits):
            result = 0
            for bit in range(32):
                if bits[bit]: result |= 1 << bit
            return result 

        start = 0
        result = math.inf
        for i, num in enumerate(nums):
            put(num, 1)
            result = min(result, abs(k - val(bits)))
            while start <= i and val(bits) > k:
                put(nums[start], -1)
                start += 1
                if start <= i:
                    result = min(result, abs(k - val(bits)))
        return result

            
