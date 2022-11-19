class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = set([nums[i] + nums[n-1-i] for i in range(n//2)])
        return len(s)
        
        
