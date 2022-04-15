class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[w, u, v, i] for i, [u, v, w] in enumerate(edges)]
        edges.sort()
        
        def kruskal(included, banned):
            uf = UF(n)
            seen = 1
            weight = 0
            
            if included != -1:
                w, u, v, i = edges[included]
                uf.union(u, v)
                seen += 1
                weight += w
            
            for idx, edge in enumerate(edges):
                if idx == banned:
                    continue
                w, u, v, i = edge
                if uf.union(u, v):
                    seen += 1
                    weight += w
                    if seen == n:
                        break
            if seen == n:
                return weight
            return math.inf
        
        min_weight = kruskal(-1, -1)
        critical = set()
        pseudo = set()
        
        for i in range(len(edges)):
            if kruskal(-1, i) > min_weight:
                critical.add(edges[i][3])
        
        for i in range(len(edges)):
            if edges[i][3] in critical:
                continue
            if kruskal(i, -1) == min_weight:
                pseudo.add(edges[i][3])
        
        return [critical, pseudo]