class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        grid = [list(grid[i]) for i in range(m)]
        dirs = [(0,1), (1,0), (-1, 0), (0,-1)]
        uppers = ['A', 'B', 'C', 'D', 'E', 'F']
        lowers = ['a', 'b', 'c', 'd', 'e', 'f']
        keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                elif grid[i][j].isupper():
                    grid[i][j] = uppers.index(grid[i][j])
                    keys += 1
                elif grid[i][j].islower():
                    grid[i][j] = -lowers.index(grid[i][j]) - 1
        
        queue = deque([(start[0], start[1], 0, 0)])
        seen = [[[30*30+1 for k in range(1 << keys)] for j in range(n)] for i in range(m)]
        seen[start[0]][start[1]][0] = 0
        
        while queue:
            r, c, s, mask = queue.popleft()
            if mask == (1 << keys) - 1:
                return s
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == "#" or seen[nr][nc][mask] <= s + 1:
                    continue
                seen[nr][nc][mask] = s + 1
                
                if type(grid[nr][nc]) == int:
                    if grid[nr][nc] < 0:
                        new_mask = mask
                        new_mask |= (1 << (-grid[nr][nc] - 1))
                        queue.append((nr, nc, s + 1, new_mask))
                    else:
                        if (mask >> grid[nr][nc]) & 1:
                            queue.append((nr, nc, s + 1, mask))
                else:
                    queue.append((nr, nc, s + 1, mask))
        return -1