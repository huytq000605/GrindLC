class Solution:
    def checkRecord(self, n: int) -> int:
        @cache
        def dfs(i, absent, late):
            if absent >= 2:
                return 0
            if late >= 3:
                return 0
            if i >= n:
                return 1
            result = dfs(i+1, absent, 0) + dfs(i+1, absent+1, 0) + dfs(i+1, absent, late + 1)
            return result % (10**9 + 7)
        return dfs(0, 0, 0)
            