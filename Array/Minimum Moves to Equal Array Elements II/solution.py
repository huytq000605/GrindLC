class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for num in nums:
            result += abs(num - nums[n//2])
        return result
    
