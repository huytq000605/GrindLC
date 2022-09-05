class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(1, n):
            s = nums[i] + nums[i-1]
            if s in seen:
                return True
            seen.add(s)
        return False
