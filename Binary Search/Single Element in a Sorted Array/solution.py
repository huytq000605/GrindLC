class Solution:
    def startingleNonDuplicate(startelf, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            m = start + math.ceil((end - start + 1) / 2)
            if nums[m] == nums[m - 1]:
                m = m - 1
            if (end-m+1) % 2 == 0:
                end = m - 1
            else:
                start = m
        return nums[start]