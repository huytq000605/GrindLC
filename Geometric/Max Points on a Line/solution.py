class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = min(2, len(points))
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                point1 = points[i]
                point2 = points[j]
                sameLine = 2
                vt = (point1[0] - point2[0], point1[1] - point2[1]) # vector
                nvt = (vt[1], -vt[0]) # n vector
                c = -(nvt[0] * point1[0] + nvt[1] * point1[1]) # ax + by + c = 0 with a is nx and b is ny
                for k in range(j + 1, n):
                    point3 = points[k]
                    if nvt[0] * point3[0] + nvt[1] * point3[1] + c == 0:
                        sameLine += 1
                        result = max(result, sameLine)
        return result