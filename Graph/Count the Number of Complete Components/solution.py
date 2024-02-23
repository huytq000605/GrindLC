class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
        self.e = [0 for _ in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: 
            self.e[u] += 1
            return
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        self.e[u] += 1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        result = 0
        for u, v in edges:
            uf.union(u, v)

        for u in range(n):
            if u != uf.find(u): continue
            r = uf.r[u]
            e = uf.e[u]
            if e == r * (r-1) // 2:
                result += 1
        return result
