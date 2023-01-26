class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = [(0, src, 0)]
        graph = [[] for _ in range(n)]
        for u, v, p in flights:
            graph[u].append((v, p))
        stops = [n for _ in range(n)]
        stops[src] = 0
        while pq:
            c, u, s = heappop(pq)
            if s > stops[u]: continue
            stops[u] = s
            if u == dst:
                return c
            if s + 1 >= k+2:
                continue
            for v, p in graph[u]:
                if s + 1 >= stops[v]: continue
                heappush(pq, (c+p, v, s+1))
        return -1
