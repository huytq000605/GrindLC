class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = [0 for i in range(n)]
        seen[source] = 1
        def dfs(u):
            if u == destination:
                return True
            for v in graph[u]:
                if seen[v]: continue
                seen[v] = 1
                if dfs(v):
                    return True
            return False
        return dfs(source)
