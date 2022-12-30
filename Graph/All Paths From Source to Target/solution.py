class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        result = []
        n = len(graph)
        def dfs(u):
            nonlocal path, result
            for v in graph[u]:
                if v == n-1:
                    result.append([*path, v])
                    continue
                path.append(v)
                dfs(v)
                path.pop()
        dfs(0)
        return result
