class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rs = [r for r in range(m) for c in range(n) if grid[r][c] == 1]
        cs = [c for c in range(n) for r in range(m) if grid[r][c] == 1]
        ps = len(rs)
        meeting = (rs[ps//2], cs[ps//2])
        return sum(abs(r - meeting[0]) for r in rs) + sum(abs(c - meeting[1]) for c in cs)
