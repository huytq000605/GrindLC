class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur = 0
        idx = 0
        m = len(nums)
        result = 0
        while cur < n:
            # If we can still use some values from nums
            if idx < m:
                # We cannot use the nums[idx], we patch the array
                if nums[idx] > cur + 1:
                    cur += (cur + 1)
                    result += 1
                # We can use the nums[idx]
                else:
                    cur += nums[idx]
                    idx += 1
            # We patch the array
            else:
                cur += (cur + 1)
                result += 1
        return result
