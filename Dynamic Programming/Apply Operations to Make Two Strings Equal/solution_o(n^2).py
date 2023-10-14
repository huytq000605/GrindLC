class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        n = len(diffs)
        @cache
        def dfs(i, free_swap):
            if i >= n:
                if free_swap:
                    return math.inf
                return 0
            result = dfs(i+1, free_swap + 1) + x
            if i < n-1:
                result = min(result, diffs[i+1] - diffs[i] + dfs(i+2, free_swap))
            if free_swap:
                result = min(result, dfs(i+1, free_swap - 1))
            return result
        result = dfs(0, 0)
        if result == math.inf:
            return -1
        return result
