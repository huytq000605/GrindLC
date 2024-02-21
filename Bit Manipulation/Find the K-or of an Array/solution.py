class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit in range(32):
            t = 0
            for num in nums:
                t += (num >> bit) & 1
            if t >= k:
                result |= (1<<bit)
        return result
