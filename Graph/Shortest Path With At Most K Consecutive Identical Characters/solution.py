class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        pq = [(0, 0, 1)]
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        ds = [[math.inf for _ in range(k+1)] for _ in range(n)]
        ds[0][1] = 0
        while pq:
            s, u, c = heappop(pq)
            if u == n-1:
                return s
            for v, w in graph[u]:
                nc = 1 if labels[u] != labels[v] else c + 1
                if nc > k: continue
                if s + w < ds[v][nc]:
                    ds[v][nc] = s + w
                    heappush(pq, (s+w,v, nc))
        return -1
