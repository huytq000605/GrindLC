class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        n = len(diffs)
        if n % 2 == 1:
            return -1
        @cache
        def dfs(i):
            if i >= n:
                return 0
            result = dfs(i+1) + x
            if i < n-1:
                result = min(result, (diffs[i+1] - diffs[i])*2 + dfs(i+2))
            return result
        return dfs(0) // 2
