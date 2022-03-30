class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 0, 1, 0)])
        seen = set()
        
        def valid(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == 1:
                return False
            return True
        
        def can_rotate(r, c, rotate):
            nr, nc = r + rotate[0], c + rotate[1]
            if nr >= n or nc >= n or grid[nr][nc] == 0:
                return True
            return False
        
        horizontal = [(0, 1, 0, 1), (1, 0, 1, 0), (0, 0, 1, -1)]
        vertical = [(0, 1, 0, 1), (1, 0, 1, 0), (0, 0, -1, 1)]
        
        while queue:
            r1, c1, r2, c2, steps = queue.popleft()
            if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                return steps
            
            if r1 == r2:
                dirs = horizontal
                rotate = (1, 0)
            else:
                dirs = vertical
                rotate = (0, 1)
                
            for i, d in enumerate(dirs):
                nr1, nc1, nr2, nc2 = r1 + d[0], c1 + d[1], r2 + d[2], c2 + d[3]
                if i == 2 and not(can_rotate(r1, c1, rotate) and can_rotate(r2, c2, rotate)):
                    continue
                if valid(nr1, nc1) and valid(nr2, nc2) and (nr1, nc1, nr2, nc2) not in seen:
                    seen.add((nr1, nc1, nr2, nc2))
                    queue.append((nr1, nc1, nr2, nc2, steps + 1))
        
        return -1