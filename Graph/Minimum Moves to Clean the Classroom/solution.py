
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        l = 0
        start = (-1, -1)
        mapping = dict()
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                if classroom[r][c] == 'L':
                    mapping[(r, c)] = l
                    l += 1
        dp = [[[-1 for _ in range(1 << l)] for _ in range(n)] for _ in range(m)]
        ds = [(1,0), (-1,0), (0, -1), (0, 1)]
        dq = deque([(start[0], start[1], energy, 0)])
        dp[start[0]][start[1]][0] = energy 
        s = 0
        while dq:
            k = len(dq)
            for _ in range(k):
                r, c, e, mask = dq.popleft()
                if mask == (1 << l) - 1:
                    return s
                if classroom[r][c] == 'R':
                    e = energy
                if e == 0:
                    continue
                
                for dr, dc in ds:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or\
                        classroom[nr][nc] == 'X':
                        continue
                    nmask = mask
                    if classroom[nr][nc] == 'L':
                        nmask |= (1 << mapping[(nr, nc)])
                    if e-1 > dp[nr][nc][nmask]:
                        dp[nr][nc][nmask] = e-1
                        dq.append((nr, nc, e-1, nmask))
            s += 1
        return -1
