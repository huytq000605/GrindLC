class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        idxs = [-1 for _ in range(n)]
        lowest = [-1 for _ in range(n)]
        i = 0
        result = []
        
        def dfs(u, parent):
            nonlocal i, idxs, lowest, result
            idxs[u] = i
            lowest[u] = i
            i += 1
            for v in graph[u]:
                if v == parent: continue
                if idxs[v] == -1:
                    dfs(v, u)
                lowest[u] = min(lowest[u], lowest[v])
                if idxs[u] < lowest[v]:
                    result.append((u, v))
        
        dfs(0, -1)
        return result
            
