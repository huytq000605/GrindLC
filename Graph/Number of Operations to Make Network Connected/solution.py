class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        uf = UF(n)
        result = n - 1
        for u, v in connections:
            if uf.union(u, v):
                result -= 1
        return result
