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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key = lambda e: e[2])
        queries = sorted([(query[2], query[0], query[1], i) for i, query in enumerate(queries)])
        result = [False for _ in range(len(queries))]
        i = 0
        uf = UF(n)
        for query in queries:
            limit, u, v, idx = query
            while i < len(edgeList) and edgeList[i][2] < limit:
                a, b, _ = edgeList[i]
                uf.union(a, b)
                i += 1
            if uf.find(u) == uf.find(v):
                result[idx] = True
        return result
