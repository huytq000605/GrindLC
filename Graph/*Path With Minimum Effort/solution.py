class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        min_effort = [[math.inf for j in range(n)] for i in range(m)]
        min_effort[0][0] = 0
        pq = [(0, 0, 0)]
        dirs = [(1,0), (0, 1), (-1,0), (0, -1)]
        while pq:
            effort, row, col = heappop(pq)
            if row == m - 1 and col == n - 1:
                return effort
            if effort > min_effort[row][col]:
                continue
            for d in dirs:
                nr, nc = row + d[0], col + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                next_effort = max(effort, abs(heights[nr][nc] - heights[row][col]))
                if next_effort < min_effort[nr][nc]:
                    min_effort[nr][nc] = next_effort
                    heappush(pq, (next_effort, nr, nc))
        return -1