class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        incr = True
        result = 1
        cur = 1
        for num in nums[1:]:
            if incr and num > prev:
                cur += 1
            elif not incr and num < prev:
                cur += 1
            elif num == prev:
                cur = 1
            else:
                incr = not incr
                cur = 2
            prev = num
            result = max(result, cur)
        return result
                
            
            
