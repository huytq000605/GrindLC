class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = len(nums) - 1
        result = -1
        for i in range(len(nums)):
            while j >= 0 and nums[i] + nums[j] >= k:
                j -= 1
            if i == j: j -= 1
            if j >= 0:
                result = max(result, nums[i] + nums[j])
        return result
