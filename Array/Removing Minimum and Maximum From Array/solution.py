class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn, mx = 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] < nums[mn]:
                mn = i
            if nums[i] > nums[mx]:
                mx = i
        i = min(mn, mx)
        j = max(mn, mx)
        return min(j+1, n-i, i+1 + n-j)
