class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[0 for j in range(n)] for i in range(m)]
        seen_len = 1
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        obstacles = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == -1:
                    obstacles += 1
                if grid[r][c] == 1:
                    start = (r,c)
                if grid[r][c] == 2:
                    end = (r,c)
        
        seen[start[0]][start[1]] = 1
        def dfs(r, c):
            nonlocal seen_len, seen, ds, obstacles
            if (r, c) == end:
                if seen_len == m * n - obstacles:
                    return 1
                return 0
            result = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == -1:
                    continue
                if seen[nr][nc]:
                    continue
                seen[nr][nc] = 1
                seen_len += 1
                result += dfs(nr, nc)
                seen[nr][nc] = 0
                seen_len -= 1
            return result
        return dfs(start[0], start[1])
        
