class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(src):
            ds = [math.inf for _ in range(n)]
            ds[src] = 0
            pq = [(0, src)]
            while pq:
                s, u = heappop(pq)
                if s != ds[u]: continue
                for v, w in graph[u]:
                    if s + w < ds[v]:
                        ds[v] = s + w
                        heappush(pq, (s+w, v))
            return ds
        ds1 = dijkstra(0)
        if ds1[n-1] == math.inf: return [False for _ in range(len(edges))]
        ds2 = dijkstra(n-1)
        result = []
        for u, v, w in edges:
            if ds1[u] + ds2[v] + w == ds1[n-1] or ds1[v] + ds2[u] + w == ds1[n-1]:
                result.append(True)
            else:
                result.append(False)
        return result
                        
