class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        median_idx = len(nums) // 2
        result = abs(nums[median_idx] - k)
        for i in range(len(nums)):
            if i == median_idx: continue
            if i < median_idx and nums[i] > k:
                result += (nums[i] - k)
            if i > median_idx and nums[i] < k:
                result += (k - nums[i])
        return result
