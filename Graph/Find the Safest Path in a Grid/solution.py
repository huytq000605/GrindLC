class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ds = [(0,1), (1,0), (0,-1), (-1,0)]
        n = len(grid)
        
        distance = [[math.inf for _ in range(n)] for _ in range(n)]
        thiefs = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    thiefs.append((r, c, 0))
                    distance[r][c] = 0
        
        
        while thiefs:
            r, c, d = thiefs.popleft()
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if distance[nr][nc] == math.inf:
                    distance[nr][nc] = d + 1
                    thiefs.append((nr, nc, d+1))
        
        pq = [(-distance[0][0], 0, 0)]
        
        seen = [[0 for _ in range(n)] for _ in range(n)]
        seen[0][0] = distance[0][0]
            
        while pq:
            d, r, c = heappop(pq)
            if r == n-1 and c == n-1:
                return -d
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if min(-d, distance[nr][nc]) <= seen[nr][nc]:
                    continue
                seen[nr][nc] = min(-d, distance[nr][nc])
                heappush(pq, (-seen[nr][nc], nr, nc))
            
        return 0
