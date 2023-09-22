class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        next_smaller = [n for _ in range(n)]
        
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        result = 0
        for i in range(n):
            result += next_smaller[i] - i
        return result
