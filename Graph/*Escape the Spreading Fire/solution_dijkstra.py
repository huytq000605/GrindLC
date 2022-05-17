class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        fire_grid = [[10**9*2+1 for j in range(n)] for i in range(m)]
        dirs = [(0,1), (1,0), (-1, 0), (0, -1)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire_grid[i][j] = 0
                    dq.append((i, j, 0))
                elif grid[i][j] == 2:
                    fire_grid[i][j] = 0
        while dq:
            r, c, s = dq.popleft()
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or s + 1 >= fire_grid[nr][nc]:
                    continue
                fire_grid[nr][nc] = s + 1
                dq.append((nr, nc, s + 1))
                
        if fire_grid[0][0] == 0:
            return -1

        pq = [(fire_grid[0][0] - 1, 0, 0, 0, )]
        reach_destination = False
        result = 0
        seen = [[-1 for j in range(n)] for i in range(m)]
        seen[0][0] = fire_grid[0][0] - 1
        while pq:
            can_wait, r, c, t = heappop(pq)

            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr == m - 1 and nc == n - 1 and t + 1 <= fire_grid[nr][nc]:
                    reach_destination = True
                    result = max(result, min(can_wait, fire_grid[nr][nc] - t - 1))
                    continue
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n or t + 1 >= fire_grid[nr][nc]:
                    continue
                # t + 1 + x == fire_grid[nr][nc] - 1      
                new_can_wait = min(can_wait, fire_grid[nr][nc] - t - 1 - 1)
                if new_can_wait > seen[nr][nc]:
                    seen[nr][nc] = new_can_wait
                    heappush(pq, (new_can_wait, nr, nc, t + 1))
                
        if not reach_destination:
            return -1
        if result > 10**9:
            return 10**9
        return result