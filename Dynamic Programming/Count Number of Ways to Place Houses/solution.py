class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, up, down):
            if i >= n:
                return 1
            result = 0
            if not up:
                result += dfs(i+1, True, False)
            if not down:
                result += dfs(i+1, False, True)
            if not up and not down:
                result += dfs(i+1, True, True)
            result += dfs(i+1, False, False)
            return result % MOD
        return dfs(0, False, False)
