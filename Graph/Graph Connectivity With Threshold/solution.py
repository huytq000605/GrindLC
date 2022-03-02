class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[y] = x
        self.rank[x] += self.rank[y]
        

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UF(n + 1)
        result = []
        for i in range(threshold + 1, n + 1):
            multiply = 2
            while i * multiply <= n:
                uf.union(i, i * multiply)
                multiply += 1
        
        for u, v in queries:
            if uf.find(u) == uf.find(v):
                result.append(True)
            else:
                result.append(False)
        
        return result