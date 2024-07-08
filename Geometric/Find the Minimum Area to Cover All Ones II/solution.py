class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def min_rectangle(r1, r2, c1, c2):
            mnr, mxr, mnc, mxc = m, -1, n, -1
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if grid[r][c]:
                        mnr = min(mnr, r)
                        mxr = max(mxr, r)
                        mnc = min(mnc, c)
                        mxc = max(mxc, c)
            if mxr == -1: return math.inf
            return (mxr - mnr + 1) * (mxc - mnc + 1)
        
        def dfs(parts, r1, r2, c1, c2):
            if parts == 1:
                return min_rectangle(r1, r2, c1, c2)
            result = math.inf
            for p in range(1, parts):
                for r in range(r1, r2):
                    result = min(result, dfs(p, r1, r, c1, c2) + dfs(parts - p, r + 1, r2, c1, c2))
                for c in range(c1, c2):
                    result = min(result, dfs(p, r1, r2, c1, c) + dfs(parts - p, r1, r2, c + 1, c2))
            
            return result
        return dfs(3, 0, m-1, 0, n-1)
