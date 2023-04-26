class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx = 0
        m = len(mat)
        for r in range(m):
            mx = max(mx, sum(mat[r]))
        for r in range(m):
            if sum(mat[r]) == mx:
                return r, mx
