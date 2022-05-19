class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        @cache
        def dfs(r, c):
            result = 0
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or matrix[nr][nc] <= matrix[r][c]:
                    continue
                result = max(result, dfs(nr, nc))
            return 1 + result
        
        return max(dfs(r, c) for r in range(m) for c in range(n))