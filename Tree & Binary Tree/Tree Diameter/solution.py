class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = 0
        def dfs(u, p, depth):
            nonlocal result
            max_depth = 0
            for v in graph[u]:
                if v == p: continue
                v_depth = dfs(v, u, depth + 1)
                result = max(result, v_depth + max_depth)
                max_depth = max(max_depth, v_depth)
            return max_depth + 1
        dfs(0, -1, 0)
        return result
