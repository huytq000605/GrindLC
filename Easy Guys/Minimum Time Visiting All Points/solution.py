class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            result += min(dx, dy) + abs(dx -dy)
        return result
