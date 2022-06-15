class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        pq = [(0, 0, 0)]
        m, n = len(grid), len(grid[0])
        dij = [[m*n for j in range(n)] for i in range(m)]
        dij[0][0] = 0
        while pq:
            removed, r, c = heappop(pq)
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                plus = 0
                if grid[nr][nc] == 1:
                    plus = 1
                if nr == m - 1 and nc == n - 1:
                    return removed + plus
                if removed + plus < dij[nr][nc]:
                    dij[nr][nc] = removed + plus
                    heappush(pq, (removed+plus, nr, nc))
        return -1