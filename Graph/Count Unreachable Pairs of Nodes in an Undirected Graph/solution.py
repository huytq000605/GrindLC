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
        if u == v: return
        if self.p[u] < self.p[v]: u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u, v in edges:
            uf.union(u, v)
        result = 0
        for u in range(n):
            if uf.find(u) == u:
                result += (n - uf.r[u]) * uf.r[u]
                n -= uf.r[u]
        return result
