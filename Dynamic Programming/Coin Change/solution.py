class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(n):
            if n < 0:
                return math.inf
            if n == 0:
                return 0
            return 1 + min(dfs(n - coin) for coin in coins)
        result = dfs(amount)
        if result == math.inf:
            return -1
        return result
