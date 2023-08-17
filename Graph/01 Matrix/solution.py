class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ds = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(mat), len(mat[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]: mat[i][j] = -1
                else: dq.append((i, j, 0))
        while dq:
            r, c, s = dq.popleft()
            s += 1
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if mat[nr][nc] == -1:
                    mat[nr][nc] = s
                    dq.append((nr, nc, s))

        return mat
