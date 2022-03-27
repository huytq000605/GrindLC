class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for row in range(len(mat)):
            rows.append((sum(mat[row]), row))
        rows.sort()
        return map(lambda e: e[1], rows[:k])