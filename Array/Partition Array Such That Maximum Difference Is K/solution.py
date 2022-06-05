class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        i = 1
        start = 0
        while i < len(nums):
            if nums[i] - nums[start] > k:
                result += 1
                start = i
            i += 1
        return result