class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor = 0
        result = []
        for num in nums:
            xor ^= num
        max_xor = (1 << maximumBit) - 1
        for removed_idx in range(n-1, -1, -1):
            result.append(xor ^ max_xor)
            xor ^= nums[removed_idx]
        return result
