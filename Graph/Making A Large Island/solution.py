class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UF(m*n)
        dirs = [(0,1), (1,0), (-1, 0), (0, -1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 0:
                        continue
                    uf.union(r*m + c, nr*m + nc)
                    
        result = max(uf.r)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                island = 1
                seen = set()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 0:
                        continue
                    group = uf.find(nr*m + nc)
                    if group in seen:
                        continue
                    seen.add(group)
                    island += uf.r[uf.find(nr*m + nc)]
                result = max(result, island)
        return result