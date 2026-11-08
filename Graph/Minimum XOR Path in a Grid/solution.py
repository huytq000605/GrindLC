class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[[False for _ in range(1024)] for _ in range(n)] for _ in range(m)]
        dq = deque([(grid[0][0], 0, 0)])
        result = math.inf
        while dq:
            k = len(dq)
            for _ in range(k):
                v, r, c = dq.popleft()
                seen[r][c][v] = True
                if r == m-1 and c == n-1:
                    result = min(result, v)
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if nr >= m or nc >= n: continue
                    nv = v ^ grid[nr][nc]
                    if seen[nr][nc][nv]: continue
                    seen[nr][nc][nv] = True
                    dq.append((v ^ grid[nr][nc], nr, nc))
        return result
