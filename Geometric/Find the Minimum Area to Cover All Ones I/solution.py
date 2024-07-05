class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mxr, mxc = -1, -1
        mnr, mnc = m, n
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    mxr = max(mxr, r)
                    mxc = max(mxc, c)
                    mnr = min(mnr, r)
                    mnc = min(mnc, c)
        return (mxr - mnr + 1) * (mxc - mnc + 1)
