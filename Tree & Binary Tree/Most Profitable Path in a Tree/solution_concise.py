class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u, p, da):
            db = 0 if u == bob else n
            res = -math.inf
            for v in graph[u]:
                if v == p: continue
                cost, ndb = dfs(v, u, da + 1)
                db = min(db, ndb)
                res = max(res, cost)
            if res == -math.inf:
                res = 0
            if da == db: res += amount[u] // 2
            if da < db: res += amount[u]
            return res, db+1
                
        return dfs(0, -1, 0)[0]
                    
