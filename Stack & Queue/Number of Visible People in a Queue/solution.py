class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(heights))]
        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                result[stack.pop()] += 1
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        return result
