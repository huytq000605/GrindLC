class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
    
    def find(self, u):
        if p != self.p[u]:
            self.p[u] = self.find(p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.p[u], self.p[v]
        if u == v:
            return False
        if self.r[v] > self.r[u]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u
        return True

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        have = [0]
        uf = UF(len(rooms))
        while have:
            u = have.pop()
            for v in rooms[u]:
                if uf.union(0, v):
                    have.append(v)
        if uf.r[0] == len(rooms):
            return True
        return False
