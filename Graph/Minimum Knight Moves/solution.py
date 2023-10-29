class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        dq = deque([(0, 0, 0)])
        ds = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        seen = set([(0, 0)])
        while dq:
            r, c, s = dq.popleft()
            if r == x and c == y:
                return s
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr > x + 2 or nc > y + 2 or nr < -2 or nc < -2 or (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                dq.append((nr, nc, s+1))
        return -1
