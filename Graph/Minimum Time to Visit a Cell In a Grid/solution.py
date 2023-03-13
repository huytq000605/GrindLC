class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        pq = [(0, 0, 0)]
        m, n = len(grid), len(grid[0])
        d = [[math.inf for j in range(n)] for i in range(m)]
        d[0][0] = 0
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        while pq:
            s, r, c = heappop(pq)
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                if s+1 >= grid[nr][nc]:
                    if s+1 < d[nr][nc]:
                        d[nr][nc] = s+1
                        heappush(pq, (s+1, nr, nc))
                else:
                    # move to previous and move back to where we are standing until meet grid[nr][nc]
                    if (s+1) % 2 == grid[nr][nc] % 2:
                        if grid[nr][nc] < d[nr][nc]:
                            d[nr][nc] = grid[nr][nc]
                            heappush(pq, (grid[nr][nc], nr, nc))
                    else:
                        if grid[nr][nc] + 1 < d[nr][nc]:
                            d[nr][nc] = grid[nr][nc] + 1
                            heappush(pq, (grid[nr][nc] + 1, nr, nc))
        return d[m-1][n-1]
            
