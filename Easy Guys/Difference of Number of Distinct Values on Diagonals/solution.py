class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0 for j in range(n)] for i in range(m)]
        for r in range(m):
            for c in range(n):
                tl_r, tl_c = r-1, c-1
                tl = set()
                while tl_r >= 0 and tl_c >= 0:
                    tl.add(grid[tl_r][tl_c])
                    tl_r, tl_c = tl_r - 1, tl_c - 1
                
                br_r, br_c = r+1, c+1
                br = set()
                while br_r < m and br_c < n:
                    br.add(grid[br_r][br_c])
                    br_r, br_c = br_r + 1, br_c + 1
                
                result[r][c] = abs(len(tl) - len(br))
        return result
