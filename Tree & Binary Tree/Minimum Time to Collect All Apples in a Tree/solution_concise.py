class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(u, parent):
            total_steps = 0
            for v in graph[u]:
                if v == parent: continue
                steps = dfs(v, u)
                if steps > 0 or hasApple[v]:
                    total_steps += steps + 2
            return total_steps
        
        result = dfs(0, -1)
        return result
            
