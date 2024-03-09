class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        Y = [0, 0, 0]
        O = [0, 0, 0]
        for r in range(m):
            for c in range(n):
                v = grid[r][c]
                if r == c and r <= m // 2: Y[v] += 1
                elif r + c == n-1 and r <= m // 2: Y[v] += 1
                elif r >= m//2 and c == n//2: Y[v] += 1
                else: O[v] += 1
        return min(
            Y[1] + Y[2] + min(O[0] + O[1], O[0] + O[2]), # Y = 0
            Y[0] + Y[2] + min(O[1] + O[2], O[1] + O[0]), # Y = 1
            Y[0] + Y[1] + min(O[2] + O[0], O[2] + O[1])# Y = 2
        )
                
