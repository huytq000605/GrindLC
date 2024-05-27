class Solution {
public:
    int MOD = pow(10, 9) + 7;
    int checkRecord(int n) {
        vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(3, vector<int>(2, 0)));
        for(int j = 0; j < 3; j++) {
            for(int k = 0; k < 2; k++) {
                dp[0][j][k] = 1;
            }
        }
        // dp[i][j][k] = # of valid sequences of length i
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j < 3; j++) {
                for(int k = 0; k < 2; k++) {
                    dp[i][j][k] = dp[i-1][0][k];
                    if(j+1 < 3) dp[i][j][k] = (dp[i][j][k] + dp[i-1][j+1][k]) % MOD;
                    if(k+1 < 2) dp[i][j][k] = (dp[i][j][k] + dp[i-1][0][k+1]) % MOD;
                }
            }
        }
        return dp[n][0][0];

        // TOP DOWN
        // auto dfs = [&](int n, int late, int absent, auto & dfs_ref) -> int {
        //     if(late >= 3 || absent >= 2) return 0;
        //     if(n <= 0) return 1;
        //     if(dp[n][late][absent] != -1) return dp[n][late][absent];
        //     int result = dfs_ref(n-1, 0, absent, dfs_ref);
        //     result += dfs_ref(n-1, late + 1, absent, dfs_ref);
        //     result %= MOD;
        //     result += dfs_ref(n-1, 0, absent + 1, dfs_ref);
        //     result %= MOD;
        //     dp[n][late][absent] = result;
        //     return result;
        // };
        // return dfs(n, 0, 0, dfs);
    }
    
};
