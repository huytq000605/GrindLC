class UnionFind:
    def __init__(self, bans, n):
        self.bans = bans
        self.people = [set([i]) for i in range(n)]
        self.parent = [i for i in range(n)]
        self.r = [1 for i in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p == y_p:
            return True
        if self.r[y_p] > self.r[x_p]:
            x_p, y_p = y_p, x_p
            
        for person in self.bans[y_p]:
            if person in self.people[x_p]:
                return False
        
        for person in self.bans[x_p]:
            if person in self.people[y_p]:
                return False
        
        self.r[x_p] += self.r[y_p]
        self.people[x_p].update(self.people[y_p])
        self.bans[x_p].update(self.bans[y_p])
        self.parent[y_p] = x_p
        return True
        

class Solution:
    def friendRequests(self, n: int, bans: List[List[int]], requests: List[List[int]]) -> List[bool]:
        banGraph = [set() for i in range(n)]
        for x, y in bans:
            banGraph[x].add(y)
            banGraph[y].add(x)
        uf = UnionFind(banGraph, n)
        result = []
        for x,y in requests:
            result.append(uf.union(x, y))
        return result
            