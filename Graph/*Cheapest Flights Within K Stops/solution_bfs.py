class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, p in flights:
            graph[u].append((v, p))
        result = math.inf
        ds = [math.inf for _ in range(n)]
        ds[src] = 0
        dq = deque([(src, 0)])
        for stop in range(k+2):
            m = len(dq)
            for _ in range(m):
                u, s = dq.popleft()
                if u == dst:
                    result = min(result, s)
                for v, p in graph[u]:
                    if s + p < ds[v]:
                        ds[v] = s + p
                        dq.append((v, s + p))
        if result == math.inf: return -1
        return result
