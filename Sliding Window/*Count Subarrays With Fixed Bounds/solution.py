class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start = 0
        imin, imax = -1, -1
        result = 0
        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                imin = -1
                imax = -1
                start = i+1
            if num == maxK:
                imax = i
            if num == minK:
                imin = i
            if imin != -1 and imax != -1:
                result += min(imax, imin) - start + 1
        return result
