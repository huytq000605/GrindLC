class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int> dp(high + 1, 0);
        dp[0] = 1;
        int MOD = 1e9 + 7;
        for(int i{1}; i <= high; ++i) {
            if(i - zero >= 0) dp[i] = (dp[i] + dp[i-zero]) % MOD;
            if(i - one >= 0) dp[i] = (dp[i] + dp[i-one]) % MOD;
        }
        return accumulate(dp.begin() + low, dp.end(), 0ll) % MOD;
    }
};
