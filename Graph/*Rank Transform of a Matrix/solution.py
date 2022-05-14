class UnionFind:
    def __init__(self):
        self.p = dict()
        self.r = dict()
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        if x not in self.p:
            self.p[x] = x
            self.r[x] = 1
            
        if y not in self.p:
            self.p[y] = y
            self.r[y] = 1
        
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.r[x] < self.r[y]:
            x, y = y, x
        self.p[y] = x
        self.r[x] += self.r[y]
    
    def groups(self):
        groups = defaultdict(list)
        for i in self.p.keys():
            groups[self.find(i)].append(i)
        return groups.values()
        
        

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        lookup = defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        rank = [0 for i in range(m + n)]
        result = [[0 for j in range(n)] for i in range(m)]
        
        for r in range(m):
            for c in range(n):
                lookup[matrix[r][c]].append((r, c))
        
        for value in sorted(lookup.keys()):
            uf = UnionFind()
            for r, c in lookup[value]:
                uf.union(r, c + m)
            
            groups = uf.groups()
            for group in groups:
                max_rank = max(rank[i] for i in group)
                for i in group:
                    rank[i] = max_rank + 1
            
            for r, c in lookup[value]:
                result[r][c] = rank[r]
                    
            
        return result