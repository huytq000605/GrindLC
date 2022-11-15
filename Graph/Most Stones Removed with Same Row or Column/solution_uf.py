class UF:
    def __init__(self):
        self.p = dict()
        self.r = defaultdict(lambda: 1)
        
    def find(self, u):
        if u not in self.p:
            self.p[u] = u
            self.r[u] = 1
            
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            if self.r[u] < self.r[v]:
                u, v = v, u
            self.p[v] = u
            self.r[u] += self.r[v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UF()
        plus = 10**4 + 1
        for r, c in stones:
            uf.union(r, c + plus)
        island = {uf.find(u) for u in uf.p.keys()}
        return len(stones) - len(island)
