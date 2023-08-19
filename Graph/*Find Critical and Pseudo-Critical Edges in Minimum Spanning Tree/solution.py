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
        if u == v:
            return False
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u
        return True
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([(u, v, w, i) for i, (u,v,w) in enumerate(edges)], key = lambda e: e[2])
        
        def krusal(included, banned):
            uf = UF(n)
            connected = 1
            MST_val = 0
            if included != -1:
                u, v, w, _ = edges[included]
                connected = 2
                MST_val = w
                uf.union(u, v)
            for idx, (u, v, w, _) in enumerate(edges):
                if idx == banned:
                    continue
                if not uf.union(u, v):
                    continue
                MST_val += w
                connected += 1
                if connected == n:
                    return MST_val
            
            return math.inf
        
        MST_min_val = krusal(-1, -1)
        pseudo_criticals = []
        criticals = []
        
        for i in range(len(edges)):
            if krusal(-1, i) > MST_min_val:
                criticals.append(edges[i][3])
            elif krusal(i, -1) == MST_min_val:
                pseudo_criticals.append(edges[i][3])
        
        return [criticals, pseudo_criticals]
        

