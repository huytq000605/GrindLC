class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0, *cuts, n]
        m = len(cuts)
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            result = math.inf
            for c in range(i+1, j):
                result = min(result, cuts[j] - cuts[i] + dfs(i, c) + dfs(c, j))
            return result
            
        return dfs(0, m-1)
