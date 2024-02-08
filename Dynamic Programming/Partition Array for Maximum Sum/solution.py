class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dfs(i):
            if i >= len(arr):
                return 0
            result = 0
            mx = 0
            for j in range(i, min(len(arr), i + k)):
                mx = max(mx, arr[j])
                result = max(result, (j - i + 1) * mx + dfs(j+1))
            return result
        return dfs(0)
