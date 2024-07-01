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
        if self.r[u] < self.r[v]: u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UF(n)
        for t, u, v in sorted(logs):
            uf.union(u, v)
            if uf.r[uf.p[u]] == n: return t
        return -1
