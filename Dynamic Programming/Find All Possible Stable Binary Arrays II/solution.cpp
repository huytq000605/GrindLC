class Solution {
public:
    int numberOfStableArrays(int zero, int one, int t) {
        // dp[z][o][p] = number of stable binary arrays with z "0", o "1", ending is p (0 or 1)
        // dp[z][o][1] = sum(dp[z][o-t][0] for t in [1, limit])
        // dp[z][o][0] = sum(dp[z-t][o][1] for t in [1, limit])
        //             = dp[z-1][o][1] + dp[z-2][o][1] + ... dp[z-t][o][1] + dp[z-t-1][o][1] - dp[z-t-1][o][1]
        //             = dp[z-1][o][1] + dp[z-1][o][0] - dp[z-t-1][o][1]
        vector<vector<vector<int>>> dp(zero+1, vector<vector<int>>(one + 1, vector<int>(2)));
        for(int i = 1; i <= min(zero, t); ++i) {
            dp[i][0][0] = 1;
        }
        for(int i = 1; i <= min(one, t); ++i) {
            dp[0][i][1] = 1;
        }
        int MOD = 1e9 + 7;
        for(int z = 1; z <= zero; ++z) {
            for(int o = 1; o <= one; ++o) {
                dp[z][o][0] = (dp[z-1][o][1] + dp[z-1][o][0]) % MOD;
                if(z-t-1 >= 0) dp[z][o][0] = ((dp[z][o][0] - dp[z-t-1][o][1]) % MOD + MOD) % MOD;

                dp[z][o][1] = (dp[z][o-1][1] + dp[z][o-1][0]) % MOD;
                if(o-t-1 >= 0) dp[z][o][1] = ((dp[z][o][1] - dp[z][o-t-1][0]) % MOD + MOD) % MOD;
            }
        }
        return (dp[zero][one][0] + dp[zero][one][1])% MOD;
    }
};
