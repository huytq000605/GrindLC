class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n+1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        min_path = math.inf
        have_path = False
        seen = set()
        def dfs(u):
            nonlocal min_path, have_path, seen
            if u == n:
                have_path = True
            for v, d in graph[u]:
                min_path = min(min_path, d)
                if v in seen:
                    continue
                seen.add(v)
                dfs(v)
        
        dfs(1)
        if not have_path:
            return -1
        return min_path
                        
                                
