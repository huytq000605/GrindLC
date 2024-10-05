class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
        self.cost = [(1<<18) - 1 for _ in range(n)]

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v, c):
        u, v = self.find(u), self.find(v)
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.cost[u] = self.cost[u] & self.cost[v] & c
        if u != v:
            self.p[v] = u
            self.r[u] += self.r[v]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        for u, v, c in edges:
            uf.union(u, v, c)
        
        result = []
        for a, b in query:
            u, v = uf.find(a), uf.find(b)
            if u != v: result.append(-1)
            else: result.append(uf.cost[u])
        return result
