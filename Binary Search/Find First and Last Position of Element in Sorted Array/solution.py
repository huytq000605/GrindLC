class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end-start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        result = [-1, -1]
        if nums[start] == target:
            result[0] = start
        else:
            return result

        end = len(nums) - 1
        while start < end:
            mid = start + math.ceil((end - start) / 2)
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        result[1] = start
        return result
