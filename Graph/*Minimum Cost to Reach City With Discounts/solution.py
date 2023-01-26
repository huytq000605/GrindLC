class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, p in highways:
            graph[u].append((v, p))
            graph[v].append((u, p))
        pq = [(0, 0, discounts)]
        discount_track = [-1 for _ in range(n)]
        while pq:
            s, u, discount = heappop(pq)
            if u == n-1:
                return s
            if discount <= discount_track[u]:
                continue
            discount_track[u] = discount
            for v, p in graph[u]:
                if discount and discount >= discount_track[v]:
                    heappush(pq, (s + p // 2, v, discount - 1))
                heappush(pq, (s + p, v, discount))
        return -1
                    
                
