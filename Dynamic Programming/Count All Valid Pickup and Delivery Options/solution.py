class Solution:
    def countOrders(self, n: int) -> int:
        # Can move to math => O(1) space
        @cache
        def dfs(p, d):
            if d == 0:
                return 1
            result = 0
            if p > 0:
                result += p * dfs(p-1, d)
            if p < d:
                result += (d - p) * dfs(p, d-1)
            return result % (10**9+7)
        return dfs(n, n)