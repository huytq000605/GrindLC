class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def dfs():
            extras = []
            zeros = []
            for r in range(3):
                for c in range(3):
                    if grid[r][c] == 0:
                        zeros.append((r, c))
                    elif grid[r][c] > 1:
                        extras.append((r, c))
            
            if len(zeros) == 0:
                return 0
            
            result = 1000
            for r1, c1 in extras:
                for r2, c2 in zeros:
                    grid[r1][c1] -= 1
                    grid[r2][c2] += 1
                    result = min(result, abs(r1 - r2) + abs(c1 - c2) + dfs())
                    grid[r1][c1] += 1
                    grid[r2][c2] -= 1
            return result
            
        return dfs()
            
            
            
