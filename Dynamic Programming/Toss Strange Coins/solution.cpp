class Solution {
public:
    double probabilityOfHeads(vector<double>& prob, int target) {
        // dp[i][j] = after i coins having j heads
        // dp[i][j] = dp[i-1][j] * (1 - prob[i]) + dp[i-1][j-1] * prob[i]
        vector<double> dp(target + 1, 0);
        dp[0] = 1.0;
        for(auto p: prob) {
            vector<double> ndp(target + 1, 0);
            for(int heads = 0; heads <= target; heads++) {
                ndp[heads] = dp[heads] * (1 - p);
                if(heads) {
                    ndp[heads] += dp[heads-1] * p;
                }
            }
            dp = ndp;
        }
        return dp[target];
    }
};
