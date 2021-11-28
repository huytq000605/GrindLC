class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        def dfs(node):
            if node == len(graph) - 1:
                result.append([*path])
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(nextNode)
                path.pop()
        path.append(0)
        dfs(0)
        return result