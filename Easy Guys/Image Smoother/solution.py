class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                cells = 0
                s = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= r + dr < m and 0 <= c + dc < n:
                            cells += 1
                            s += img[r+dr][c+dc]
                result[r][c] = s // cells
        return result
