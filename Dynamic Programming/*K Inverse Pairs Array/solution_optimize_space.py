class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # we always try to put number in descending order
        # dfs(n, k) = dfs(n-1, k) + dfs(n-1, k-1) + ... dfs(n-1, k - (n-1))
        # dp[m][k] = sum(dp[m-1][l] for l in range(k-(m-1), k+1))
        # dp[m][k] = number of arrays to put numbers from [m, n] into array to have k inverse pairs
        dp = [0 for _ in range(k+1)]
        dp[0] = 1
        for num in range(n, 0, -1):
            next_dp = [0 for _ in range(k+1)]
            # k+2 for last element for access [-1] to be 0 (quick hack for prefix sum)
            prefix_dp = [0 for _ in range(k+2)]
            for j in range(k+1):
                if j > 0: prefix_dp[j] = prefix_dp[j-1]
                prefix_dp[j] += dp[j]
            for pairs in range(k+1):
                next_dp[pairs] = (prefix_dp[pairs] - prefix_dp[max(0, pairs-(num-1)) - 1]) % MOD
            dp = next_dp
        return dp[k] % MOD


