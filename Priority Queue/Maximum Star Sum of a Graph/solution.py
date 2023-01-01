class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        conn = [[] for i in range(n)]
        for u, v in edges:   
            heappush(conn[u], vals[v])
            if len(conn[u]) > k:
                heappop(conn[u])
            
            u, v = v, u
            heappush(conn[u], vals[v])
            if len(conn[u]) > k:
                heappop(conn[u])
        
        for pq in conn:
            while len(pq) > 1 and pq[0] < 0:
                heappop(pq)
        result = max(vals)
        result = max(result, max(sum(pq) + vals[i] for i, pq in enumerate(conn)) )
        return result
