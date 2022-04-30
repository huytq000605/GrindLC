class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1] * n
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        
        if x_p != y_p:
            if self.r[x_p] < self.r[y_p]:
                x_p, y_p = y_p, x_p
            self.p[y_p] = x_p
            self.r[x_p] += self.r[y_p]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])
        result = [0 for i in range(len(hits))]
        uf = UnionFind(m * n + 1)
        
        def union_around(r, c):
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    uf.union(r*n + c + 1, nr*n+nc+1)
        
        for r, c in hits:
            grid[r][c] -= 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    union_around(r, c)
                    if r == 0:
                        uf.union(0, c + 1)

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            grid[r][c] += 1
            if grid[r][c] == 1:
                before = uf.r[uf.find(0)]
                if r == 0:
                    uf.union(0, c + 1)
                union_around(r, c)
                after = uf.r[uf.find(0)]
                result[i] = max(after - before - 1, 0)
                    
        return result