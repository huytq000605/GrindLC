class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        current = [0]
        result = []
        def dfs(node):
            if node == len(graph) - 1:
                result.append([*current])
                return
            for connect in graph[node]:
                current.append(connect)
                dfs(connect)
                current.pop()
        dfs(0)
        return result