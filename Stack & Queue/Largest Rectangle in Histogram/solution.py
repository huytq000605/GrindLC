class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        heights.append(0)
        n = len(heights)
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if len(stack) > 0:
                    w = i - stack[-1] - 1
                else:
                    w = i - (-1) - 1
                result = max(result, w * h)
            stack.append(i)
        return result
