class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        def dfs(u):
            nonlocal result
            if u >= len(cost):
                return 0
            l = dfs(u * 2 + 1)
            r = dfs(u * 2 + 2)
            result += abs(l - r)
            cost[u] += max(l, r)
            return cost[u]
        dfs(0)
        return result
