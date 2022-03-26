class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        start = [0, 0]
        end = [0, 0]
        player = [0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B":
                    start = [i, j]
                elif grid[i][j] == "T":
                    end = [i, j]
                elif grid[i][j] == "S":
                    player = [i, j]
        
        queue = deque([(start[0], start[1], 0, player[0], player[1])])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        seen.add(queue[0])
        
        # can player go from (r,c) to (dr, dc) with box at (box_r, box_c)
        def can(r, c, dr, dc, box_r, box_c, visited):
            if r == dr and c == dc:
                return True
            visited.add((r, c))
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == "#" or (nr, nc) in visited:
                    continue
                if nr == box_r and nc == box_c:
                    continue
                if can(nr, nc, dr, dc, box_r, box_c, visited):
                    return True
            return False
        
        # valid row, col
        def valid(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "#":
                return False
            return True
        
        while queue:
            box_r, box_c, step, player_r, player_c = queue.popleft()
            for d in dirs:
                next_box_r, next_box_c = box_r + d[0], box_c + d[1]
                next_player_r, next_player_c = box_r - d[0], box_c - d[1]
                if (next_box_r, next_box_c, next_player_r, next_player_c) in seen:
                    continue
                if not (valid(next_box_r, next_box_c) and valid(next_player_r, next_player_c)):
                    continue
                if not can(player_r, player_c, next_player_r, next_player_c, box_r, box_c, set()):
                    continue
                seen.add((next_box_r, next_box_c, next_player_r, next_player_c))
                if next_box_r == end[0] and next_box_c == end[1]:
                    return step + 1
                queue.append((next_box_r, next_box_c, step + 1, next_player_r, next_player_c))
        
        return -1