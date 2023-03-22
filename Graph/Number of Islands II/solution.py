class UF:
    def __init__(self, m, n):
        self.p = [[(i, j) for j in range(n)] for i in range(m)]
        self.r = [[1 for j in range(n)] for i in range(m)]
    
    def find(self, r, c):
        if self.p[r][c] != (r, c):
            nr, nc = self.p[r][c]
            self.p[r][c] = self.find(nr, nc)
        return self.p[r][c]
    
    def union(self, r1, c1, r2, c2):
        r1, c1 = self.find(r1, c1)
        r2, c2 = self.find(r2, c2)
        if r1 == r2 and c1 == c2:
            return False
        if self.r[r2][c2] > self.r[r1][c1]:
            r1, r2 = r2, r1
            c1, c2 = c2, c1
        self.r[r1][c1] += self.r[r2][c2]
        self.p[r2][c2] = (r1, c1)
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UF(m, n)
        ds = [(0, 1), (1,0), (-1,0), (0,-1)]
        grid = [[0 for j in range(n)] for i in range(m)]
        islands = 0
        result = []
        for r, c in positions:
            if grid[r][c] == 1:
                result.append(result[-1])
                continue
            grid[r][c] = 1
            islands += 1
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                if grid[nr][nc] == 0: continue
                if uf.union(r, c, nr, nc):
                    islands -= 1
            result.append(islands)
        return result
