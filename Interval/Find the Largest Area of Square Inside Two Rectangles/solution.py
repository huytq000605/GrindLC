class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                r1x1, r1y1 = bottomLeft[i]
                r1x2, r1y2 = topRight[i]
                
                r2x1, r2y1 = bottomLeft[j]
                r2x2, r2y2 = topRight[j]
                
                x = min(r1x2, r2x2) - max(r1x1, r2x1)
                y = min(r1y2, r2y2) - max(r1y1, r2y1)
                result = max(result, min(x, y))
        return result * result
