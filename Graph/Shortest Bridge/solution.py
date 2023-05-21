class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        try:
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        stack = [(r, c)]
                        grid[r][c] = -1
                        while stack:
                            r, c = stack.pop()
                            q.append((r, c))
                            for dr, dc in ds:
                                nr, nc = r + dr, c + dc
                                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                                    continue
                                if grid[nr][nc] != 1: continue
                                grid[nr][nc] = -1
                                stack.append((nr, nc))
                        raise Exception
        except Exception:
            pass
        s = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                    if grid[nr][nc] == 1: return s
                    if grid[nr][nc] == -1: continue
                    grid[nr][nc] = -1
                    q.append((nr, nc))       
            s += 1
        return -1

