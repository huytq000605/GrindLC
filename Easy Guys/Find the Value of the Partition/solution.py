class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        result = math.inf
        for i in range(len(nums) - 1):
            result = min(result, nums[i+1] - nums[i])
        return result
