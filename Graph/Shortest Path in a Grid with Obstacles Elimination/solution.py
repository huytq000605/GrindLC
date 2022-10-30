class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[math.inf for l in range(k+1)] for j in range(n)] for i in range(m)]
        dp[0][0][k] = 0
        
        result = math.inf
        q = deque([(0, 0, k, 0)])
        ds = [(0,1), (1,0), (0, -1), (-1, 0)]
        
        while q:
            r, c, l, s = q.popleft()
            if r == m-1 and c == n-1:
                result = min(result, s)
                
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] == 1 and l == 0:
                    continue
                nl = l if grid[nr][nc] == 0 else l-1
                if dp[nr][nc][nl] > s+1:
                    dp[nr][nc][nl] = s+1
                    q.append((nr, nc, nl, s+1))
        
        if result == math.inf:
            return -1
        return result
