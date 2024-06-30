class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ind = [0 for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
            ind[u] += 1

        result = [set() for _ in range(n)]
        def dfs(u):
            nonlocal result
            if result[u]: return result[u]
            for v in graph[u]:
                result[u].add(v)
                for z in dfs(v):
                    result[u].add(z)
            return result[u]

        for u in range(n):
            if ind[u] == 0:
                dfs(u)
        
        return [sorted(a) for a in result]
            
