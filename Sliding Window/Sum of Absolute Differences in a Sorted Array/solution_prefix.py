class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        result = [nums[i] * (i+1) - prefix[i] + prefix[-1] - prefix[i+1] - nums[i] * (n-i) for i in range(n)]
        return result
        
