class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0 for i in range(k + 1)]
        dp[0] = 1
        prefix = [1 for i in range(k+1)]
        MOD = 10**9+7
        for i in range(1, n+1):
            new_prefix = [0 for i in range(k+1)]
            for j in range(0, k+1):
                if j >= i:
                    dp[j] = (prefix[j] - prefix[j-i]) % MOD
                else:
                    dp[j] = prefix[j] % MOD
                if j > 0:
                    new_prefix[j] = new_prefix[j-1]
                new_prefix[j] += dp[j]
            prefix = new_prefix
        return dp[-1]
                
    # dfs(n, k) = dfs(n-1, k) + dfs(n-1, k-1) + dfs(n-1, k-2) + ... dfs(n-1, 0)
    # dfs(n-1, k) = dfs(n-2, k) + dfs(n-2, k-1) + ... dfs(n-2, k-(n-1))
    # => dp[i][k] = sum(dp[i-1][l] for l in [k-i-1, k])