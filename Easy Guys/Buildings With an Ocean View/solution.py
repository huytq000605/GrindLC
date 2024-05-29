class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        for i in range(len(heights) - 1, -1, -1):
            if not result or heights[i] > heights[result[-1]]:
                result.append(i)
        return result[::-1]
