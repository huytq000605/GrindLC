class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dfs(num, n):
            if n == 1:
                return num
            result = 0
            for i in range(num):
                result += dfs(num - i, n - 1)
            return result
        return dfs(5, n)