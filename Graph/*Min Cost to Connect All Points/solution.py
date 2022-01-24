class Solution:
    class UnionFind:
        def __init__(self, n):
            self.p = [i for i in range(n)]
            self.r = [1 for i in range(n)]
        
        def find(self, x):
            if x != self.p[x]:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        
        def union(self, x, y):
            x_p, y_p = self.find(x), self.find(y)
            if x_p == y_p:
                return 0
            if self.r[x_p] < self.r[y_p]:
                x_p, y_p = y_p, x_p
            self.p[y_p] = x_p
            self.r[x_p] += self.r[y_p]
            return self.r[x_p]
            
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        distances = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heappush(distances, (distace, i, j))
        result = 0
        uf = self.UnionFind(n)
        while True:
            d, u, v = heappop(distances)
            value = uf.union(u, v)
            if value != 0:
                result += d
            if value == n:
                return result
        n
