class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        queries = sorted([(query, i) for i, query in enumerate(queries)])
        result = [0 for i in range(len(queries))]
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        points = 0
        seen = set([(0, 0)])
        for query, i in queries:
            while pq:
                if pq[0][0] >= query:
                    break
                points += 1
                v, r, c = heappop(pq)
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    heappush(pq, (grid[nr][nc], nr, nc))
            result[i] = points
        return result
                    
                    
        
