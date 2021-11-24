from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while len(stack) and temperatures[stack[-1]] < temp:
                prevIdx = stack.pop()
                result[prevIdx] = i - prevIdx
            stack.append(i)
        return result