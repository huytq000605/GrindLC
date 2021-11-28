class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = 0
        maxIdx = 0
        for i, num in enumerate(nums):
            if num < nums[minIdx]:
                minIdx = i
            if num > nums[maxIdx]:
                maxIdx = i
        n = len(nums)
        result = min(max(maxIdx + 1, minIdx + 1), max(n - maxIdx, n - minIdx), minIdx + 1 + (n - maxIdx), maxIdx + 1 + (n- minIdx))
        return result