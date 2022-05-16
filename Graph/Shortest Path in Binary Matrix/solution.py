class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        dirs = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1),(1, -1), (-1,1)]
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1
        q = deque([(0, 0, 1)])
        while q:
            r, c, s = q.popleft()
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 1:
                    continue
                if nr == m-1 and nc == n-1:
                    return s+1
                grid[nr][nc] = 1
                q.append((nr, nc, s + 1))
                
        return -1