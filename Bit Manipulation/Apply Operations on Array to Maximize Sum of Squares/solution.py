class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0 for _ in range(30)]
        for num in nums:
            bit = 0
            while num:
                bits[bit] += num & 1
                num >>= 1
                bit += 1
        
        result = 0
        MOD = 10**9 + 7
        for _ in range(k):
            num = 0
            for bit in range(30):
                if bits[bit]:
                    bits[bit] -= 1
                    num += 1 << bit
            result += num ** 2
            result %= MOD
        return result
