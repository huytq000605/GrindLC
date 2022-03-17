class UF:
    def __init__(self, size):
        self.p = [i for i in range(size)]
        self.r = [1 for i in range(size)]
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2 = UF(n+1), UF(n+1)
        edges1 = []
        edges2 = []
        used = 0
        for t, u, v in edges:
            if t == 3:
                use = False
                use = uf1.union(u, v) or use
                use = uf2.union(u, v) or use
                if use: 
                    used += 1
            elif t == 1:
                edges1.append((u, v))
            else:
                edges2.appnd((u, v))
        for u, v in edges1:
            if uf1.union(u, v):
                used += 1
        for u, v in edges2:
            if uf2.union(u, v):
                used += 1
        if max(uf1.r) != n or max(uf2.r) != n:
            return -1
        
        return len(edges) - used
