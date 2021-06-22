from typing import List
import string


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def diffMin(timePoint1: str, timePoint2: str) -> int:
            hour1 = int(timePoint1[0:2])
            min1 = int(timePoint1[3:])
            hour2 = int(timePoint2[0:2])
            min2 = int(timePoint2[3:])
            diff = (hour2 - hour1) * 60 + min2 - min1
            if diff > 720:
                diff = 1440 - diff
            return diff
        timePoints.sort()
        result = 9999
        for i, timePoint in enumerate(timePoints):
            if i == len(timePoints) - 1:
                result = min(result, diffMin(timePoints[0], timePoint))
                break
            result = min(result, diffMin(timePoint, timePoints[i+1]))
        return result
