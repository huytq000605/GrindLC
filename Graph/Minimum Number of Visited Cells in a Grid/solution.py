class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        dq = deque([(0, 0)])
        s = 1
        m, n = len(grid), len(grid[0])
        max_r = [0 for _ in range(n)]
        max_c = [0 for _ in range(m)]
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                if r == m-1 and c == n-1:
                    return s
                for nr in range(max(r+1, max_r[c] + 1), min(m, r + grid[r][c] + 1)):
                    max_r[c] = nr
                    dq.append((nr, c))
                for nc in range(max(c+1, max_c[r] + 1), min(n, c + grid[r][c] + 1)):
                    max_c[r] = nc
                    dq.append((r, nc))
            s += 1
        return -1
        
