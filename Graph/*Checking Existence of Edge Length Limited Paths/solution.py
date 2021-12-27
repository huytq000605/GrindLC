class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p == y_p:
            return
        if self.r[x_p] < self.r[y_p]:
            x_p, y_p = y_p, x_p
        self.r[x_p] += self.r[y_p]
        self.p[y_p] = x_p

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key = lambda query: query[2])
        edgeList.sort(key = lambda edge: edge[2])
        
        uf = UnionFind(n)
        
        
        idx = 0
        result = [False] * len(queries)
        for query in queries:
            u, v, limit, i = query
            while idx < len(edgeList) nd edgeList[idx][2] < limit:
                uf.union(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            if uf.find(u) == uf.find(v):
                result[i] = True
        
        return result
