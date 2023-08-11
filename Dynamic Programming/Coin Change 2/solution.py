class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # TOP DOWN
        @cache
        def dfs(i, coin):
            if i >= len(coins):
                if coin == amount:
                    return 1
                return 0
            if coin > amount:
                return 0
            # dp[i][j] = dp[i][j+coins[i]] + dp[i+1][j]
            return dfs(i, coin + coins[i]) + dfs(i+1, coin)
        
        # BOTTOM UP
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n + 1)]
        dp[n][amount] = 1
        for i in reversed(range(n)):
            for j in reversed(range(amount+1)):
                dp[i][j] = dp[i+1][j]
                if j + coins[i] > amount: continue
                dp[i][j] += dp[i][j + coins[i]]
        
        return dp[0][0]
