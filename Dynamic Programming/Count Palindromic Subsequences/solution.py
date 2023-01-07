class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        result = 0
        for i in range(10):
            for j in range(10):
                pattern = str(i) + str(j) + "*" + str(j) + str(i)
                @cache
                def dfs(i, j):
                    nonlocal pattern
                    if i >= n:
                        if j == 5:
                            return 1
                        return 0
                    result = dfs(i+1, j)
                    if j < 5 and (s[i] == pattern[j] or pattern[j] == "*"):
                        result += dfs(i+1, j+1)
                    return result % MOD
                result = (result + dfs(0, 0)) % MOD
        return result
