class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        end = n-1
        result = 0
        for start in range(n):
            while end > start and nums[start] + nums[end] >= target:
                end -= 1
            if start >= end: break
            result += end - start
        return result
