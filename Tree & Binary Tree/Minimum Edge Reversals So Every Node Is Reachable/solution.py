class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        
        root = 0
        for u in range(n):
            if len(graph[u]) == 1:
                root = u
                break
        
        @cache
        def dfs(u, p):
            if p != -1 and len(graph[u]) == 1:
                return 0
            result = 0
            for v, cost in graph[u]:
                if v == p: continue
                result += dfs(v, u) + cost
            return result
        
        result = [0 for _ in range(n)]
        
        def calculate(u, p, before):
            nonlocal result
            if len(graph[u]) == 1 and p != -1:
                result[u] = before
                return
            result[u] = before + dfs(u, p)
            for v, cost in graph[u]:
                if v == p: continue
                    
                # u down to v
                # next_before = original_before + from_u_to_all - from_v_to_all + cost_from_v_to_u - cost_from_u_to_v
                cost_from_v_to_u = 0
                for z, c in graph[v]:
                    if z == u:
                        cost_from_v_to_u = c
                
                next_before = before + dfs(u, p) - dfs(v, u) + cost_from_v_to_u - cost
                calculate(v, u, next_before)
        calculate(root, -1, 0)
        return result
