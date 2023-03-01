class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(start, end):
            if start >= end:
                return
            pivot = nums[end]
            j = start - 1
            for i in range(start, end):
                if nums[i] <= pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1
            nums[j], nums[end] = nums[end], nums[j]
            qs(start, j-1)
            qs(j+1, end)
        qs(0, len(nums) - 1)
        return nums
            
