class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = nums[-1] - nums[0] - 1 - (n-2)
        if diff < k:
            return nums[-1] + k - diff
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            diff = (nums[mid] - nums[0] - 1) - (mid - 1)
            if diff < k:
                start = mid + 1
            else:
                end = mid
        diff = (nums[start-1] - nums[0] - 1) - (start-1 - 1)
        return nums[start-1] + k - diff
