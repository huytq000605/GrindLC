class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
    
    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u
    
    def knew(self, u):
        return self.find(u) == self.find(0)
    
    def reset(self, u):
        self.p[u] = u

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda m: m[2])
        uf = UF(n)
        uf.union(0, firstPerson)
        
        i = 0
        while i < len(meetings):
            t = meetings[i][2]
            people = []
            while i < len(meetings) and meetings[i][2] == t:
                u, v, _ = meetings[i]
                uf.union(u, v)
                people.append(u)
                people.append(v)
                i += 1
            
            for p in people:
                if not uf.knew(p):
                    uf.reset(p)
        
        result = []
        for u in range(n):
            if uf.knew(u): result.append(u)
        return result
