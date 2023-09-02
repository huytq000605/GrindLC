class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d = set(dictionary)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            result = 1 + dfs(i+1)
            for j in range(i, n):
                if s[i:j+1] in d:
                    result = min(result, dfs(j+1))
            return result
        return dfs(0)
