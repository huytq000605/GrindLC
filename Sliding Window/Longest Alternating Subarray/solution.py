class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        diff = 1
        cur = 1
        for i in range(1, n):
            if nums[i] - nums[i-1] == diff:
                diff = -diff
                cur += 1
            else:
                diff = 1
                cur = 1
                if nums[i] - nums[i-1] == diff:
                    diff = -diff
                    cur += 1
            result = max(result, cur)

            
        if result <= 1: return -1
        return result
