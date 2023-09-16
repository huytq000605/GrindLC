class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[math.inf for j in range(n)] for i in range(m)]
        efforts[0][0] = 0
        
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pq = [(0, 0, 0)]
        while pq:
            e, r, c = heappop(pq)
            if r == m-1 and c == n-1:
                return e
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                if ne < efforts[nr][nc]:
                    efforts[nr][nc] = ne
                    heappush(pq, (ne, nr, nc))  
        return -1
