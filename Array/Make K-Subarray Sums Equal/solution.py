class UF:
    def __init__(self, n, arr):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
        self.l = [[arr[i]] for i in range(n)]
    
    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.r[u] < self.r[v]: u, v = v,u
        self.r[u] + self.r[v]
        for e in self.l[v]: self.l[u].append(e)
        self.p[v] = u

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        uf = UF(n, arr)
        for i in range(n+k):
            uf.union(i % n, (i + k) % n)
        result = 0
        for u in range(n):
            if uf.find(u) == u:
                # can use quick select to achieve better time complexity
                uf.l[u].sort()
                m = len(uf.l[u])
                median = uf.l[u][m//2]
                for num in uf.l[u]: result += abs(num - median)
        return result
