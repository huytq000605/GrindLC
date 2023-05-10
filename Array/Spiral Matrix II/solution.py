class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mnr, mnc = 0, 0
        mxr, mxc = n-1, n-1
        result = [[0 for _ in range(n)] for _ in range(n)]
        i = 1
        while i <= n*n:
            for c in range(mnc, mxc+1):
                result[mnr][c] = i
                i += 1
            mnr += 1
            for r in range(mnr, mxr+1):
                result[r][mxc] = i
                i += 1
            mxc -= 1
            for c in range(mxc, mnc-1, -1):
                result[mxr][c] = i
                i += 1
            mxr -= 1
            for r in range(mxr, mnr-1, -1):
                result[r][mnc] = i
                i += 1
            mnc += 1
        return result
