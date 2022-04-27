class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
        self.m = [set([i]) for i in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.r[u] < self.r[v]:
            u,v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        self.m[u].update(self.m[v])

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UF(n)
        for u, v in pairs:
            uf.union(u, v)
        arr = [c for c in s]
        for i in range(n):
            if i == uf.find(i):
                characters = sorted([s[j] for j in uf.m[i]])
                idx = 0
                for j in sorted(uf.m[i]):
                    arr[j] = characters[idx]
                    idx += 1
        return "".join(arr)
