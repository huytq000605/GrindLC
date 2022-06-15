class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dq = deque([(0, 0, 0)])
        m, n = len(grid), len(grid[0])
        grid[0][0] = 2
        
        while dq:
            r, c, s = dq.popleft()
            if r == m-1 and c == n-1:
                return s
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 2:
                    continue
                if grid[nr][nc] == 1:
                    dq.append((nr, nc, s + 1))
                else:
                    dq.appendleft((nr, nc, s))
                grid[nr][nc] = 2
        return -1