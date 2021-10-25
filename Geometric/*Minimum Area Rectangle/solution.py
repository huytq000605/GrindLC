from typing import List
import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointMap = {}
        for point in points:
            pointMap[f"{point[0]}-{point[1]}"] = True
        minArea = sys.maxsize
        hasRectangle = False
        
        for point1 in points:
            for point2 in points:
                if point2[0] == point1[0] or point2[1] == point1[1]:
                    continue
                x1 = point1[0]
                y1 = point1[1]
                x2 = point2[0]
                y2 = point2[1]
                if pointMap.get(f"{x1}-{y2}") != None and pointMap.get(f"{x2}-{y1}") != None:
                    area = abs(x1-x2) * abs(y1-y2)
                    minArea = min(minArea, area)
                    hasRectangle = True
        
        if hasRectangle == False:
            return 0
        return minArea