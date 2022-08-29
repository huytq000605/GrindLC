class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        n = len(height)
        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                lowest = height[stack.pop()]
                if stack:
                    result += (i - 1 - stack[-1]) * (min(height[stack[-1]], height[i]) - lowest)
                else:
                    break
            stack.append(i)
        return result
