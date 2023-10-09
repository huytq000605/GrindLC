class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def binary_search(num):
            start = 0
            end = n
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        left = binary_search(target)
        if left == n or nums[left] != target:
            return [-1, -1]
        right = binary_search(target + 1) - 1
        if left > right:
            right = left
        return [left, right]
