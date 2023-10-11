class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        pq = [(0, start[0], start[1])]
        ds = [(0,1), (1,0), (-1, 0), (0,-1)]
        ss = [[math.inf for _ in range(n)] for _ in range(m)]
        ss[start[0]][start[1]] = 0
        while pq:
            s, r, c = heappop(pq)
            if r == destination[0] and c == destination[1]:
                return s
            for dr, dc in ds:
                ns, nr, nc = s, r, c
                while True:
                    nr, nc = nr + dr, nc + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or maze[nr][nc] == 1:
                        nr, nc = nr - dr, nc - dc
                        break
                    ns += 1
                if ss[nr][nc] > ns:
                    heappush(pq, (ns, nr, nc))
                    ss[nr][nc] = ns
        return -1
            
