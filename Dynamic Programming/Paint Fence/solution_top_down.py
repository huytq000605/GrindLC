class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def dfs(i, j):
            if j < 0: return 0
            if i >= n:
                return 1
            return dfs(i+1, j-1) + dfs(i+1, 1) * (k-1)
        return dfs(0, 2)
                
