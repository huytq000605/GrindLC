class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        new_mat = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r % 2 == 0:
                    new_mat[r][c] = mat[r][(((c - k) % n) + n) % n]
                else:
                    new_mat[r][c] = mat[r][(c + k) % n]
                if new_mat[r][c] != mat[r][c]:
                    return False
        return True
