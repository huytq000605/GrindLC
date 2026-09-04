class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mins = [nums[-1] for _ in range(n)]
        for i in range(n-2, -1, -1):
            mins[i] = min(mins[i+1], nums[i])
        mx = nums[0]
        for i in range(n):
            mx = max(nums[i], mx)
            if mx - mins[i] <= k:
                return i
        return -1
