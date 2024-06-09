class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if (nums[mid] - nums[0] + 1) - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid
        # arr[start-1] has (arr[start-1] - arr[0] + 1) - (start-1 + 1) missing numbers
        # find the (k - (arr[start-1] - arr[0] + 1) + start) missing numbers between start-1 and start
        # => k + arr[0] - 1 + start
        return k + nums[0] - 1 + start  
