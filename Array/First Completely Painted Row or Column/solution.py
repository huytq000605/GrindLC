class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rs, cs = [n for _ in range(m)], [m for _ in range(n)]
        map_rc = dict()
        for r in range(m):
            for c in range(n):
                map_rc[mat[r][c]] = (r, c)
        
        for i, num in enumerate(arr):
            r, c = map_rc[num]
            rs[r] -= 1
            if rs[r] == 0:
                return i
            cs[c] -= 1
            if cs[c] == 0:
                return i
        return -1
