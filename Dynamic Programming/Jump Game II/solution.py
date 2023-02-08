class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        r = 0
        j = 0
        while r < n-1:
            nr = 0
            result += 1
            while j <= r:
                nr = max(nr, nums[j] + j)
                j += 1
            r = nr
        return result
        
