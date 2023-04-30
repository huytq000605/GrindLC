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
        if u == v: return False
        if self.r[u] < self.r[v]: u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        return True
    
    def clone(self):
        other = UF(0)
        other.p = [*self.p]
        other.r = [*self.r]
        return other
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B, C = [], [], []
        for t, u, v in edges:
            u, v = u-1, v-1
            if t == 1: A.append((u, v))
            elif t == 2: B.append((u, v))
            else: C.append((u, v))
        result = 0
        uf = UF(n)
        for u, v in C:
            if not uf.union(u, v):
                result += 1
        
        ufA = uf.clone()
        for u, v in A:
            if not ufA.union(u, v):
                result += 1
        if ufA.r[ufA.find(0)] != n: return -1 
        
        ufB = uf.clone()
        for u, v in B:
            if not ufB.union(u, v):
                result += 1
        if ufB.r[ufB.find(0)] != n: return -1 
        return result
