class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            while start < mid and nums[mid] == nums[start]:
                start += 1
            while end > mid and nums[mid] == nums[end]:
                end -= 1
            if nums[mid] >= nums[start]:
                if nums[mid] >= target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return nums[start] == target
