class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        prefix = [[0 for i in range(k + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        prefix[0] = [1 for i in range(k+1)]
        MOD = 10**9+7
        for i in range(1, n+1):
            for j in range(0, k+1):
                if j >= i:
                    dp[i][j] = (prefix[i-1][j] - prefix[i-1][j-i]) % MOD
                else:
                    dp[i][j] = prefix[i-1][j] % MOD
                if j > 0:
                    prefix[i][j] = prefix[i][j-1]
                prefix[i][j] += dp[i][j]
        return dp[-1][-1]
                
    # dfs(n, k) = dfs(n-1, k) + dfs(n-1, k-1) + dfs(n-1, k-2) + ... dfs(n-1, 0)
    # dfs(n-1, k) = dfs(n-2, k) + dfs(n-2, k-1) + ... dfs(n-2, k-(n-1))
    # => dp[i][k] = sum(dp[i-1][l] for l in [k-i-1, k])