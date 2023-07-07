class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        result = 0
        cur = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > threshold:
                cur = 0
                continue
            if not cur and nums[i] % 2 == 0:
                cur = 1
                result = max(result, cur)
                continue
            if cur:
                if nums[i] % 2 != nums[i-1] % 2:
                    cur += 1
                    result = max(result, cur)
                else:
                    cur = 0
                    if nums[i] % 2 == 0:
                        cur = 1
        return result
                    
