class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        seen1, seen2 = set(), set()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or heights[r][c] > heights[nr][nc] or (nr,nc) in seen:
                    continue
                dfs(nr, nc, seen)

        for c in range(n):
            dfs(0, c, seen1)
            dfs(m-1, c, seen2)

        for r in range(m):
            dfs(r, 0, seen1)
            dfs(r, n-1, seen2)
        return seen1 & seen2
