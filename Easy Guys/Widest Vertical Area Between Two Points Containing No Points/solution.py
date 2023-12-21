class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        result = 0
        for i in range(n-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            result = max(result, x2 - x1)
        return result
