class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        result = set(map(tuple, map(sorted, connections)))

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        rank = [(-2) for i in range(n)]
        
        def dfs(u, depth):
            nonlocal rank
            if rank[u] >= 0:
                return rank[u]
            rank[u] = depth
            min_depth = depth
            for v in graph[u]:
                if depth == rank[v] + 1:
                    continue
                back_depth = dfs(v, depth + 1)
                if back_depth <= depth:
                    result.discard(tuple(sorted([u, v])))
                min_depth = min(min_depth, back_depth)
            return min_depth
        
        dfs(0, 0)
        return result