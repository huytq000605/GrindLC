class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        ds = [(0,1), (1, 0), (0, -1), (-1, 0)]
        s = set()
        cleaned = 0
        r, c, di = 0, 0, 0
        while True:
            if (r, c, di) in s: break
            cleaned += room[r][c] == 0
            room[r][c] = -1
            s.add((r, c, di))
            dr, dc = ds[di]
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= m or nc >= n or room[nr][nc] == 1:
                di = (di + 1) % len(ds)
            else:
                r, c = nr, nc
        return cleaned
            
