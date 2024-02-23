class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        result = 0
        while k or xor:
            result += (k & 1) != (xor & 1)
            k >>= 1
            xor >>= 1
        return result
