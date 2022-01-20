import math

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        
        stack = []
        arr = [math.inf, *nums, math.inf]
        for i, num in enumerate(arr):
            while stack and num > arr[stack[-1]]:
                j = stack.pop()
                prevBigger = stack[-1]
                result += arr[j] * (j - prevBigger) * (i - j)
            stack.append(i)
        stack = []
        arr = [-math.inf, *nums, -math.inf]
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                j = stack.pop()
                prevSmaller = stack[-1]
                result -= arr[j] * (j - prevSmaller) * (i - j)
            stack.append(i)
        
        return result