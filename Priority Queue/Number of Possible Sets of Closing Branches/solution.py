class Solution:
    def numberOfSets(self, n: int, max_distance: int, roads: List[List[int]]) -> int:
        graph = [[math.inf for _ in range(n)] for _ in range(n)]
        for u, v, w in roads:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)
        
        result = 0
        for mask in range(1 << n):
            valid = True
            for u in range(n):
                if (mask >> u) & 1 == 0: continue
                ds = [math.inf for _ in range(n)]
                ds[u] = 0
                pq = [(0, u)]
                while pq:
                    s, u = heappop(pq)
                    for v in range(n):
                        if v != u and (mask >> v) & 1 and s + graph[u][v] < ds[v]:
                            ds[v] = s + graph[u][v]
                            heappush(pq, (graph[u][v] + s, v))
                
                if any([ds[v] > max_distance for v in range(n) if (mask >> v) & 1 == 1]):
                    valid = False
                    break
            if valid: 
                result += 1
        return result
                    
                
            
