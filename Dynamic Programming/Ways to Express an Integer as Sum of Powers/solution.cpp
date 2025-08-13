class Solution {
public:
    int numberOfWays(int n, int x) {
        int MOD = 1e9 + 7;
        vector<int> dp(n+1);
        dp[0] = 1;
        for(int i = 1; pow(i, x) <= n; ++i) {
            int p = pow(i, x);
            for(int num = n; num >= p; --num) {
                dp[num] = (dp[num] + dp[num-p]) % MOD;
            }
        }
        return dp[n];
    }
};
