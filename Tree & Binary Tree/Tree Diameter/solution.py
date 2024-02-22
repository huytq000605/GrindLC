class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(u):
            dq = deque([(u, -1, 0)])
            while dq:
                u, p, s = dq.popleft()
                for v in graph[u]:
                    if v == p: continue
                    dq.append((v, u, s+1))
            return u, s
        
        u, _ = bfs(0)
        _, result = bfs(u)
        return result
