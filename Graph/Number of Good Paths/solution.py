class UF:
    def __init__(self, n, vals):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
        self.counter = [Counter({vals[i]: 1}) for i in range(n)]
        
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        for k, c in self.counter[v].items():
            self.counter[u][k] += c

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        edges = sorted([(max(vals[u], vals[v]), u, v) for u, v in edges])
        uf = UF(n, vals)
        result = n
        for val, u, v in edges:
            u, v = uf.find(u), uf.find(v)
            result += uf.counter[u][val] * uf.counter[v][val]
            uf.union(u, v)
        return result
            
            
