class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = -math.inf
        result = 0
        for start, end in points:
            if prev < start:
                result += 1
                prev = end
            prev = min(prev, end)
        return result
