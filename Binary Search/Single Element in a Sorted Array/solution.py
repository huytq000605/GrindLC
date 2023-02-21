class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:      
            mid = start + (end - start) // 2
            # check if target is on the right of mid
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or \
                (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                start = mid + 1
            else:
                end = mid
        return nums[start]
