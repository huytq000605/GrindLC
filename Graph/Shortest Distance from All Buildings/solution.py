
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        visited_houses = [[0 for _ in range(n)] for _ in range(m)]
        distances = [[0 for _ in range(n)] for _ in range(m)]
        houses = 0
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c):
            dq = deque([(r, c)])
            visited = set()
            s = 0
            while dq:
                for _ in range(len(dq)):
                    r, c = dq.popleft()
                    for dr, dc in ds:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr == m or nc == n: continue
                        if grid[nr][nc] != 0: continue
                        if (nr, nc) in visited: continue
                        visited_houses[nr][nc] += 1
                        distances[nr][nc] += s + 1
                        visited.add((nr, nc))
                        dq.append((nr, nc))
                s += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    bfs(r, c)
                    houses += 1
        
        result = math.inf
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and visited_houses[r][c] == houses:
                    result = min(result, distances[r][c])
        return -1 if result == math.inf else result
