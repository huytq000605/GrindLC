class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ds = [(0,1), (1,0), (0,-1), (-1,0)]
        m, n = len(grid), len(grid[0])
        start = (-1, -1)
        mapping = dict()
        mask_idx = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "@":
                    start = (r, c)
                elif grid[r][c].isupper():
                    mapping[grid[r][c]] = mask_idx
                    mapping[grid[r][c].lower()] = mask_idx
                    mask_idx += 1

        mask_count = mask_idx
        seen = [[[False for k in range(1 << mask_count)] for j in range(n)] for i in range(m)]
        dq = deque([(start[0], start[1], 0, 0)])
        while dq:
            r, c, mask, s = dq.popleft()
            if mask == (1 << mask_count) - 1:
                return s
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if grid[nr][nc] == "#":
                    continue
                if grid[nr][nc].isupper():
                    mask_idx = mapping[grid[nr][nc]]
                    if (mask >> mask_idx) & 1 == 0: continue
                next_mask = mask
                if grid[nr][nc].islower():
                    mask_idx = mapping[grid[nr][nc]]
                    next_mask |= (1 << mask_idx)
                if seen[nr][nc][next_mask]:
                    continue
                seen[nr][nc][next_mask] = True
                dq.append((nr, nc, next_mask, s+1))
        return -1
