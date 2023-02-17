class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        b_steps = [n for _ in range(n)]
        def b(u, s, p):
            if u == 0:
                b_steps[u] = s
                return True
            for v in graph[u]:
                if v == p: continue
                if b(v, s + 1, u):
                    b_steps[u] = s
                    return True
            return False
        b(bob, 0, -1)
        
        def dfs(u, s, p):
            res = -math.inf
            for v in graph[u]:
                if v == p: continue
                cost = dfs(v, s+1, u)
                res = max(res, cost)
                
            if res == -math.inf: res = 0
            if s < b_steps[u]:
                res += amount[u]
            elif s == b_steps[u]:
                res += amount[u] // 2
            return res
        return dfs(0, 0, -1)
                
