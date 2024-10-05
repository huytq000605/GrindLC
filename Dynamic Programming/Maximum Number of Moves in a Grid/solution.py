class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [(-1, 1), (0, 1), (1, 1)]
        @cache
        def dfs(r, c):
            result = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] <= grid[r][c]:
                    continue
                result = max(result, 1 + dfs(nr, nc))
            return result
        
        return max([dfs(r, 0) for r in range(m)])    
