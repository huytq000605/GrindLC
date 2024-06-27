class UF:
    def __init__(self, n):
        self.p = [[(r, c) for c in range(n)] for r in range(n)]
        self.r = [[1 for c in range(n)] for r in range(n)]

    def find(self, rc):
        r, c = rc
        if self.p[r][c] != (r, c):
            self.p[r][c] = self.find(self.p[r][c])
        return self.p[r][c]
    
    def union(self, rc1, rc2):
        rc1, rc2 = self.find(rc1), self.find(rc2)
        if rc1 == rc2: return
        r1, c1 = rc1
        r2, c2 = rc2
        if self.r[r1][c1] < self.r[r2][c2]:
            r1, r2 = r2, r1
            c1, c2 = c2, c1
        self.r[r1][c1] += self.r[r2][c2]
        self.p[r2][c2] = (r1, c1)
    
    def rank(self, rc):
        r, c = rc
        return self.r[r][c]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UF(n)
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    for dr, dc in ds:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
                        if grid[nr][nc]: uf.union((r, c), (nr, nc))
                    result = max(result, uf.rank(uf.find((r, c))))
                        
        for r in range(n):
            for c in range(n):
                if grid[r][c]: continue
                seen = set()
                cur = 1
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
                    if grid[nr][nc] == 0: continue
                    island = uf.find((nr, nc))
                    if island not in seen:
                        seen.add(island)
                        cur += uf.rank(island)
                result = max(result, cur)
        return result
