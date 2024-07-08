class Solution {
public:
    int kInversePairs(int n, int k) {
        int MOD = 1000000007;
        // dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... + dp[n-1][k-(n-1)]
        // dp[n][k] = number of array with size n and k inverse pairs
        vector<int> dp(k + 1, 0);
        dp[0] = 1;
        for(int sz = 1; sz <= n; sz++) {
            vector<int> next_dp(k+1, 0);
            vector<int> prefix_dp(k+1, 0);
            for(int pairs = 0; pairs <= k; pairs++) {
                if(pairs) prefix_dp[pairs] = prefix_dp[pairs-1];
                prefix_dp[pairs] = (prefix_dp[pairs] + dp[pairs]) % MOD;
            }

            for(int pairs = 0; pairs <= k; pairs++) {
                next_dp[pairs] = prefix_dp[pairs];
                if(pairs - (sz - 1) - 1 >= 0) {
                    next_dp[pairs] -= prefix_dp[pairs - (sz - 1) - 1];
                }
                next_dp[pairs] = (next_dp[pairs] + MOD) % MOD;
            }

            dp = next_dp;
        }
        return dp[k] % MOD;
    }
};
