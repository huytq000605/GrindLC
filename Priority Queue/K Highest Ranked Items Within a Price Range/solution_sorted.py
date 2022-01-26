class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]
        result = []
        seen = set()
        seen.add((start[0], start[1]))
        queue = deque([(start[0], start[1], 0)])
        if grid[start[0]][start[1]] >= pricing[0] and grid[start[0]][start[1]] <= pricing[1]:
            result.append((0, grid[start[0]][start[1]], start[0], start[1]))
        while queue:
            r, c, s = queue.popleft()
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in seen or grid[nr][nc] == 0:
                    continue
                seen.add((nr, nc))
                queue.append((nr, nc, s + 1))
                if grid[nr][nc] >= pricing[0] and grid[nr][nc] <= pricing[1]:
                    result.append((s + 1, grid[nr][nc], nr, nc))
        result.sort()
        result = list(map(lambda element: (element[2], element[3]), result[:k]))
        return result