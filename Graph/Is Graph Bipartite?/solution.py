class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0 for _ in range(n)]
        def dfs(u, c):
            if colors[u]:
                if c != colors[u]: return 0
                return c
            colors[u] = c
            for v in graph[u]:
                if not dfs(v, 3-c):
                    return 0
            return c
        for u in range(n):
            if not colors[u]:
                if not dfs(u, 1): return 0
        return True
