class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dfs(start, end):
            if end - start + 1 < 3:
                return 0
            result = math.inf
            for i in range(start + 1, end):
                result = min(result, values[start]*values[end]*values[i] + dfs(start, i) + dfs(i , end))
            return result
        return dfs(0, len(values) - 1)