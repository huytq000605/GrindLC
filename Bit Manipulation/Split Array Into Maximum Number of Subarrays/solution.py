class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cur = (1 << 30) - 1
        result = 0
        for num in nums:
            cur &= num
            # only split when subarray = 0
            if cur == 0:
                result += 1
                cur = (1 << 30) - 1
        return max(1, result)
