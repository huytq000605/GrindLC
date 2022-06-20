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
        
        def can_go(start_time):
            seen = set()
            q = deque([(0, 0, start_time)])
            while q:
                r, c, t = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr == m - 1 and nc == n - 1 and t + 1 <= fire_grid[nr][nc]:
                        return True
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or t + 1 >= fire_grid[nr][nc] or (nr,nc) in seen:
                        continue
                    seen.add((nr, nc))
                    q.append((nr, nc, t + 1))
            return False
        
        if not can_go(0):
            return -1
        start = 0
        end = 10**9
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if can_go(mid):
                start = mid
            else:
                end = mid - 1
        return start