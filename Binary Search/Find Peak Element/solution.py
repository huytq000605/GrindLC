class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        # We always have nums[start] > nums[start-1] and nums[end] > nums[end + 1]
        # So in the end, when we have only 2 elements left, the peak must be 1 of them
        # The testcases don't contain the case where nums[i] == nums[i+1]
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
