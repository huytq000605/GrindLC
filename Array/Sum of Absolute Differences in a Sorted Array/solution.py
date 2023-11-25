class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        result[0] = sum(nums) - nums[0] * n
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            result[i] = result[i-1] + diff * (i-1) - diff * (n-1-(i+1) + 1)
        return result
        
