class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        prefix = [1 for _ in range(m*n)]
        for r in range(m):
            for c in range(n):
                idx = r*n + c
                if idx > 0:
                    prefix[idx] = prefix[idx-1]
                prefix[idx] = (prefix[idx] * grid[r][c]) % MOD
                
        suffix = [1 for _ in range(m*n)]
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                idx = r*n + c
                if idx < m*n-1:
                    suffix[idx] = suffix[idx+1]
                suffix[idx] = (suffix[idx] * grid[r][c]) % MOD
        
        for r in range(m):
            for c in range(n):
                idx = r * n + c
                pref = 1
                suff = 1
                if idx > 0:
                    pref = prefix[idx-1]
                if idx < m*n-1:
                    suff = suffix[idx+1]
                
                grid[r][c] = (pref * suff) % MOD
        
        return grid
