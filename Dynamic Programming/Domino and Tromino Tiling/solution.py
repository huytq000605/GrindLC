class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(col1, col2):
            if col1 > n or col2 > n:
                return 0
            if col1 == n and col2 == n:
                return 1
            
            result = 0
            if col1 > col2:
                result += dfs(col1, col2 + 2)
                if col1 - col2 == 1:
                    result += dfs(col1 + 1, col2 + 2)
            elif col1 < col2:
                result += dfs(col1 + 2, col2)
                if col1 - col2 == -1:
                    result += dfs(col1 + 2, col2 + 1)
            else:
                result += dfs(col1 + 1, col2 + 1) + dfs(col1 + 2, col2 + 1) + dfs(col1 + 1, col2 + 2) + dfs(col1 + 2, col2)
            return result % MOD
        return dfs(0, 0)
                