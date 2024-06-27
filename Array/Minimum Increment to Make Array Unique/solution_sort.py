class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        result = 0
        for num in nums:
            if num <= prev:
                result += prev + 1 - num
                num = prev + 1
            prev = num
            
        return result
