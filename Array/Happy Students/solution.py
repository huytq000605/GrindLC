class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        have_zero = False
        for i, num in enumerate(nums):
            if num == 0:
                have_zero = True
            selected = i + 1
            if selected > num and (i == n-1 or selected < nums[i+1]):
                result += 1
        # Not choosing any students
        if not have_zero:
            result += 1
        return result
            
            
