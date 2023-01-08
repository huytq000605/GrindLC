class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 1
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                vt = (x2 - x1, y2 - y1)
                nvt = (vt[1], -vt[0])
                # equation: ax + by + c = 0
                # with (a,b) = nvt
                c = -nvt[0]*x1 - nvt[1] * y1
                sameLine = 2
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if nvt[0]*x3 + nvt[1]*y3 + c == 0:
                        sameLine += 1
                result = max(result, sameLine)
        return result
