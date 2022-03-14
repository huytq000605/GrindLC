class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i, prev, k, cur):
            if k < 0:
                return math.inf
            if i >= n:
                return 0
            result = dfs(i + 1, prev, k - 1, cur)
            if prev == s[i]:
                if cur >= 2 and cur != 9 and cur != 99:
                    result = min(result, dfs(i+1, prev, k, cur + 1))
                else:
                    result = min(result, 1 + dfs(i+1, prev, k, cur + 1))
            else:
                result = min(result, 1 + dfs(i+1, s[i], k, 1))
            return result
        return dfs(0, "", k, 0)