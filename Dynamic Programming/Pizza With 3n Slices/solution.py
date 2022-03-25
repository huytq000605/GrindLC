class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        
        @cache
        def dfs(idx, k, take_first):
            if idx >= len(slices) or k == 0:
                return 0
            if idx == n - 1 and take_first:
                return 0
            if idx == 0:
                return max(dfs(idx + 1, k, False), dfs(idx + 2, k -1, True) + slices[0])
            return max(dfs(idx + 1, k, take_first), dfs(idx + 2, k - 1, take_first) + slices[idx])
        
        result = dfs(0, n // 3, False)
        return result