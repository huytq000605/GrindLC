class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n//2):
            result = max(result, nums[i] + nums[n-1-i])
        return result
