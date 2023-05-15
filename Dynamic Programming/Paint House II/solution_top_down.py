class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        @cache
        def dfs(i, j):
            if i >= m:
                return 0
            result = math.inf
            for k in range(n):
                if k == j: continue
                result = min(result, costs[i][k] + dfs(i+1, k))
            return result
        return dfs(0, -1)
