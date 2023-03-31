class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        prefix = [[0 for j in range(n+1)] for i in range(m+1)]
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                val = 1 if pizza[r][c] == "A" else 0
                prefix[r][c] = prefix[r+1][c] + prefix[r][c+1] - prefix[r+1][c+1] + val
        
        @cache
        def dfs(r, c, k):
            if prefix[r][c] < k: return 0
            if k == 1: return 1
            
            result = 0
            # horizontal cut
            for nr in range(r+1, m):
                if prefix[r][c] - prefix[nr][c] > 0:
                    result += dfs(nr,c,k-1)
            # vertical cut
            for nc in range(c+1, n):
                if prefix[r][c] - prefix[r][nc] > 0:
                    result += dfs(r, nc, k-1)
            return result % MOD
        return dfs(0, 0, k)
