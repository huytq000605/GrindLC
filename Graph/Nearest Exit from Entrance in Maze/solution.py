class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ds = [(0,1), (1,0), (-1,0), (0,-1)]
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        q = deque([(entrance[0], entrance[1], 0)])
        while q:
            r, c, s = q.popleft()
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or maze[nr][nc] == "+":
                    continue
                if nr == 0 or nc == 0 or nr == m-1 or nc == n-1:
                    return s+1
                maze[nr][nc] = "+"
                q.append((nr, nc, s+1))
        return -1
