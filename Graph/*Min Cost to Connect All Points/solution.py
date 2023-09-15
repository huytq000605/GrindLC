class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
    
    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return 0
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u
        return self.r[u]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UF(n)
        pq = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heappush(pq, (distance, i, j))
        result = 0
        while pq:
            d, u, v = heappop(pq)
            val = uf.union(u, v)
            if val != 0: result += d
            if val == n: return result
        return result
