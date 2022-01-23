class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
        
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p == y_p:
            return False
        if self.r[x_p] < self.r[y_p]:
            x_p, y_p = y_p, x_p
        self.p[y_p] = x_p
        self.r[x_p] += self.r[y_p]
        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        groups = n
        
        def similar(s1, s2):
            n = len(s1)
            diff = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2
        
        for i in range(n):
            for j in range(i):
                if similar(strs[i], strs[j]) and uf.union(i, j):
                    groups -= 1

        return groups