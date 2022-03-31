class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        result = []
        idx = 0
        idxs = [-1 for i in range(n)]
        lowest = [-1 for i in range(n)]
        
        def dfs(u, parent):
            nonlocal result, idxs, idx
            idxs[u] = idx
            lowest[u] = idx
            idx += 1
            current = lowest[u]
            for v in graph[u]:
                if v == parent:
                    continue
                if idxs[v] == -1:
                    lowest_reach = dfs(v, u)
                lowest[u] = min(lowest[u], lowest[v])
                if current < lowest[v]:
                    result.append((u, v))
            return lowest[u]
        dfs(0, -1)
        return result