class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dq = deque()
        distance = [[math.inf for j in range(n)] for i in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    dq.append((r, c, 0))
        if len(dq) == 0 or len(dq) == n*n: return -1
        
        result = 0
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        while dq:
            r, c, s = dq.popleft()
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
                if s + 1 < distance[nr][nc]:
                    distance[nr][nc] = s + 1
                    result = max(result, s + 1)
                    dq.append((nr, nc, s+1))
        return result
