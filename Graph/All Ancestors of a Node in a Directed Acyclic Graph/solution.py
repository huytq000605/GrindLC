class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)

        result = [[] for _ in range(n)]
        def dfs(u, anc):
            for v in graph[u]:
                if result[v] and result[v][-1] == anc: continue
                result[v].append(anc)
                dfs(v, anc)
        
        for u in range(n):
            dfs(u, u)
        
        return result
            
            
