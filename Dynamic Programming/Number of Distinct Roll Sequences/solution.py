class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, prev, prev_prev):
            if i >= n:
                return 1
            result = 0
            for dice in range(1, 7):
                if dice == prev or dice == prev_prev:
                    continue
                if dice % 2 == 0 and prev % 2 == 0:
                    continue
                if dice % 3 == 0 and prev % 3 == 0:
                    continue
                result += dfs(i + 1, dice, prev)
            return result % MOD
        return dfs(0, -1, -1)