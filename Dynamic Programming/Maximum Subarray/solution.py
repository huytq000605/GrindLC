class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = -math.inf
        for num in nums:
            current = max(num, num + current)
            result = max(result, current)
        return result