class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        mod = 10**9 + 7
        @cache
        def dfs(idx, cur):
            if idx >= n:
                if cur == 2:
                    return 1
                else:
                    return 0
            result = 0
            if corridor[idx] == "S":
                if cur == 2:
                    return 0
                else:
                    if cur + 1 == 2:
                        result =  dfs(idx + 1, 0) + dfs(idx + 1, cur + 1)
                    else:
                        result = dfs(idx + 1, cur + 1)
            else:
                if cur == 2:
                    result = dfs(idx + 1, 0) + dfs(idx + 1, cur)
                else:
                    result = dfs(idx + 1, cur)
            return result % mod
        return dfs(0, 0)