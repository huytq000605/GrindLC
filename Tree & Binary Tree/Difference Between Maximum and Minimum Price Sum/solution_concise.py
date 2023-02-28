class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        @cache
        def dfs(u, p):
            longest_path = 0
            for v in graph[u]:
                if v == p: continue
                longest_path = max(longest_path, dfs(v, u) + price[v])
            return longest_path
        
        result = 0
        for u in range(n):
            result = max(result, dfs(u, -1))
        return result
                
