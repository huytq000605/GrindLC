class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        def dfs(r, c):
            seen[r][c] = True
            result = grid[r][c]
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                if not grid[nr][nc] or seen[nr][nc]: continue
                result += dfs(nr, nc)
            return result

        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and not seen[r][c]:
                    if dfs(r, c) % k == 0:
                        result += 1
        return result
