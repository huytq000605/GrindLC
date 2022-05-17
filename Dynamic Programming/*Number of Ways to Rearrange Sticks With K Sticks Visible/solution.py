class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        @cache
        def dfs(n, k):
            if k == 0:
                return 0
            if k == n:
                return 1
            # Select right most stick
            # If we select the highest stick => just dfs(n-1, k-1)
            # If we select the non-highest stick => we have n-1 ways to select them => dfs(n-1, k)
            result = dfs(n-1, k-1) + dfs(n-1, k) * (n-1)
            return result % (10**9 + 7)
        return dfs(n, k)