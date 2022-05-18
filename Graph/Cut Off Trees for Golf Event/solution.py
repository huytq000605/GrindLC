class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def shorest_path(sr, sc, dr, dc):
            nonlocal dirs
            dq = deque([(sr, sc, 0)])
            seen = set()
            while dq:
                r, c, s = dq.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or forest[nr][nc] == 0 or (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    if nr == dr and nc == dc:
                        return s+1
                    dq.append((nr, nc, s + 1))
            return -1
        
        pq = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heappush(pq, (forest[i][j], i, j))
        
        r, c = 0, 0
        result = 0
        while pq:
            height, nr, nc = heappop(pq)
            if r == nr and c == nc:
                continue
            steps = shorest_path(r, c, nr, nc)
            if steps == -1:
                return -1
            r, c = nr, nc
            result += steps
        return result
            