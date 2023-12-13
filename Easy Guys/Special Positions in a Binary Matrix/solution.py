class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        result = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and rows[r] == 1 and cols[c] == 1:
                    result += 1
        return result
