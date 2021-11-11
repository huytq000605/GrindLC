class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(k): # Subarrays have maximum array element <= k
            nonlocal nums
            start = 0
            result = 0
            for i in range(len(nums)):
                if nums[i] > k:
                    start = i + 1
                    continue
                else:
                    result += i - start + 1
            return result
        return count(right) - count(left - 1)
            