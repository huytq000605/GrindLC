class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            
            while nums[mid] == nums[end] and end > mid:
                end -= 1
            while nums[mid] == nums[start] and start < mid:
                start += 1
            if nums[mid] >= nums[start]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False