class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # yA > yB, xA < xB
        points.sort(key = lambda p: (p[0], -p[1]))
        n = len(points)
        result = 0
        for i, (xA, yA) in enumerate(points):
            mn_y = -math.inf
            for j in range(i+1, n):
                if points[j][1] <= yA and points[j][1] > mn_y:
                    result += 1
                    mn_y = points[j][1]
        return result
                    
            
