class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m-3+1):
            for j in range(n-3+1):
                h = 0
                for r in range(i, i +3):
                    for c in range(j, j+3):
                        if r == i+1 and c != j+1:
                            continue
                        h += grid[r][c]
                result = max(h, result)
        return result
