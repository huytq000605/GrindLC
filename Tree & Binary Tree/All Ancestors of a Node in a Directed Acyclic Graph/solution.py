class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[v].append(u)
        
        seen = [False for i in range(n)]
        ans = [set() for i in range(n)]
        
        def dfs(u):
            if seen[u]:
                return ans[u]
            childs = set()
            seen[u] = True
            for v in graph[u]:
                childs.add(v)
                for child in dfs(v):
                    childs.add(child)
            ans[u] = childs
            return childs
        
        for i in range(n):
            if seen[i] == False:
                dfs(i)
        
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return ans