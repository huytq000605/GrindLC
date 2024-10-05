class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        ds = [(0,1), (1,0), (-1,0), (0,-1)]

        def valid(day):
            seen = set()
            for i in range(min(day, len(cells))):
                r, c = cells[i]
                seen.add((r-1, c-1))

            dq = deque()
            for c in range(n):
                if (0, c) not in seen:
                    dq.append((0, c))
                    seen.add((0, c))

            while dq:
                for _ in range(len(dq)):
                    r, c = dq.popleft()
                    if r == m-1:
                        return True
                    for dr, dc in ds:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                        if (nr, nc) in seen: continue
                        seen.add((nr, nc))
                        dq.append((nr, nc))
            return False

        start = 0
        end = m*n
        while start < end:
            mid = start + math.ceil((end - start + 1) // 2)
            if valid(mid):
                start = mid
            else:
                end = mid-1
        return start
            
