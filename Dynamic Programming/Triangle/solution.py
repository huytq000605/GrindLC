class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        m = len(triangle)
        for row in range(1, m):
            n = len(triangle[row])
            cur = [math.inf for i in range(n)]
            for col in range(n):
                for prev_col in range(col - 1, col + 1):
                    if prev_col < 0 or prev_col >= len(prev):
                        continue
                    cur[col] = min(cur[col], prev[prev_col] + triangle[row][col])
            prev = cur
        return min(prev)
