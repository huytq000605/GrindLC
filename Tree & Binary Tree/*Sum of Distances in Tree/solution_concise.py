class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        children = [0 for i in range(n)]

        def dfs(u, parent):
            s = 0
            for v in graph[u]:
                if v == parent:
                    continue
                s += dfs(v, u)
                children[u] += children[v] + 1
            return s + children[u]

        result = [0 for i in range(n)]
        result[0] = dfs(0, -1)
        
        def cal(u, parent):
            if u != 0:
                result[u] = result[parent] - 1 - children[u] + (n - children[u] - 1)
            for v in graph[u]:
                if v == parent:
                    continue
                cal(v, u)

        cal(0, -1)
        return result
