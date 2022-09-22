class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                lowest = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    result += (i - stack[-1] - 1) * (min(h, left) - lowest)
            stack.append(i)
        return result
